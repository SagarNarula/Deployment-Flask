import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
app = Flask(__name__) #Create an instance of Flask
model = pickle.load(open('model1.pkl', 'rb')) #Load our model pickle File

@app.route('/')
def home():
    return render_template('Index.html')
	
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('Index.html', prediction_text='User Weight should be  {} pounds'.format(output))
	
if __name__ == "__main__":
    app.run(debug=True)
