import pandas as pd
import os

import pickle
from API.model.pipeline_preparation import prediction_pipeline
from sklearn.model_selection import train_test_split
from API.model.preprocessing import transform
from sqlalchemy import create_engine

train_file = "postgres://xeumkbpo:oVQND5ep22edECWjXRx-zUEGsV09C3KT@raja.db.elephantsql.com:5432/xeumkbpo"
# train_file = os.environ['DATABASE_URL']
test_file = os.path.dirname(os.path.realpath(__file__)) + '/dataset/test.csv'
Model_path = os.path.dirname(os.path.realpath(__file__)) + '/saved_model/model.sav'
engine = create_engine(train_file)


# df = ['Age', 'Cabin', 'Embarked', 'Fare', 'Name', 'Parch', 'Pclass', 'Sex','SibSp', 'Survived', 'Ticket', 'Title', 'FamilySize']


def _save_model(model):  # with _ befor the function name it means that this function is local
    pickle.dump(model, open(Model_path, 'wb'))  # wb -- write the filz in binary


def read_train():
    # load data

    # train = pd.read_csv(train_file)
    train = pd.read_sql("passengers", con=engine)
    test = pd.read_csv(test_file)
    # merge train and test
    df_titanic = train.append(test, ignore_index=True)

    # create indexes to separate data later on
    train_idx = len(train)
    test_idx = len(df_titanic) - len(test)

    df_titanic = transform(df_titanic)

    # create train and test data
    train = df_titanic[:train_idx]
    test = df_titanic[test_idx:]

    # convert Survived back to int
    train.Survived = train.Survived.astype(int)
    # Convert the male and female groups to integer form
    # train.Sex = train.Sex.map({"male": 0, "female": 1})

    X_train = train.drop('Survived', axis=1)
    y_train = train['Survived']

    X_test = test
    y_test = test['Survived']

    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    prediction_pipeline.fit(X_train, y_train)
    _save_model(prediction_pipeline)
    # print(prediction_pipeline.score(X_test, y_test))

    if __name__ == '__main__':  # condition for run this file
        read_train()
