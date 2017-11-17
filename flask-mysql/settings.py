# ----------------------------------------------------------------------------------------------- #
# This is a settings file that will initialize all the database configurations.                   #
#                                                                                                 #
# Code Written: Minh-Quan H. Nguyen                                                               #
# ----------------------------------------------------------------------------------------------- #


# -------------------------------- Define Database Configuration -------------------------------- #
SECRET_KEY = 'password'
DEBUG = True
DB_USERNAME = 'root'
DB_PASSWORD = 'password'
FLASK_DATABASE_NAME = 'my_games'
DB_URI = "mysql://%s:%s@mysql:3306/%s" % (DB_USERNAME, DB_PASSWORD, FLASK_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
