from flask import Flask, request, jsonify
from config.db import db
from bson import ObjectId

app = Flask(__name__)

@app.route('/')
def home():
    return {'message' : 'API is Running !!'}

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)