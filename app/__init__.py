# Global imports
from flask import Flask

# Local imports
from config import app_config


def create_app(config_name):
    """ Create the application factory """

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    

    return app