#!/usr/bin/python

#sudo apt-get install python3-venv
#$ mkdir flaskexample
#cd flaskexample
#$ python3 -m venv venv
#source venv/bin/activate
#$ venv\Scripts\activate
#You should see: (venv) ➜  flaskexample 
#sudo apt install python3-flask
#pip install flask
# (venv) ➜  flaskexample python3
#>>> import flask
#>>>
#export FLASK_APP=hello
#export FLASK_DEBUG=1
#flask run


***code***
**********


from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return 'Web App with Python Flask!'

app.run(host='0.0.0.0', port=81)
