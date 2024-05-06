import pickle

from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler,RobustScaler
from sklearn.preprocessing import OneHotEncoder ,LabelEncoder
from sklearn.compose import ColumnTransformer


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
        bmi = request.form.get("bmi")
        bp_category = request.form.get("bp_category")

        data = {'gender':[gender],
                'height':[height],
                'weight':[weight],
                'ap_hi':[ap_hi],
                'ap_lo':[ap_lo],
                'cholesterol':[cholesterol],
                'gluc':[glucose],
                'smoke':[smoke],
                'alco':[alcohol],
                'active':[active],
                'age_years':[age],
                'bmi':[bmi],
                'bp_category':[bp_category]}
        
        df = pd.DataFrame(data)
        numerical = ['height', 'weight', 'ap_hi', 'ap_lo', 'gluc', 'alco', 'age_years', 'bmi']

        CTE = ColumnTransformer(transformers=[('robsc', RobustScaler(), Numerical),
                                        ('ohe', OneHotEncoder(drop='first', handle_unknown='ignore'), ['bp_category'])
                            ], remainder='passthrough')

        df_transformed = CTE.fit_transform(df)

        pred = model.predict("index.html",data=df.preds)

        if pred==0:
            prediction = 'No disease'
        else:
            prediction='Disease'


    return render_template("index.html", age=age, height=height, weight=weight, ap_hi=ap_hi, ap_lo=ap_lo,
                               gender=gender, cholesterol=cholesterol, glucose=glucose, smoke=smoke,
                               alcohol=alcohol,active=active,bmi=bmi,bp_category=bp_category)



if __name__=='__main__':
    app.run(debug=True)
   
     