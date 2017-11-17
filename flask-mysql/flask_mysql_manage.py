# ----------------------------------------------------------------------------------------------- #
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
    port = 5000
))


# ----------------------------------------- Run the App ----------------------------------------- #
if __name__ == "__main__":
    manager.run()
    