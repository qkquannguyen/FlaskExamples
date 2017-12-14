# ----------------------------------------------------------------------------------------------- #
# This is a simple Flask Web Application that is deployed to your localhost using docker. The app #
# will show you the contents of your MySQL Database built with a Docker Container.                #
#                                                                                                 #
# The purpose of this app is to show how you are able to connect to a database using Flask and    #
# display its contents.                                                                           #
#                                                                                                 #
# Code Written: Minh-Quan H. Nguyen                                                               #
# ----------------------------------------------------------------------------------------------- #


# ----------------------------------- Import Libraries / File ----------------------------------- #
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# --------------------------------------- Initialize App. --------------------------------------- #
app = Flask(__name__)

 
# --------------------------------------- Import Settings --------------------------------------- #
'''
Use the following code to import your settings that is written in Python.

    app.config.from_object('<your python setting file here>')
'''
app.config.from_object('settings')


# ------------------------------------- Initialize Database ------------------------------------- #
'''
Simply initialize a MySQL Database with Flask by using the code below. This will utilize the
SQLAlchemy Library from Flask.
'''
db = SQLAlchemy(app)


# -------------------------------- Import Application Controller -------------------------------- #
from flask_mysql_app import flask_controller