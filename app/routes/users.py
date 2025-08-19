from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from config.db import db

user_bp = Blueprint("user", __name__, url_prefix="/users")

# --- SIGNUP ---
@user_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    if not data or "email" not in data or "password" not in data:
        return jsonify({"error": "Email and password are required"}), 400

    email = data["email"]
    password = data["password"]

    # Check if user already exists
    existing_user = db.crochet_user.find_one({"email": email})
    if existing_user:
        return jsonify({"error": "User already exists"}), 400

    hashed_pw = generate_password_hash(password)

    user = {
        "email": email,
        "password": hashed_pw
    }

    db.crochet_user.insert_one(user)

    return jsonify({"message": "User created successfully"}), 201


# --- LOGIN ---
@user_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data or "email" not in data or "password" not in data:
        return jsonify({"error": "Email and password are required"}), 400

    email = data["email"]
    password = data["password"]

    user = db.crochet_user.find_one({"email": email})

    if not user:
        return jsonify({"error": "User not found"}), 404

    if not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid password"}), 401

    return jsonify({"message": "Login successful", "email": email}), 200


# --- TEST GET USERS ---
@user_bp.route("/", methods=["GET"])
def get_users():
    users = list(db.crochet_user.find({}, {"password": 0}))  # hide password
    for user in users:
        user["_id"] = str(user["_id"])
    return jsonify(users)
