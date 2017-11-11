# ----------------------------------------------------------------------------------------------- #
# This is a simple Flask Web Application that is deployed to your localhost using docker. The app #
# simply shows a message to the world that it is a healthy running application on the web!        #
#                                                                                                 #
# Code Written: Minh-Quan H. Nguyen                                                               #
# ----------------------------------------------------------------------------------------------- #


# ----------------------------------- Import Libraries / File ----------------------------------- #
from flask import Flask


# --------------------------------------- Initialize App. --------------------------------------- #
app = Flask(__name__)


# --------------------------------------- Import Settings --------------------------------------- #
'''
Use the following code to import your settings that is written in Python.

app.config.from_object('<your python setting file here>')
'''


# ------------------------------------- Initialize Database ------------------------------------- #
'''
Simply initialize a MySQL Database with Flask by using the code below. This will utilize the
SQLAlchemy Library from Flask.

db = SQLAlchemy(app) 
'''


# -------------------------------- Import Application Controller -------------------------------- #
from helloworld_web_app import helloworld_controller
