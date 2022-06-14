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
    
@app.route('/predict', methods =['POST'])
def predict():
    data = request.get_json() 
    fighter1_name = data.get("fighter1")
    fighter2_name = data.get("fighter2")

    print(data)


    fighter1 = mongo.db.recent_matches.find({'fighter':fighter1_name})
    fighter2 = mongo.db.recent_matches.find({'fighter':fighter2_name})
    
    df1 = pd.DataFrame(fighter1)
    df2 = pd.DataFrame(fighter2)
    df1.drop(columns = ['fighter', '_id'], inplace = True)
    df2.drop(columns = ['fighter', '_id'], inplace = True)
    model_data = pd.concat([df1,df2], axis = 1)
    columns = ['B_avg_KD', 'B_avg_opp_KD', 'B_avg_SIG_STR_pct', 'B_avg_opp_SIG_STR_pct', 'B_avg_TD_pct', 'B_avg_opp_TD_pct', 'B_avg_SUB_ATT', 'B_avg_opp_SUB_ATT', 'B_avg_REV', 'B_avg_opp_REV', 'B_avg_SIG_STR_att', 'B_avg_SIG_STR_landed', 'B_avg_opp_SIG_STR_att', 'B_avg_opp_SIG_STR_landed', 'B_avg_TOTAL_STR_att', 'B_avg_TOTAL_STR_landed', 'B_avg_opp_TOTAL_STR_att', 'B_avg_opp_TOTAL_STR_landed', 'B_avg_TD_att', 'B_avg_TD_landed', 'B_avg_opp_TD_att', 'B_avg_opp_TD_landed', 'B_avg_HEAD_att', 'B_avg_HEAD_landed', 'B_avg_opp_HEAD_att', 'B_avg_opp_HEAD_landed', 'B_avg_BODY_att', 'B_avg_BODY_landed', 'B_avg_opp_BODY_att', 'B_avg_opp_BODY_landed', 'B_avg_LEG_att', 'B_avg_LEG_landed', 'B_avg_opp_LEG_att', 'B_avg_opp_LEG_landed', 'B_avg_DISTANCE_att', 'B_avg_DISTANCE_landed', 'B_avg_opp_DISTANCE_att', 'B_avg_opp_DISTANCE_landed', 'B_avg_CLINCH_att', 'B_avg_CLINCH_landed', 'B_avg_opp_CLINCH_att', 'B_avg_opp_CLINCH_landed', 'B_avg_GROUND_att', 'B_avg_GROUND_landed', 'B_avg_opp_GROUND_att', 'B_avg_opp_GROUND_landed', 'B_avg_CTRL_time(seconds)', 'B_avg_opp_CTRL_time(seconds)', 'B_total_time_fought(seconds)', 'B_total_rounds_fought', 'B_total_title_bouts', 'B_current_win_streak', 'B_current_lose_streak', 'B_longest_win_streak', 'B_wins', 'B_losses', 'B_draw', 'B_win_by_Decision_Majority', 'B_win_by_Decision_Split', 'B_win_by_Decision_Unanimous', 'B_win_by_KO/TKO', 'B_win_by_Submission', 'B_win_by_TKO_Doctor_Stoppage', 'B_Stance', 'B_Height_cms', 'B_Reach_cms', 'B_Weight_lbs', 'R_avg_KD', 'R_avg_opp_KD', 'R_avg_SIG_STR_pct', 'R_avg_opp_SIG_STR_pct', 'R_avg_TD_pct', 'R_avg_opp_TD_pct', 'R_avg_SUB_ATT', 'R_avg_opp_SUB_ATT', 'R_avg_REV', 'R_avg_opp_REV', 'R_avg_SIG_STR_att', 'R_avg_SIG_STR_landed', 'R_avg_opp_SIG_STR_att', 'R_avg_opp_SIG_STR_landed', 'R_avg_TOTAL_STR_att', 'R_avg_TOTAL_STR_landed', 'R_avg_opp_TOTAL_STR_att', 'R_avg_opp_TOTAL_STR_landed', 'R_avg_TD_att', 'R_avg_TD_landed', 'R_avg_opp_TD_att', 'R_avg_opp_TD_landed', 'R_avg_HEAD_att', 'R_avg_HEAD_landed', 'R_avg_opp_HEAD_att', 'R_avg_opp_HEAD_landed', 'R_avg_BODY_att', 'R_avg_BODY_landed', 'R_avg_opp_BODY_att', 'R_avg_opp_BODY_landed', 'R_avg_LEG_att', 'R_avg_LEG_landed', 'R_avg_opp_LEG_att', 'R_avg_opp_LEG_landed', 'R_avg_DISTANCE_att', 'R_avg_DISTANCE_landed', 'R_avg_opp_DISTANCE_att', 'R_avg_opp_DISTANCE_landed', 'R_avg_CLINCH_att', 'R_avg_CLINCH_landed', 'R_avg_opp_CLINCH_att', 'R_avg_opp_CLINCH_landed', 'R_avg_GROUND_att', 'R_avg_GROUND_landed', 'R_avg_opp_GROUND_att', 'R_avg_opp_GROUND_landed', 'R_avg_CTRL_time(seconds)', 'R_avg_opp_CTRL_time(seconds)', 'R_total_time_fought(seconds)', 'R_total_rounds_fought', 'R_total_title_bouts', 'R_current_win_streak', 'R_current_lose_streak', 'R_longest_win_streak', 'R_wins', 'R_losses', 'R_draw', 'R_win_by_Decision_Majority', 'R_win_by_Decision_Split', 'R_win_by_Decision_Unanimous', 'R_win_by_KO/TKO', 'R_win_by_Submission', 'R_win_by_TKO_Doctor_Stoppage', 'R_Stance', 'R_Height_cms', 'R_Reach_cms', 'R_Weight_lbs']
    model_data.columns = columns

    prediction = model.predict(model_data)
    accuracy = model.score(model_data)
    
    return jsonify({"prediction":prediction, "accuracy": accuracy})


# @app.route('/predict',methods=['POST','GET'])
# def predict():

#     int_features = [float(x) for x in request.form.values()]
#     final_features = [np.array(int_features)]
#     
#         
if __name__ == '__main__':
    app.run(debug=True)