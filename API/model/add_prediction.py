from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# Init app
app = Flask(__name__)
# basedir = os.path.abspath(os.path.dirname(__file__))
url = 'postgres://xeumkbpo:oVQND5ep22edECWjXRx-zUEGsV09C3KT@raja.db.elephantsql.com:5432/xeumkbpo'
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)


# Product Class/Model
class Predict(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    survived = db.Column(db.Integer)

    def __init__(self, survived):
        self.survived = survived


# Product Schema
class PredictSchema(ma.Schema):
    class Meta:
        fields = ('id', 'survived')


# Init schema
prediction_schema = PredictSchema(strict=True)
predictions_schema = PredictSchema(many=True, strict=True)


# Create a Product
@app.route('/add_prediction', methods=['POST'])
def add_prediction():
    survived = request.json['survived']

    new_prediction = Predict(survived)

    db.session.add(new_prediction)
    db.session.commit()

    return prediction_schema.jsonify(new_prediction)
