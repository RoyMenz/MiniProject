from flask import Flask
from config.db import db

def create_app():
    app = Flask(__name__)

    from app.routes.products import products_bp
    from app.routes.users import user_bp

    app.register_blueprint(products_bp)
    app.register_blueprint(user_bp)

    return app
