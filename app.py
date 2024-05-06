import pickle

from flask import Flask, render_template, request

import numpy as np
import pandas as pd


app = Flask(__name__)

model = pickle.load(open('best_tree_classifier.pkl','rb'))

@app.route("/",methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def prediction():
    if request.method == 'POST':
        age = request.form.get("age")
        height = request.form.get("height")
        weight = request.form.get("weight")
        ap_hi = request.form.get("ap_hi")
        ap_lo = request.form.get("ap_lo")
        gender = request.form.get("gender")
        cholesterol = request.form.get("cholesterol")
        glucose = request.form.get("Glucose")
        smoke = request.form.get("Smoke")
        alcohol = request.form.get("Alcohol")
        active = request.form.get("Actve")

    return render_template("index.html", age=age, height=height, weight=weight, ap_hi=ap_hi, ap_lo=ap_lo,
                               gender=gender, cholesterol=cholesterol, glucose=glucose, smoke=smoke,
                               alcohol=alcohol,active=active)



if __name__=='__main__':
    app.run(debug=True)
   
     