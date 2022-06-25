from flask import Flask, request, jsonify
import json
import os
import pandas as pd
#from flask_sqlSOXalchemy import sqlSOXAlchemy

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

#@app.route('/sample')


def filters_col(num):
    file = open('meta/'+str(num)+'.json')
    
    json_object = json.load(file)
    
    return json_object

