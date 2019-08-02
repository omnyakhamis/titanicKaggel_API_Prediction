from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from API.model.preprocessors import Get_Dummies
from API.model.preprocessors import Select_all_usefull_features
from sklearn.linear_model import LogisticRegression
from API.model.preprocessors import Replace_missing_Dummies


numerical_features = ['Age', 'Fare', 'Pclass']
categorical_data = ['Sex']

features = numerical_features


prediction_pipeline = Pipeline([
    ('X dummies',Get_Dummies()),
    ('replace all missing dummies', Replace_missing_Dummies(categorical_data)),
    ('X preprocessing',Select_all_usefull_features(features)),
    ('model_dreation',LogisticRegression())
    ])