#!/usr/bin/env python

# import necessary packages
import os
from flask import Flask

# create flask app
flaskapp = Flask(__name__)

# base route to check if service is running
@flaskapp.route('/')
def alive():
    return "200 OK"
   
# run the app
if __name__ == '__main__':
    flaskapp.run(debug=True, host='0.0.0.0', port = int(os.environ.get('PORT', 8080)))
