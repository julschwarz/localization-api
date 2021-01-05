#from gtsam_optimization import *
from flask import Flask, Response, request, flash, url_for, jsonify
from flask import Flask
import redis
import numpy as np
import matplotlib.pyplot as plt


app = Flask(__name__)

@app.route('/')
def hello_world():
    print("works")
    return "This API is running perfectly!"


@app.route('/about')
def about():
    return 'The about page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        print(data["data"])
        return "do_the_login()"
    else:
        return "show_the_login_form()"


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 80.
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)