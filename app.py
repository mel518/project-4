from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import json
from bson.json_util import dumps
from matplotlib import projections
#from zmq import ROUTER
from bson import json_util
from flask_cors import CORS
import sys
import numpy as np
import os
import time
from flask import Flask, request, jsonify, render_template
import joblib

# Create an instance of Flask
app = Flask(__name__)
CORS(app)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb+srv://mel518:databasepass@TestTrain.ppavz.mongodb.net/Project4?retryWrites=true&w=majority")
#model = joblib.load('fighter_classifier.h5')

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict',methods=['POST','GET'])
# def predict():

#     int_features = [float(x) for x in request.form.values()]
#     final_features = [np.array(int_features)]
#     prediction = model.predict(final_features)

#     # output = round(prediction[0], 2)
#     if prediction==0:
#         return render_template('index.html',
#                                prediction_text='Low chances of patient readmitted to hospital.'.format(prediction),
#                                )
#     else:
#         return render_template('index.html',
#                                prediction_text='High chances of patient readmitted to hospital'.format(prediction),
#                               )

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

@app.route("/fighter_stats")
def fighter():
    data = mongo.db.fighter_stats.find()
    list_cur = list(data)
    json_data = jsonify(json_util.dumps(list_cur))
    return json_data



if __name__ == '__main__':
    app.run(debug=True)
