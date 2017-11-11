# ----------------------------------------------------------------------------------------------- #
# This is a simple Flask Web Application that is deployed to your localhost using docker. The app #
# simply shows a message to the world that it is a healthy running application on the web!        #
#                                                                                                 #
# Code Written: Minh-Quan H. Nguyen                                                               #
# ----------------------------------------------------------------------------------------------- #

# ----------------------------------- Import Libraries / File ----------------------------------- #
import logging

from app import app
from flask import Flask, request


# -------------------------------------- Set the Log Level -------------------------------------- #
logging.getLogger().setLevel(logging.DEBUG)


# --------------------------------------- Routing to App. --------------------------------------- #

''' ---- Initialize Hello-World Endpoint ---- '''
@app.route('/')
@app.route('/hello')
def helloworld_endpoint():

    # Hello World Message
    helloMessage = "Hello World, this is my Hello-World Flask Example!\n" \
                   "Please enjoy this message as long as you want!"
    
    # Log a healthy status code
    logging.debug("HTTP Code 200 - Routing Success!")

    # Return the Hello World Message
    return helloMessage