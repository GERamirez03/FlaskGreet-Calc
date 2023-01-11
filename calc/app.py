from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/add')
def add_q_params():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(add(a,b))

@app.route('/sub')
def subtract_q_params():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(sub(a,b))

@app.route('/mult')
def multiply_q_params():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(mult(a,b))

@app.route('/div')
def divide_q_params():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(div(a,b))