from flask import Blueprint, request, jsonify
from config.db import db
from bson import ObjectId

orders_bp = Blueprint("orders", __name__, url_prefix="/orders")

# --- CREATE ORDER ---
@orders_bp.route("/create", methods=["POST"])
def create_order():
    data = request.get_json()
    if not data or "user_id" not in data or "items" not in data:
        return jsonify({"error": "user_id and items required"}), 400

    order = {
        "user_id": data["user_id"],
        "items": data["items"],  # list of {product_id, qty}
        "status": "pending"
    }

    result = db.crochet_orders.insert_one(order)
    return jsonify({"message": "Order created", "order_id": str(result.inserted_id)}), 201

# --- GET USER ORDERS ---
@orders_bp.route("/<user_id>", methods=["GET"])
def get_user_orders(user_id):
    orders = list(db.crochet_orders.find({"user_id": user_id}))
    for o in orders:
        o["_id"] = str(o["_id"])
    return jsonify(orders), 200

# --- UPDATE ORDER STATUS ---
@orders_bp.route("/update/<order_id>", methods=["PUT"])
def update_order(order_id):
    data = request.get_json()
    status = data.get("status")
    if not status:
        return jsonify({"error": "status required"}), 400

    result = db.crochet_orders.update_one(
        {"_id": ObjectId(order_id)},
        {"$set": {"status": status}}
    )
    if result.matched_count == 0:
        return jsonify({"error": "Order not found"}), 404
    return jsonify({"message": "Order updated"}), 200
