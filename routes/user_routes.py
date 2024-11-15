from flask import Blueprint, request, jsonify
from models.user import create_user, authenticate_user
from models.assignment import upload_assignment
from bson.objectid import ObjectId

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/register", methods=["POST"])
def register_user():
    data = request.json
    result = create_user(data)
    if "error" in result:
        return jsonify({"message": result["error"]}), 400
    return jsonify({"message": "User registered successfully"}), 201

@user_routes.route("/login", methods=["POST"])
def login_user():
    data = request.json
    user = authenticate_user(data["email"], data["password"])
    if not user:
        return jsonify({"message": "Invalid credentials"}), 401
    return jsonify({"message": "Login successful"}), 200

@user_routes.route("/upload", methods=["POST"])
def upload():
    data = request.json
    result = upload_assignment(data)
    return jsonify({"message": "Assignment uploaded successfully", "id": str(result.inserted_id)}), 201
