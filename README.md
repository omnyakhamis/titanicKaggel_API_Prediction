"# TitanicKaggel_InProduction" 
"# titanicKaggel_API_Prediction" 
# Kaggle-titanic

This is a tutorial in an Python file for the Kaggle competition, Titanic Machine Learning From Disaster. The goal of this repository is to provide an example of a competitive analysis for those interested in getting into the field of data analytics or using python for Kaggle's Data Science competitions .

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

1. Download this repository in a zip file by execute this from the terminal:

```
https://github.com/omnyakhamis/titanicKaggel_API_Prediction.git
```

### Installing

A step by step series of examples that tell you how to get a development env running

1. Navigate to the directory where you unzipped or cloned the repo and create a virtual environment with.

```
pipenv shell
```

And repeat

```
pipenv install
```

## Deployment

### Running the run python file

```
python run.py
```
 To create and run a server.

### Installing Postman API development environment
1. Download : https://www.getpostman.com/downloads/
2. Sign in 
3. The API Running on :
    * https://titanicapiomnya.herokuapp.com/ - Welcom message
    *  https://titanicapiomnya.herokuapp.com/health - To be sur the server is running
    *  https://titanicapiomnya.herokuapp.com/train - To create, train and save a model.
    *   https://titanicapiomnya.herokuapp.com/Prediction - To make prediction
    ```
        #Exmaple data to make prediction by using postman
        {"Age": 50,"Pclass": 1, "Fare": 71.2833, "Sex": "male","Name":"Owen Harris","SibSp":0,
        "Parch":0,"Ticket":"PC 17599","Cabin":null,"Embarked":"S"}
        ```
## Built With

* [flask](https://www.fullstackpython.com/flask.html) - The micro web framework written in Python used
* [elephantsql - PostgreSQL as a Service](https://www.elephantsql.com/) - DB Management
* [pgAdmin](https://www.pgadmin.org/) - PostgreSQL Tools
* [getpostman](https://www.getpostman.com/) - API development environment

## Contributing

Please read [CONTRIBUTING.md]() for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **Omnya Khamis** - *Initial work* - [OmnyaKhamis](https://github.com/omnyakhamis)

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
