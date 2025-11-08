import pandas as pd
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, DuplicateKeyError
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CSVPATH = "data.csv"
MONGO_HOST = "mymongo"
MONGO_PORT = 27017
MONGO_DB = "ondreji"
MONGO_COLLECTION = "prosim"

def load_csv() -> list:
    data = pd.read_csv(CSVPATH)
    logger.info(
        f"CSV read succesfully"
    )
    return data

def insert_to_db(data) -> None:
    """Get data to MongoDB."""
    try:
        # Connect to MongoDB
        client = MongoClient(
            f"mongodb://{MONGO_HOST}:{MONGO_PORT}/", serverSelectionTimeoutMS=5000
        )
        if not client.server_info():
            raise Exception("Could not connect to MongoDB server.")
        db = client[MONGO_DB]
        collection = db[MONGO_COLLECTION]
        logger.info(
            f"Connected to MongoDB at {MONGO_HOST}:{MONGO_PORT}, DB: {MONGO_DB}, "
            f"Collection: {MONGO_COLLECTION}"
        )
        collection.insert_many(data.to_dict('records'))
        logger.info(
            f"Data inserted to ondreji.prosim"
        )
    except Exception as e:
        logger.error(f"Error: {e}")

def main() -> None:
    data = load_csv()
    insert_to_db(data)

if __name__ == "__main__":
    main()