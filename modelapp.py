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
model = joblib.load('fighter_classifier.h5')

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    print(request.form)
    
# fighter1(fighter1):
#     data1 = mongo.db.recent_matches.find({'fighter':fighter1})

# def fighter2(fighter2):
#     data2 = mongo.db.recent_matches.find({'fighter':fighter2})




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
#         
if __name__ == '__main__':
    app.run(debug=True)