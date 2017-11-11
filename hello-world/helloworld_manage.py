# ----------------------------------------------------------------------------------------------- #
# This is a simple Flask Web Application that is deployed to your localhost using docker. The app #
# simply shows a message to the world that it is a healthy running application on the web!        #
#                                                                                                 #
# Code Written: Minh-Quan H. Nguyen                                                               #
# ----------------------------------------------------------------------------------------------- #

# ----------------------------------- Import Libraries / File ----------------------------------- #
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_script import Manager, Server
from app import app


# --------------------------------- Initialize Manager for Apps --------------------------------- #
manager = Manager(app)


# ----------------------------------------- Define Host ----------------------------------------- #
manager.add_command("runserver", Server(
    host = '0.0.0.0',
    port = 8080
))


# ----------------------------------- Run the Hello World App ----------------------------------- #
if __name__ == "__main__":
    manager.run()
    