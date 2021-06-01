import numpy as np 
import pandas as pd 
import pickle

from flask import Flask, request, render_template

app=Flask("__name__")
model =  pickle.load(open('LogisticRegression.sav','rb'))

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    input_features = [int(x) for x in request.form.values()]
    features_value = [np.array(input_features)]

    features_name = ["Gender","Senior Citizen","Partner","Dependents","tenure","Phone Service","Multiple Lines","InternetService","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport","StreamingTV","StreamingMovies","Contract","Paperless Billing","Payment Methods","Monthly Charges","TotalCharges"]

    df = pd.DataFrame(features_value,columns=features_name)
    output = model.predict(df)

    if output == 1:
 	    res_val = "LOYAL"

    else:
 	   res_val= "NOT LOYAL" 

    return render_template('index.html',prediction_text='Customer is {}'.format(res_val))  


if __name__=="__main__":
    app.run(debug=True)