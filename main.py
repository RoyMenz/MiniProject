from flask import Flask
from config.db import db
from app.routes.user import user_bp  # Import the blueprint

app = Flask(__name__)

@app.route('/')
def home():
    return {'message': 'API is Running !!'}

# Register the user blueprint
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
