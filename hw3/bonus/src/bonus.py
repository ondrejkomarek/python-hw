# -------------------------------
# Simple Flask Server Demo
# -------------------------------
# This script creates a simple Flask server that can receive and serve
# sensor data via REST API endpoints

from flask import Flask, request, jsonify
import logging
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, DuplicateKeyError

# Create Flask application instance
app = Flask(__name__)

# Server configuration
HOST = "myserver"
PORT = 80

MONGO_HOST = "mymongo"
MONGO_PORT = 27017
MONGO_DB = "ondreji"
MONGO_COLLECTION = "prosim"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/data", methods=["GET"])
def get_data():
    """Get data from MongoDB."""
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
        print("All sensor data:")
        data = list(collection.find({}, {"_id": 0})) 
        return jsonify(data)
    except Exception as e:
        logger.error(f"Error: {e}")
    return "Not Found", 404


if __name__ == "__main__":
    logger.info(
        f"Serving at {HOST}:{PORT}"
        f"Available endpoints:"
        f" GET /data>"
    )

    app.run(host=HOST, port=PORT, debug=True)
