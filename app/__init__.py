import os

# Global imports
from flask import Flask
from app.config import app_config
from app.db_config import create_table, destroy_tables
from dotenv import load_dotenv


def create_app(config_name):
    """ Create the application factory """

    app = Flask(__name__)
    app.config.from_object(app_config['development'])
    app.config.from_pyfile('config.py')

    """ create tables """
    destroy_tables()
    create_table()

    """ import api versions """
    from app.api.v1 import v1
    from app.api.v2 import v2

    """ Register blueprints """
    app.register_blueprint(v1)
    app.register_blueprint(v2)

    APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
    dotenv_path = os.path.join(APP_ROOT, '.env')
    load_dotenv(dotenv_path)

    return app
