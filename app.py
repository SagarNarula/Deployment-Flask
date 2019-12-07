import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
app = Flask(__name__) #Create an instance of Flask
model = pickle.load(open('model1.pkl', 'rb')) #Load our model pickle File

@app.route('/')
def home():
    return render_template('Index.html')
	
#app.route('/predict',methods=['POST'])
# prediction function \
"""
def ValuePredictor(to_predict_list): 
    to_predict = np.array(to_predict_list).reshape(1, 2) 
    loaded_model = pickle.load(open("model.pkl", "rb")) 
    result = loaded_model.predict(to_predict) 
    #output=round(result[0],2)
    return result[0]
  
@app.route('/predict',methods = ['POST']) 
def predict(): 
    if request.method == 'POST': 
        to_predict_list = request.form.to_dict() 
        to_predict_list = list(to_predict_list.values()) 
        to_predict_list = list(map(int, to_predict_list)) 
        result = ValuePredictor(to_predict_list)
        output=round(int(result[0]),2)
	    return render_template("Index.html",prediction=Output)
	"""
	
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('Index.html', prediction_text='Employee Weight should be  {} pounds'.format(output))
	
if __name__ == "__main__":
    app.run(debug=True)