from flask import Flask
from flask_cors import CORS
from config.db import init_db

def create_app():
    app = Flask(__name__)

    # Load config
    app.config.from_object("config.settings")

    # Enable CORS
    CORS(app)

    # Initialize MongoDB
    init_db(app)

    # Register blueprints
    from app.routes.auth import auth_bp
    from app.routes.products import products_bp
    from app.routes.cart import cart_bp
    from app.routes.orders import orders_bp
    from app.routes.users import users_bp
    from app.routes.admin import admin_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(products_bp, url_prefix="/products")
    app.register_blueprint(cart_bp, url_prefix="/cart")
    app.register_blueprint(orders_bp, url_prefix="/orders")
    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(admin_bp, url_prefix="/admin")

    return app
