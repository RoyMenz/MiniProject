from flask import Blueprint, request, jsonify
from config.db import db
from bson import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

user_bp = Blueprint('user', __name__, url_prefix='/users')

# Get all users
@user_bp.route('/', methods=['GET'])
def get_users():
    users = list(db.crochet_user.find())
    for user in users:
        user['_id'] = str(user['_id'])
    return jsonify(users)

# Signup user
@user_bp.route('/signup', methods=['POST'])
def signup_user():
    data = request.json
    hashed_password = generate_password_hash(data['password'])
    db.crochet_user.insert_one({
        "name": data['name'],
        "email": data['email'],
        "password": hashed_password
    })
    return jsonify({"message": "User created"}), 201

# Login user
@user_bp.route('/login', methods=['POST'])
def login_user():
    data = request.json
    user = db.crochet_user.find_one({"email": data["email"]})
    if user and check_password_hash(user['password'], data['password']):
        return jsonify({"message": "Login successful!"})
    return jsonify({"error": "Invalid credentials"}), 401
