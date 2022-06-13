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
import pandas as pd
import os
import time
from flask import Flask, request, jsonify, render_template
import joblib
from sklearn.metrics import accuracy_score

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
    print(request.form.values())
    fighter1 = mongo.db.recent_matches.find({'fighter':request.form.values[0]})
    fighter2 = mongo.db.recent_matches.find({'fighter':request.form.values[1]})
    df1 = pd.DataFrame(fighter1)
    df2 = pd.DataFrame(fighter2)
    df1.drop(columns = 'fighter', inplace = True)
    df2.drop(columns = 'fighter', inplace = True)
    df1.append(df2)
    df1_formodel = pd.get_dummies(df1)

    prediction = model.predict(df1_formodel)
    accuracy = model.score(df1_formodel)

    if prediction==0:
        return render_template('index.html',prediction_text='Fighter 1 Wins'.format(accuracy))
    else:
       return render_template('index.html',prediction_text='Fighter 2 Wins'.format(accuracy))

predict()




# @app.route('/predict',methods=['POST','GET'])
# def predict():

#     int_features = [float(x) for x in request.form.values()]
#     final_features = [np.array(int_features)]
#     
#         
if __name__ == '__main__':
    app.run(debug=True)