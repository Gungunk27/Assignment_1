from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client.assignment_portal

users_collection = db.users

def create_user(data):
    if users_collection.find_one({"email": data["email"]}):
        return {"error": "User already exists"}
    data["password"] = generate_password_hash(data["password"])
    return users_collection.insert_one(data)

def authenticate_user(email, password):
    user = users_collection.find_one({"email": email})
    if user and check_password_hash(user["password"], password):
        return user
    return None
