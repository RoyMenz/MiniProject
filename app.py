# app.py (top-level file)

from app import create_app  # import factory from app/__init__.py

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)