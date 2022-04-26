# Forest-Fire-Prediction-Website
A website that predicts the probability of a forest fire taking place based on oxygen,temperature and humidity content
## Instructions for VS Code :
1) In project , make sure that the "forest_html" file is in the templates folder.
2) In the static folder add the css and js file for css js elements to work on webpage.

## Steps to deploy using Flask :
Flask is one of the most popular web application frameworks written in Python.
It is a microframework designed for an easy and quick start.
Extending with tools and libraries adds more functionality to Flask for more complex projects. 

1) Create a virtual environment in python3.9 onto your machine.
2) Install all the required python libraries used in the project into the virtual environment.
3) Initialise the app.py file as a flask app.
4) Run the flask server using the "flask run" command onto the command line.

For more detailed steps on how to run a flask project, refer to the file given below.👇🏻

Once you're done with the setup, a virtual environment needs to be established to deploy the Forest-Fire-Prediction Website using Flask: https://phoenixnap.com/kb/install-flask

## Regarding the model :
The forest fire prediction is applied with the help of Machine Learning Algorithm, Support Vector Machine (forest_fire.py). The data used for traing the model consist of five columns namely,
Area, Oxygen, Tempurature, Humidity and Fire Occurrence. The main purpose is to deploy the ML model uisng Flask, so data has small amount of enteries.
