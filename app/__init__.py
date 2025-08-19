from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    # Register blueprints
    from app.routes.users import user_bp
    from app.routes.admin import admin_bp
    from app.routes.cart import cart_bp
    from app.routes.orders import orders_bp

    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(cart_bp, url_prefix='/cart')
    app.register_blueprint(orders_bp, url_prefix='/orders')

    # Root route (just for testing)
    @app.route("/")
    def home():
        return jsonify({"message": "API is working! 🚀"})

    return app
