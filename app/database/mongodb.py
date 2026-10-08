import os
from pathlib import Path

from dotenv import load_dotenv
from pymongo import MongoClient

BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")

mongo_uri = os.getenv("MONGODB_URI")
mongo_db = os.getenv("MONGODB_DB")

if not mongo_uri:
    raise ValueError("MONGODB_URI is missing from .env")

if not mongo_db:
    raise ValueError("MONGODB_DB is missing from .env")

client = MongoClient(mongo_uri)

db = client[mongo_db]

conditions_collection = db["conditions"]

# Actually test the connection
client.admin.command("ping")

print("MongoDB connection successful")
print(f"Database: {mongo_db}")