# ----------------------------------------------------------------------------------------------- #
# This file will initialize the data in the MySQL DB as variables for this app to process. This   #
# file will handle the initialization of the variables and serializes the data so it can be shown #
# in a JSON format.                                                                               #
#                                                                                                 #
# Code Written: Minh-Quan H. Nguyen                                                               #
# ----------------------------------------------------------------------------------------------- #


# ----------------------------------- Import Libraries / File ----------------------------------- #
from app import db
import simplejson as json


# --------------------------- Initialize Class Model for the Database --------------------------- #
class FlaskModel(db.Model):

    # Initialize database columns attributes and the data type of the data in the database
    db_index = db.Column(db.Integer, primary_key = True)
    stock_ticker = db.Column(db.VARCHAR(32))
    stock_description = db.Column(db.VARCHAR(128))
    current_holding = db.Column(db.DECIMAL(10, 3))
    current_stock_price = db.Column(db.DECIMAL(10, 2))
    entry_stock_price = db.Column(db.DECIMAL(10, 2))

    # Constructor for the Data
    def __init__(self, db_index, stock_ticker, stock_description, current_holding,
                 current_stock_price, entry_stock_price):
        self.db_index = db_index
        self.stock_ticker = stock_ticker
        self.stock_description = stock_description
        self.current_holding = current_holding
        self.current_stock_price = current_stock_price
        self.entry_stock_price = entry_stock_price
        pass


    # Serialization of the Data for JSON
    @property
    def serialize(self):
        return {
            'Stock'             :   self.stock_ticker,
            'Stock Description' :   self.stock_description,
            'Stock Holdings'    :   self.current_holding,
            'Current Price'     :   self.current_stock_price,
            'Entry Price'       :   self.entry_stock_price
        }