import pickle

from flask import Flask, render_template, request

import numpy as np
import pandas as pd


app = Flask(__name__)

model = pickle.load(open('best_tree_classifier.pkl','rb'))

@app.route("/",methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict",methods=['GET'])
def prediction():

    age_user = request.from.get("age")

    return render_template("test.html",age=age_user)




if __name__=='__main__':
    age = Home()
    print('age')
    app.run(debug=True)
     