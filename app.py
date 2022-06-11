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
# mongo = PyMongo(app, uri="mongodb://localhost:27017/project4")
mongo = PyMongo(app, uri="mongodb+srv://mel518:databasepass@TestTrain.ppavz.mongodb.net/Project4?retryWrites=true&w=majority")



# # Use PyMongo to establish Mongo connection
# mongo = PyMongo(app, uri="mongodb://localhost:27017/project4")

@app.route("/")
def home():
    data = mongo.db.Data.find()
    list_cur = list(data)
    json_data = jsonify(json_util.dumps(list_cur))
    return json_data

@app.route("/fighter_stats")
def stats():
    data = mongo.db.fighter_stats.find({}, {'_id': 0})
    list_cur = list(data)
    return jsonify(list_cur)

@app.route("/fighter_stats/<fighter>")
def fighter(player):
    data =mongo.db.fighter_stats.find({'fighter':player},{'date': 0, 'avg_KD': 0, 'win_by_Decision_Majority': 0})
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

@app.route("/combined/<fighter>")
def select(fighter):
    data =mongo.db.Combined_Fighter.find({'fighter':fighter},{'_id': 0,'date': 1,'avg_KD':1,'avg_TOTAL_STatt':1,'avg_TOTAL_STlanded':1})
    list_cur = list(data)
    return jsonify(list_cur)

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