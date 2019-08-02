# Create the Route
from flask import Blueprint, request, jsonify
from .model.prediction import make_prediction
from API.model.run_pipeline import read_train
import pandas as pd
from sqlalchemy import create_engine
import os


def check_input(req_data):
    cols_list = ['Age', 'Pclass', 'Fare', 'Sex', 'Name', 'SibSp', 'Parch', 'Ticket', 'Cabin', 'Embarked']
    key_list = []
    for key in req_data:
        key_list.append(key)
        # print (key_list)
    if set(cols_list) != set(key_list):
        req_state = "false"
        return req_state


# create route for prediction
prediction_app = Blueprint('/Prediction', __name__)


@prediction_app.route('/', methods=['GET'])
def hello():
    return "Hello"


@prediction_app.route('/Prediction', methods=['POST'])
def predict():
    req_data = request.get_json()
    req_state = check_input(req_data)
    if req_state != "false":
        age = request.json['Age']
        pclass = request.json['Pclass']
        fare = request.json['Fare']
        sex = request.json['Sex']
        name = request.json['Name']
        parch = request.json['Parch']
        sibSp = request.json['SibSp']
        ticket = request.json['Ticket']
        cabin = request.json['Cabin']
        embarked = request.json['Embarked']

        prediction = make_prediction(req_data).tolist()
        prediction_copy = prediction
        to_file = pd.DataFrame({'Age': age,
                                'Pclass': pclass,
                                'Fare': fare,
                                'Sex': sex,
                                'Name': name,
                                'Parch': parch,
                                'SibSp': sibSp,
                                'Ticket': ticket,
                                'Cabin': cabin,
                                'Embarked': embarked,
                                'Survived_prediction': prediction_copy,
                                })

        url = os.environ['DATABASE_URL']

        engine = create_engine(url)
        to_file.to_sql("predicted_data", con=engine, if_exists='append')

        return jsonify({'success': True, 'prediction': prediction})
    else:
        return jsonify({'success': False, 'prediction': "Data are NOT completed"})


# create route for get request
@prediction_app.route('/health', methods=['GET'])
def check_health():
    return "Server running"


# create route for get request-train model
@prediction_app.route('/train', methods=['GET'])
def train():
    read_train()
    return "model is saved"
