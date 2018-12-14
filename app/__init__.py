import os

# Global imports
from flask import Flask
from app.config import app_config
from dotenv import load_dotenv


def create_app(config_name):
    """ Create the application factory """

    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
    dotenv_path = os.path.join(APP_ROOT, '.env')
    load_dotenv(dotenv_path)

    return app
