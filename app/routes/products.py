from flask import Blueprint, request, jsonify
from config.db import db
from bson import ObjectId

products_bp = Blueprint("products", __name__, url_prefix="/products")

@products_bp.route("/", methods=["GET"])
def get_products():
    products = list(db.products.find())
    for product in products:
        product["_id"] = str(product["_id"])
    return jsonify(products)

@products_bp.route("/", methods=["POST"])
def add_product():
    data = request.json
    new_product = {
        "name": data["name"],
        "price": data["price"]
    }
    db.products.insert_one(new_product)
    new_product["_id"] = str(new_product["_id"])
    return jsonify(new_product), 201
