from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))

db = client["adaptive_test"]

questions_collection = db["questions"]
sessions_collection = db["sessions"]