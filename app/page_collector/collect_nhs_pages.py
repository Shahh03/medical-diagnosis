import json
import random
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin, urldefrag, urlparse

import requests
from bs4 import BeautifulSoup


# ============================================================
# WINDOWS UTF-8 OUTPUT
# ============================================================

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except AttributeError:
    pass


# ============================================================
# CONFIG
# ============================================================

A_Z_URL = (
    "https://www.nhsinform.scot/"
    "illnesses-and-conditions/a-to-z/"
)

OUTPUT_DIR = Path("data")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_JSON = OUTPUT_DIR / "nhs_all_pages.json"
ERROR_JSON = OUTPUT_DIR / "nhs_all_pages_errors.json"


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/154.0.0.0 Safari/537.36"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;"
        "q=0.9,image/avif,image/webp,*/*;q=0.8"
    ),
    "Accept-Language": "en-GB,en;q=0.9",
    "Connection": "keep-alive",
}


REQUEST_TIMEOUT = 30

# Random delay is better than requesting every page at exactly the same interval.
MIN_DELAY_SECONDS = 8
MAX_DELAY_SECONDS = 12

MAX_RETRIES = 3
BACKOFF_BASE_SECONDS = 15

RETRY_STATUS_CODES = {
    403,
    408,
    429,
    500,
    502,
    503,
    504,
}


# ============================================================
# HELPERS
# ============================================================

def normalize_whitespace(text):
    return re.sub(
        r"\s+",
        " ",
        text or ""
    ).strip()


def normalize_url(url):
    clean_url, _ = urldefrag(url)

    return clean_url.rstrip("/") + "/"


