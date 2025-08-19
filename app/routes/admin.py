from flask import Blueprint, request, jsonify
from config.db import db

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

# --- GET ALL USERS ---
@admin_bp.route("/users", methods=["GET"])
def get_all_users():
    users = list(db.crochet_user.find({}, {"password": 0}))
    for u in users:
        u["_id"] = str(u["_id"])
    return jsonify(users), 200

# --- GET ALL ORDERS ---
@admin_bp.route("/orders", methods=["GET"])
def get_all_orders():
    orders = list(db.crochet_orders.find())
    for o in orders:
        o["_id"] = str(o["_id"])
    return jsonify(orders), 200

# --- DELETE USER ---
@admin_bp.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    result = db.crochet_user.delete_one({"_id": user_id})
    if result.deleted_count == 0:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted"}), 200
