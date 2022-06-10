from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import json
from bson.json_util import dumps
from matplotlib import projections
#from zmq import ROUTER
from bson import json_util
from flask_cors import CORS


# Create an instance of Flask
app = Flask(__name__)
CORS(app)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="https://ufcmatchdata.herokuapp.com")

# # Use PyMongo to establish Mongo connection
# mongo = PyMongo(app, uri="mongodb://localhost:27017/project4")

@app.route("/")
def home():
    data = mongo.db.stats.find()
    list_cur = list(data)
    json_data = jsonify(json_util.dumps(list_cur))
    return json_data

@app.route("/fighter")
def select():
    data = mongo.db.stats.find()
    list_cur = list(data)
    return jsonify(list_cur)

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



if __name__ == '__main__':
    app.run(debug=True)




# from flask import Flask, render_template, redirect, jsonify
# from flask_pymongo import PyMongo
# import json
# from bson.json_util import dumps
# from matplotlib import projections
# from zmq import ROUTER
# from bson import json_util
# from flask_cors import CORS

# # Create an instance of Flask
# app = Flask(__name__)
# CORS(app)

# # Use PyMongo to establish Mongo connection
# mongo = PyMongo(app, uri="mongodb://localhost:27017/Project4")


# @app.route("/fighters")
# def fighters():
#     data = mongo.db.fighters.find({},{'_id':False})
#     list_cur = list(data)
    
#     return jsonify(list_cur[0]["fighter_dropdown"])


# if __name__ == '__main__':
#     app.run(debug=True)