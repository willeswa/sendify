import os

# Global imports
from flask import Flask
from flask_jwt_extended import JWTManager
from app.config import app_config
from app.db_config import Database
from dotenv import load_dotenv

db = Database()
env = os.getenv('FLASK_ENV')
super_secret = os.getenv('JWT_SECRET_KEY')


def create_app(config_name):
    """ Create the application factory """

    app = Flask(__name__)
    app.config.from_object(app_config['development'])
    app.config.from_pyfile('config.py')
    app.config['JWT_SECRET_KEY'] = super_secret
    JWTManager(app)

    """ create tables """
    db.destroy_tables()
    db.create_table()

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
