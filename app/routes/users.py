from flask import Blueprint, request, jsonify
from config.db import db
from werkzeug.security import generate_password_hash
from bson import ObjectId

user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No input data provided"}), 400

        username = data.get("username") or data.get("name")  # accepts both
        email = data.get("email")
        password = data.get("password")

        if not username or not email or not password:
            return jsonify({"error": "Missing required fields"}), 400

        # Check if email already exists
        existing_user = db.crochet_user.find_one({"email": email})
        if existing_user:
            return jsonify({"error": "User already exists"}), 400

        # Hash password
        hashed_pw = generate_password_hash(password)

        # Insert into MongoDB
        new_user = {
            "username": username,
            "email": email,
            "password": hashed_pw
        }
        result = db.crochet_user.insert_one(new_user)

        return jsonify({
            "message": "User created successfully",
            "user_id": str(result.inserted_id)
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