def load_json(path, default):
    if not path.exists():
        return default

    try:
        with path.open(
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(file)

    except Exception:
        return default


def save_json(path, data):
    with path.open(
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=2
        )


# ============================================================
# REQUEST WITH RETRY
# ============================================================

def get_with_retry(
    session,
    url
):
    for attempt in range(
        MAX_RETRIES + 1
    ):

        try:
            response = session.get(
                url,
                timeout=REQUEST_TIMEOUT
            )

            if response.status_code == 200:
                return response

            if (
                response.status_code
                not in RETRY_STATUS_CODES
            ):
                response.raise_for_status()

            if attempt >= MAX_RETRIES:
                response.raise_for_status()

            wait_seconds = (
                BACKOFF_BASE_SECONDS
                * (2 ** attempt)
            )

            print(
                f"    HTTP "
                f"{response.status_code}. "
                f"Retrying in "
                f"{wait_seconds}s..."
            )

            time.sleep(
                wait_seconds
            )

        except requests.RequestException:

            if attempt >= MAX_RETRIES:
                raise

            wait_seconds = (
                BACKOFF_BASE_SECONDS
                * (2 ** attempt)
            )

            print(
                "    Request failed. "
                f"Retrying in "
                f"{wait_seconds}s..."
            )

            time.sleep(
                wait_seconds
            )

    raise RuntimeError(
        f"Failed to request {url}"
    )


# ============================================================
# DISCOVER ALL NHS A-Z CONDITION LINKS
# ============================================================

EXCLUDED_INDEX_LABELS = {
    "illnesses and conditions",
}

EXCLUDED_PREFIXES = [
    "how to ",
    "living with ",
    "living well with ",
    "managing ",
]


def is_condition_link(
    label,
    url
):
    label_lower = (
        label.strip().lower()
    )

    url_lower = (
        normalize_url(url).lower()
    )

    if not label_lower:
        return False

    if (
        label_lower
        in EXCLUDED_INDEX_LABELS
    ):
        return False

    for prefix in EXCLUDED_PREFIXES:

        if label_lower.startswith(
            prefix
        ):
            return False

    if (
        "/illnesses-and-conditions/"
        not in url_lower
    ):
        return False

    if "/a-to-z/" in url_lower:
        return False

    root_url = normalize_url(
        "https://www.nhsinform.scot/"
        "illnesses-and-conditions/"
    ).lower()

    if url_lower == root_url:
        return False

    return True


def discover_condition_links(
    session
):
    print(
        "Loading NHS A-Z index..."
    )

    response = get_with_retry(
        session,
        A_Z_URL
    )

    soup = BeautifulSoup(
        response.content,
        "html.parser"
    )

    discovered = {}

    for anchor in soup.find_all(
        "a",
        href=True
    ):

        label = normalize_whitespace(
            anchor.get_text(
                " ",
                strip=True
            )
        )

        absolute_url = normalize_url(
            urljoin(
                A_Z_URL,
                anchor["href"]
            )
        )

        if not is_condition_link(
            label,
            absolute_url
        ):
            continue

        discovered[
            absolute_url
        ] = label

    results = [
        {
            "index_label": label,
            "url": url
        }
        for url, label
        in discovered.items()
    ]

    results.sort(
        key=lambda item:
        item["index_label"].lower()
    )

    return results


# ============================================================
# PAGE → READABLE MARKDOWN-LIKE TEXT
# ============================================================

def extract_page_content(
    soup
):
    """
    Preserve the page structure instead of trying
    to classify medical information.

    Output looks like:

    # Condition title

    Intro paragraph

    ## Symptoms

    Text

    - item
    - item

    ### Contact your GP

    ...
    """

    content = []

    # Prefer page <main> if present.
    container = soup.find("main")

    if container is None:
        container = soup

    for element in container.find_all(
        [
            "h1",
            "h2",
            "h3",
            "h4",
            "p",
            "li",
        ]
    ):

        # Ignore navigation/footer/header elements.
        if element.find_parent(
            [
                "nav",
                "header",
                "footer",
            ]
        ):
            continue

        text = normalize_whitespace(
            element.get_text(
                " ",
                strip=True
            )
        )

        if not text:
            continue

        # Preserve heading hierarchy.
        if element.name == "h1":

            content.append(
                f"# {text}"
            )

        elif element.name == "h2":

            content.append(
                f"\n## {text}"
            )

        elif element.name == "h3":

            content.append(
                f"\n### {text}"
            )

        elif element.name == "h4":

            content.append(
                f"\n#### {text}"
            )

        elif element.name == "li":

            content.append(
                f"- {text}"
            )

        elif element.name == "p":

            content.append(
                text
            )

    return "\n".join(
        content
    ).strip()


# ============================================================
# SCRAPE ONE COMPLETE PAGE
# ============================================================

def collect_page(
    session,
    item
):
    response = get_with_retry(
        session,
        item["url"]
    )

    soup = BeautifulSoup(
        response.content,
        "html.parser"
    )

    h1 = soup.find("h1")

    if h1:
        title = normalize_whitespace(
            h1.get_text(
                " ",
                strip=True
            )
        )

    else:
        title = item[
            "index_label"
        ]

    page_content = (
        extract_page_content(
            soup
        )
    )

    return {
        "title": title,
        "index_label":
            item["index_label"],
        "url": normalize_url(
            response.url
        ),
        "content":
            page_content,
    }


# ============================================================
# MAIN
# ============================================================

def main():

    session = requests.Session()

    session.headers.update(
        HEADERS
    )

    condition_links = (
        discover_condition_links(
            session
        )
    )

    total = len(
        condition_links
    )

    print()
    print(
        f"Conditions discovered: "
        f"{total}"
    )

    # Resume support.
    pages = load_json(
        OUTPUT_JSON,
        []
    )

    errors = load_json(
        ERROR_JSON,
        []
    )

    saved_urls = {
        normalize_url(
            page["url"]
        )
        for page in pages
        if page.get("url")
    }

    print(
        f"Already collected: "
        f"{len(saved_urls)}"
    )

    print(
        f"Remaining: "
        f"{total - len(saved_urls)}"
    )

    print()

    for index, item in enumerate(
        condition_links,
        start=1
    ):

        target_url = normalize_url(
            item["url"]
        )

        if target_url in saved_urls:

            print(
                f"[{index}/{total}] "
                f"SKIP -> "
                f"{item['index_label']}"
            )

            continue

        print(
            f"[{index}/{total}] "
            f"COLLECTING -> "
            f"{item['index_label']}"
        )

        try:

            page = collect_page(
                session,
                item
            )

            pages.append(
                page
            )

            saved_urls.add(
                page["url"]
            )

            # Remove previous error
            # if this URL later succeeds.
            errors = [
                error
                for error in errors
                if normalize_url(
                    error.get(
                        "url",
                        ""
                    )
                )
                != target_url
            ]

            # Save after EVERY page.
            save_json(
                OUTPUT_JSON,
                pages
            )

            save_json(
                ERROR_JSON,
                errors
            )

            print(
                f"    SAVED -> "
                f"{page['title']}"
            )

            print(
                f"    Content length: "
                f"{len(page['content']):,} "
                f"characters"
            )

        except Exception as error:

            print(
                f"    FAILED -> "
                f"{error}"
            )

            errors = [
                existing
                for existing in errors
                if normalize_url(
                    existing.get(
                        "url",
                        ""
                    )
                )
                != target_url
            ]

            errors.append({
                "index_label":
                    item["index_label"],

                "url":
                    item["url"],

                "error":
                    str(error),
            })

            save_json(
                ERROR_JSON,
                errors
            )

        if index < total:

            delay = random.uniform(
                MIN_DELAY_SECONDS,
                MAX_DELAY_SECONDS
            )

            print(
                f"    Waiting "
                f"{delay:.1f}s..."
            )

            time.sleep(
                delay
            )

    print()
    print(
        "=" * 70
    )

    print(
        "PAGE COLLECTION FINISHED"
    )

    print(
        "=" * 70
    )

    print(
        f"Collected pages: "
        f"{len(pages)}"
    )

    print(
        f"Failed pages: "
        f"{len(errors)}"
    )

    print(
        f"Output: "
        f"{OUTPUT_JSON.resolve()}"
    )

    print(
        f"Errors: "
        f"{ERROR_JSON.resolve()}"
    )


if __name__ == "__main__":
    main()
