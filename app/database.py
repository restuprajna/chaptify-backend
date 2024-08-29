from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from typing import Optional
import os

# Use environment variables for sensitive information
MONGO_DB_URL = os.getenv("MONGO_DB_URL", "mongodb://localhost:27017")

# Initialize the MongoDB client and the database
client = AsyncIOMotorClient(MONGO_DB_URL)
db = client["library_db"]  # The name of your MongoDB database

# Utility function to convert ObjectId to string
def obj_id_to_str(id: Optional[ObjectId]):
    return str(id) if id else None
