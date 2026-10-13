import os
import certifi
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DB = os.getenv("MONGODB_DB")

if not MONGODB_URI:
    raise ValueError("MONGODB_URI is missing from .env")

if not MONGODB_DB:
    raise ValueError("MONGODB_DB is missing from .env")

client = MongoClient(
    MONGODB_URI,
    tls=True,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=10000,
)

db = client[MONGODB_DB]


def test_connection():
    client.admin.command("ping")
    print("MongoDB connection successful")
    print("Database:", MONGODB_DB)


if __name__ == "__main__":
    test_connection()