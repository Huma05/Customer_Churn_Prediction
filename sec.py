



model =  pickle.load(open('LogisticRegression.sav','rb'))



@app.route('/predict',methods=['POST'])
def predict():
       input_features = [boolean(x,y) for x,y in request.form.values()]
       features_value = [np.array(input_features)]

features_name = ['Monthly Charges','Payment Methods','Paperless Billing','Multiple Lines','Phone Service',
                  'Senior Citizen','Gender']

data = pd.data(features_value)
output = model.predict(single_pred)

if output == 0:
    res_val = "LOYAL"

else:
   res_val= "NOT LOYAL" 

 return render_template('index.html',prediction_text='Customer is {}'.format(res_val))