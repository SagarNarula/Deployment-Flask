# Deployment-Flask

ML-Model-Flask-Deployment
This is a demo project to elaborate how Machine Learn Models are deployed on production using Flask API

Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

Project Structure

Weight-Height.ipynb - This contains code fot our Machine Learning model to predict user weight based on training data in 'weight-height.csv' file.
app.py - This contains Flask APIs that receives the details through GUI or API calls, computes the precited value based on our model and returns it.
templates - This folder contains the HTML template to allow user to enter detail and displays the predicted user weight.
Running the project
Run app.py using below command to start Flask API
python app.py
By default, flask will run on port 5000.

