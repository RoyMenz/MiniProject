from flask_pymongo import PyMongo
from flask import Flask
from pymongo import MongoClient

MONGO_URI = "mongodb+srv://roycreatives28:roy%402005@miniproject.7e8kkje.mongodb.net/"
 
client = MongoClient(MONGO_URI)
db = client["crochet_app"]
