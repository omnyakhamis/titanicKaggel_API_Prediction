# the last step -- create the application
from flask import Flask
from .ModelView import prediction_app  # import the route that was create


def create_app():
    server = Flask('Survived_prediction')  # intiat my server
    server.register_blueprint(prediction_app)  # give the route
    return server

    # we create the def create_app(): because we will run from out side the model
