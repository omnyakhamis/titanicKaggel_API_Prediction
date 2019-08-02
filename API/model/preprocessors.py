from sklearn.base import BaseEstimator,TransformerMixin
import pandas as pd
#from sklearn.preprocessing import OneHotEncoder


 # class Replace_nan_numerical_values(BaseEstimator,TransformerMixin):
 #    def __init__(self,features):
 #         self.features = features
 #    def fit(self,X,y):
 #         return self
 #    def transform(self,X):
 #        X = X.copy()
 #        print("i am in function")
 #
 #        # PassengerId can be removed from data for now
 #         X.drop('PassengerId', axis=1, inplace=True)
 #             # create a new feature to extract title names from the Name column
 #         X['Title'] = X['Name'].apply(lambda name: name.split(',')[1].split('.')[0].strip())
 #            # normalize the titles
 #         normalized_titles = {
 #                 "Capt":       "Officer",
 #                 "Col":        "Officer",
 #                 "Major":      "Officer",
 #                 "Jonkheer":   "Royalty",
 #                 "Don":        "Royalty",
 #                 "Sir" :       "Royalty",
 #                 "Dr":         "Officer",
 #                 "Rev":        "Officer",
 #                 "the Countess":"Royalty",
 #                 "Dona":       "Royalty",
 #                 "Mme":        "Mrs",
 #                 "Mlle":       "Miss",
 #                 "Ms":         "Mrs",
 #                 "Mr" :        "Mr",
 #                 "Mrs" :       "Mrs",
 #                 "Miss" :      "Miss",
 #                 "Master" :    "Master",
 #                 "Lady" :      "Royalty"
 #             }
 #             # map the normalized titles to the current titles
 #         X['Title']= X['Title'].map(normalized_titles)
 #
 #         X['Cabin'] = X['Cabin'].fillna(X['Cabin'].mode()[0])
 #         X['Embarked'] = X['Embarked'].fillna(X['Embarked'].mode()[0])
 #         X['Fare'] = X['Fare'].fillna(X['Fare'].mode()[0])
 #         X['Age'] = X['Age'].fillna(X['Age'].mode()[0])
 #         return X

class Select_all_usefull_features (BaseEstimator,TransformerMixin):
    def __init__(self,features):
        self.features = features
    def fit(self,X,y):
        return self
    def transform(self,X):
        X = X.copy()
        X = X[self.features]
        print("Final features",X.columns)
        return X

class Get_Dummies (BaseEstimator, TransformerMixin):
    def fit(self,X,y):
        return self
    def transform(self,X):
        X = X.copy()
        X = pd.get_dummies(X, drop_first=True)
        return X

class Replace_missing_Dummies (BaseEstimator, TransformerMixin):
  def __init__(self, features):
    self.features = features

  def fit(self,X,y):
    return self

  def transform(self,X):
    X = X.copy()
    for feature in self.features:
      if feature not in X.columns:
        X[feature] = [0]*len(X.index)
    return X