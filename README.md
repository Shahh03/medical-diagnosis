# Medical Diagnosis AI

Medical Diagnosis AI is a university project currently in the **data acquisition stage**.

So far, the project focuses on collecting structured medical-condition information from NHS Inform and preparing a verified local dataset for later use.

---

## Implemented So Far

### NHS Inform A–Z Scraping

The scraper starts from the NHS Inform A–Z conditions index:

https://www.nhsinform.scot/illnesses-and-conditions/a-to-z/

It discovers condition links and processes them sequentially.

### Extracted Fields

For each condition, the scraper currently extracts:

- Condition name
- Symptoms
- Causes
- Warnings
- Recommendations / treatment information
- Source URL

### Extraction Fallbacks

The scraper includes several fallbacks for pages with different structures:

- Introductory-text fallback when a dedicated symptoms section is missing
- Warning-text fallback for urgent advice such as `999`, `111`, or urgent GP guidance
- Linked treatment/prevention-page fallback when recommendations are stored on another NHS Inform page

### Sequential Scraping

The current crawler processes conditions one at a time automatically:

```text
Condition 1
    ↓
Scrape
    ↓
Save
    ↓
Wait
    ↓
Condition 2
    ↓
Repeat
```

This helps reduce request failures during a long crawl.

### Retry Handling

Temporary request failures are retried with increasing delays.

The scraper currently handles retryable responses such as:

- 403
- 408
- 429
- 500
- 502
- 503
- 504

### Resume Support

Each successful condition is saved immediately.

If the scraper is interrupted, it can be run again and already-saved condition URLs are skipped.

### Local Dataset Output

The scraper currently generates:

```text
data/
├── nhs_conditions_sequential.json
├── nhs_conditions_sequential.csv
├── nhs_conditions_errors.json
└── nhs_conditions_errors.csv
```

The JSON and CSV files contain successfully scraped records, while the error files contain pages that failed during scraping.

---

## Current Project Structure

```text
medical-diagnosis/
│
├── app/
│   ├── api/
│   │
│   ├── database/
│   │   └── mongodb.py
│   │
│   └── scraper/
│       └── nhs_scraper.py
│
├── data/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```

---

## Current Technologies

- Python
- Requests
- BeautifulSoup
- Pandas
- PyMongo
- python-dotenv
- Jupyter
- ipykernel

---

## Current Requirements

```txt
requests
beautifulsoup4
pandas
pymongo
python-dotenv
jupyter
ipykernel
```

Install them with:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

MongoDB configuration is stored in `.env`:

```env
MONGODB_URI=your_mongodb_connection_string
MONGODB_DB=medical_diagnosis_ai
```

The `.env` file should not be committed to Git.

MongoDB connectivity has been set up, but scraped records are not being inserted into MongoDB yet.

---

## Current Dataset Structure

A scraped condition currently looks like this:

```json
{
  "condition": "Asthma",
  "symptoms": "...",
  "causes": "...",
  "warnings": "...",
  "recommendations": "...",
  "source_url": "...",
  "symptoms_source": "section",
  "warnings_source": "section",
  "recommendations_source": "section",
  "recommendations_source_url": null,
  "index_label": "Asthma"
}
```

The source fields help show whether data came from:

- the normal page section
- an introductory fallback
- a warning-text fallback
- a linked treatment/prevention page

---

## Current Status

The project is currently focused on:

```text
NHS Inform
    ↓
A–Z condition discovery
    ↓
Sequential scraping
    ↓
Structured field extraction
    ↓
Local JSON / CSV dataset
    ↓
Dataset verification
```

MongoDB storage, preprocessing, model training, and the Flask API are later stages and are not implemented yet.

---

## Disclaimer

This project is for educational and research purposes only.

It is not intended to provide professional medical diagnosis or replace advice from qualified healthcare professionals.
