from flask import Blueprint, request, jsonify
from models.user import create_user, authenticate_user
from models.assignment import get_assignments_by_admin, update_assignment_status
from bson.objectid import ObjectId

admin_routes = Blueprint("admin_routes", __name__)

@admin_routes.route("/register", methods=["POST"])
def register_admin():
    data = request.json
    result = create_user(data)
    if "error" in result:
        return jsonify({"message": result["error"]}), 400
    return jsonify({"message": "Admin registered successfully"}), 201

@admin_routes.route("/login", methods=["POST"])
def login_admin():
    data = request.json
    user = authenticate_user(data["email"], data["password"])
    if not user or user["role"] != "admin":
        return jsonify({"message": "Invalid credentials or not an admin"}), 401
    return jsonify({"message": "Admin login successful"}), 200

@admin_routes.route("/assignments", methods=["GET"])
def view_assignments():
    admin_email = request.args.get("email")
    assignments = get_assignments_by_admin(admin_email)
    return jsonify(assignments), 200

@admin_routes.route("/assignments/<id>/<action>", methods=["POST"])
def update_assignment(id, action):
    if action not in ["accept", "reject"]:
        return jsonify({"message": "Invalid action"}), 400
    status = "Accepted" if action == "accept" else "Rejected"
    update_assignment_status(ObjectId(id), status)
    return jsonify({"message": f"Assignment {status}"}), 200
