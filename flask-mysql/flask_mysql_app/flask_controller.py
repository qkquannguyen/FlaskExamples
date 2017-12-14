# ----------------------------------------------------------------------------------------------- #
# This file will route the traffic at various endpoint to display different types of messages.    #
# Querying the data from MySQL will also happen here and other nifty things!                      #
#                                                                                                 #
# Code Written: Minh-Quan H. Nguyen                                                               #
# ----------------------------------------------------------------------------------------------- #


# ----------------------------------- Import Libraries / File ----------------------------------- #
from app import app, db
from flask_mysql_app.flask_repository import *
from flask import Flask, request
from flask import jsonify


# ------------------------------------- MySQL Testing Route ------------------------------------- #
'''
HTML Method:    GET
Endpoint:       "/test-my-database"
Return:         A successful message / code that you connected to the database successfully
Purpose:        To ensure that the database is properly connected
'''
@app.route('/test-my-database')
def mysql_database_test():

    try:
        jsonify(json_list=[i.serialize for i in FlaskModel.query.all()])
        return jsonify({'Database Connection' : 'Good'}), 200
    except Exception:
        return jsonify({'Database Connection' : 'Bad - Check Database Config.'}), 501

# ------------------------------------ JSONIFY Testing Route ------------------------------------ #
'''
HTML Method:    GET
Endpoint:       "/jsonify-test"
Return:         A successful message in JSON
Purpose:        To test JSONIFY and see if it is working properly
'''
@app.route('/jsonify-test')
def jsonify_test():
    
    # Return a successful message in JSON
    try:
        return jsonify(success=True), 200
    
    except Exception:
        return "Unable to successfully call JSONIFY. " \
               "Please make sure you included the JSONIFY Library.", 501


# -------------------------- Welcome to My Flask Web Application Route -------------------------- #
'''
HTML Method:    GET
Endpoint 1:     "/"
Endpoint 2:     "/home"
Return:         A welcome message to the user that they have successfully connected to the app
Purpose:        No particular purpose other than a pretty printing endpoint
'''
@app.route('/')
@app.route('/home')
def home_page():
    
    try:
        return "Welcome to my Flask Application! " \
               "Enjoy this message as long as you like!", 200
    except Exception:
        return "Unable to load the page. HTML Error 404.", 404


# ---------------------------------- Display all Data in MySQL ---------------------------------- #
'''
HTML Method:    GET
Endpoint:       "/show-me-the-goods"
Return:         All the data stored in the database 
Purpose:        To show users what is in the database
'''
@app.route('/show-me-the-goods')
def data_page():
    
    try:
        return(jsonify(flask_db=[i.serialize for i in FlaskModel.query.all()])), 200
    except Exception:
        return "Unable to display the data. " \
               "Check the database configurations and connection.", 501