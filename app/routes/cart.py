from flask import Blueprint, request, jsonify
from config.db import db
from bson import ObjectId

cart_bp = Blueprint("cart", __name__, url_prefix="/cart")

# --- ADD ITEM TO CART ---
@cart_bp.route("/add", methods=["POST"])
def add_to_cart():
    data = request.get_json()
    if not data or "user_id" not in data or "product_id" not in data:
        return jsonify({"error": "user_id and product_id required"}), 400

    cart_item = {
        "user_id": data["user_id"],
        "product_id": data["product_id"],
        "quantity": data.get("quantity", 1)
    }
    db.crochet_cart.insert_one(cart_item)

    return jsonify({"message": "Item added to cart"}), 201

# --- VIEW USER CART ---
@cart_bp.route("/<user_id>", methods=["GET"])
def view_cart(user_id):
    cart = list(db.crochet_cart.find({"user_id": user_id}))
    for c in cart:
        c["_id"] = str(c["_id"])
    return jsonify(cart), 200

# --- REMOVE ITEM FROM CART ---
@cart_bp.route("/remove/<item_id>", methods=["DELETE"])
def remove_from_cart(item_id):
    result = db.crochet_cart.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count == 0:
        return jsonify({"error": "Item not found"}), 404
    return jsonify({"message": "Item removed"}), 200
