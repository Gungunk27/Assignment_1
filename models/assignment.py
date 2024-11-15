from pymongo import MongoClient
from config import MONGO_URI
from datetime import datetime

client = MongoClient(MONGO_URI)
db = client.assignment_portal

assignments_collection = db.assignments

def upload_assignment(data):
    data["timestamp"] = datetime.utcnow()
    return assignments_collection.insert_one(data)

def get_assignments_by_admin(admin_email):
    return list(assignments_collection.find({"admin": admin_email}))

def update_assignment_status(assignment_id, status):
    return assignments_collection.update_one(
        {"_id": assignment_id}, {"$set": {"status": status}}
    )
