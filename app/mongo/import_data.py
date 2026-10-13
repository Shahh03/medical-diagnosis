import json
import sys
from pathlib import Path

from pymongo import ReplaceOne


ROOT_DIR = Path(__file__).resolve().parents[2]

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app.mongo.mongodb import db


DATA_FILE = (
    ROOT_DIR
    / "app"
    / "dataset"
    / "input"
    / "conditioned"
    / "nhs_conditions_manual_final.json"
)

REQUIRED_FIELDS = {
    "condition",
    "symptoms",
    "causes",
    "warnings",
    "recommendations",
}


def validate_record(record, index):
    if set(record.keys()) != REQUIRED_FIELDS:
        raise ValueError(
            f"Invalid fields in record {index}: "
            f"{record.get('condition')}"
        )

    for field in REQUIRED_FIELDS:
        if not isinstance(record[field], str):
            raise ValueError(
                f"{record.get('condition', f'Record {index}')} "
                f"-> {field} must be a string"
            )

    if not record["condition"].strip():
        raise ValueError(
            f"Record {index} has empty condition"
        )

    if not record["symptoms"].strip():
        raise ValueError(
            f"{record['condition']} has empty symptoms"
        )


def load_conditions():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_FILE}"
        )

    with DATA_FILE.open(
        "r",
        encoding="utf-8",
    ) as file:
        conditions = json.load(file)

    if not isinstance(conditions, list):
        raise TypeError(
            "Expected the conditioned dataset to contain a list."
        )

    return conditions


def validate_conditions(conditions):
    seen = set()

    for index, record in enumerate(conditions):
        validate_record(
            record,
            index,
        )

        name = record["condition"].strip()

        if name in seen:
            raise ValueError(
                f"Duplicate condition: {name}"
            )

        seen.add(name)


def import_conditions():
    """
    Validate the conditioned five-field dataset and upsert it
    into MongoDB's `conditions` collection.

    Returns a summary dictionary so Flask can expose this action
    through the Data Handling API.
    """

    conditions = load_conditions()

    print(
        f"Loaded {len(conditions)} conditions"
    )

    validate_conditions(conditions)

    print("Dataset validation passed")

    collection = db["conditions"]

    collection.create_index(
        "condition",
        unique=True,
        name="unique_condition",
    )

    operations = [
        ReplaceOne(
            {
                "condition": record["condition"]
            },
            record,
            upsert=True,
        )
        for record in conditions
    ]

    if not operations:
        return {
            "dataset": 0,
            "inserted": 0,
            "modified": 0,
            "matched": 0,
            "mongodb_total": collection.count_documents({}),
        }

    result = collection.bulk_write(
        operations
    )

    summary = {
        "dataset": len(conditions),
        "inserted": result.upserted_count,
        "modified": result.modified_count,
        "matched": result.matched_count,
        "mongodb_total": collection.count_documents({}),
    }

    print()
    print("Import complete")
    print("----------------")
    print("Dataset:", summary["dataset"])
    print("Inserted:", summary["inserted"])
    print("Modified:", summary["modified"])
    print("Matched:", summary["matched"])
    print("MongoDB total:", summary["mongodb_total"])

    return summary


def main():
    import_conditions()


if __name__ == "__main__":
    main()
