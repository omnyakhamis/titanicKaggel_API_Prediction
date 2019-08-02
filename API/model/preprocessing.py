
def transform(X):
      
    print("i am in function")

        # PassengerId can be removed from data for now
    X.drop('PassengerId', axis=1, inplace=True)
        # create a new feature to extract title names from the Name column
    X['Title'] = X['Name'].apply(lambda name: name.split(',')[1].split('.')[0].strip())
        # normalize the titles
    normalized_titles = {
            "Capt":       "Officer",
            "Col":        "Officer",
            "Major":      "Officer",
            "Jonkheer":   "Royalty",
            "Don":        "Royalty",
            "Sir" :       "Royalty",
            "Dr":         "Officer",
            "Rev":        "Officer",
            "the Countess":"Royalty",
            "Dona":       "Royalty",
            "Mme":        "Mrs",
            "Mlle":       "Miss",
            "Ms":         "Mrs",
            "Mr" :        "Mr",
            "Mrs" :       "Mrs",
            "Miss" :      "Miss",
            "Master" :    "Master",
            "Lady" :      "Royalty"
        }
        # map the normalized titles to the current titles
    X['Title']= X['Title'].map(normalized_titles)

    X['Cabin'] = X['Cabin'].fillna(X['Cabin'].mode()[0])
    X['Embarked'] = X['Embarked'].fillna(X['Embarked'].mode()[0])
    X['Fare'] = X['Fare'].fillna(X['Fare'].mode()[0])
    X['Age'] = X['Age'].fillna(X['Age'].mode()[0])
    return X