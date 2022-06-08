from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import json
from bson.json_util import dumps
from matplotlib import projections
from zmq import ROUTER
from bson import json_util
from flask_cors import CORS

# Create an instance of Flask
app = Flask(__name__)
CORS(app)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/Project4")


@app.route("/fighters")
def fighters():
    data = mongo.db.fighters.find({},{'_id':False})
    list_cur = list(data)
    
    return jsonify(list_cur[0]["fighter_dropdown"])


if __name__ == '__main__':
    app.run(debug=True)