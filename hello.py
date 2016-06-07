#!/usr/bin/python

###################################################################
#
#   This is a "Hello World!" Python script
#
#
#
###################################################################



from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'