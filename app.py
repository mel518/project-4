from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import json
from bson.json_util import dumps
from matplotlib import projections
#from zmq import ROUTER
from bson import json_util
from flask_cors import CORS
import sys
import simplejson



# Create an instance of Flask
app = Flask(__name__)
CORS(app)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb+srv://mel518:databasepass@TestTrain.ppavz.mongodb.net/Project4?retryWrites=true&w=majority")

@app.route("/")
def home():
    data = mongo.db.Data.find()
    list_cur = list(data)
    json_data = jsonify(json_util.dumps(list_cur))
    return json_data

@app.route("/fighters")
def fighters():
    data = mongo.db.fighters.find({},{'_id':False})
    list_cur = list(data)
    
    return jsonify(list_cur[0]["fighter_dropdown"])

@app.route("/combined")
def combined():
    data = mongo.db.Combined_Fighter.find()
    list_cur = list(data)
    json_data = jsonify(json_util.dumps(list_cur))
    return json_data


@app.route("/combined/<fighter>")
def select(fighter):
    data =mongo.db.Combined_Fighter.find({'fighter':fighter},{'_id': 0,'date': 1,'avg_KD':1,'avg_TOTAL_STatt':1,'avg_TOTAL_STlanded':1})
    list_cur = list(data)
    return simplejson.dumps(list_cur, ignore_nan=True)


if __name__ == '__main__':
    app.run(debug=True)


 # Successfully installed simplejson-3.17.6