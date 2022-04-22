#!/usr/bin/env python

# import necessary packages
import os
from flask import Flask
import json
import mysql.connector

# create flask app
flaskapp = Flask(__name__)

# base route to check if service is running
@flaskapp.route('/')
def alive():
    return "I'm alive!"

@flaskapp.route('/customers', methods=['GET'])
def customers():
    conn = mysql.connector.connect(
        host = os.environ.get("DB_HOST"), 
        user = os.environ.get("DB_USER"),
        passwd = os.environ.get("DB_PWD"),
        database = "sample")  

    #retrieving information 
    cur = conn.cursor() 
    cur.execute("SELECT * FROM customer")

    # serialize results into JSON
    row_headers=[x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data=[]
    for result in rv:
         json_data.append(dict(zip(row_headers,result)))
    
    conn.close()
    
    # return the results
    return json.dumps(json_data)

@flaskapp.route('/agents', methods=['GET'])
def agents():
    conn = mysql.connector.connect(
        host = os.environ.get("DB_HOST"), 
        user = os.environ.get("DB_USER"),
        passwd = os.environ.get("DB_PWD"),
        database = "sample")  

    #retrieving information 
    cur = conn.cursor() 
    cur.execute("SELECT * FROM agents")

    # serialize results into JSON
    row_headers=[x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data=[]
    for result in rv:
         json_data.append(dict(zip(row_headers,result)))
    
    conn.close()
    
    # return the results
    return json.dumps(json_data)
   
# run the app
if __name__ == '__main__':
    flaskapp.run(debug=True, host='0.0.0.0', port = int(os.environ.get('PORT', 8080)))