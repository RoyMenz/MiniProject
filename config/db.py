from flask_pymongo import PyMongo
from flask import Flask

mongo = PyMongo()

def init_db(app: Flask):
    app.config["MONGO_URI"] = "mongodb+srv://roycreatives28:roy%402005@miniproject.7e8kkje.mongodb.net/crochet_app"
    mongo.init_app(app)
