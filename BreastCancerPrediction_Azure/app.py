
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from flask import Flask, request, render_template
import pickle
import os

app = Flask("__name__")



q = ""

@app.route("/")
def loadPage():
	return render_template('home.html', query="")


@app.route("/predict", methods=['POST'])
def predict():

    inputQuery1 = request.form['query1']
    inputQuery2 = request.form['query2']
    inputQuery3 = request.form['query3']
    inputQuery4 = request.form['query4']

    model = pickle.load(open("modelBreastCancer.sav", "rb"))


    data = [[inputQuery1, inputQuery2, inputQuery3, inputQuery4]]
    new_df = pd.DataFrame(data, columns = ['radius_mean', 'perimeter_mean', 'area_mean', 'concave points_mean'])

    single = model.predict(new_df)
    probablity = model.predict_proba(new_df)[:,1]

    if single==1:
        o1 = "le patient a été diagnostiqué comme ayant un cancer du sein."
    else:
        o1 = "le patient n'a pas été diagnostiqué comme ayant un cancer du sein."

    return render_template('home.html', output1=o1, query1 = request.form['query1'], query2 = request.form['query2'],query3 = request.form['query3'],query4 = request.form['query4'])

if __name__ == "__main__":
    app.run()
