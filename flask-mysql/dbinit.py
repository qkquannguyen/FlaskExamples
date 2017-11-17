# ----------------------------------------------------------------------------------------------- #
# This is the Python file that will create and initialize our MySQL Database for our Application  #
#                                                                                                 #
# Code Written: Minh-Quan H. Nguyen                                                               #
# ----------------------------------------------------------------------------------------------- #


# ----------------------------------- Import Libraries / File ----------------------------------- #
from app import db
from flask_mysql_app.flask_repository import *


# ------------------------------------- Create the Database ------------------------------------- #
db.create_all()