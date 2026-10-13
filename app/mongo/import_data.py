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
            f"Invalid fields in record {index}: {record.get('condition')}"
        )

    if not record["condition"].strip():
        raise ValueError(f"Record {index} has empty condition")

    if not record["symptoms"].strip():
        raise ValueError(
            f"{record['condition']} has empty symptoms"
        )

    for field in REQUIRED_FIELDS:
        if not isinstance(record[field], str):
            raise ValueError(
                f"{record['condition']} -> {field} must be a string"
            )


def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_FILE}")

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        conditions = json.load(f)

    print(f"Loaded {len(conditions)} conditions")

    seen = set()

    for index, record in enumerate(conditions):
        validate_record(record, index)

        name = record["condition"].strip()

        if name in seen:
            raise ValueError(f"Duplicate condition: {name}")

        seen.add(name)

    print("Dataset validation passed")

    collection = db["conditions"]

    collection.create_index(
        "condition",
        unique=True,
        name="unique_condition",
    )

    operations = [
        ReplaceOne(
            {"condition": record["condition"]},
            record,
            upsert=True,
        )
        for record in conditions
    ]

    result = collection.bulk_write(operations)

    print()
    print("Import complete")
    print("----------------")
    print("Dataset:", len(conditions))
    print("Inserted:", result.upserted_count)
    print("Modified:", result.modified_count)
    print("Matched:", result.matched_count)
    print("MongoDB total:", collection.count_documents({}))


if __name__ == "__main__":
    main()