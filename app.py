from flask import Flask
from config.db import init_db
from app.routes.auth import auth_bp

def create_app():
    app = Flask(__name__)
    init_db(app)
    app.register_blueprint(auth_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
