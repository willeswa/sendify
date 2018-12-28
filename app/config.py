""" This modules holds classes for different environment config """
import os


secret_key = os.getenv('SECRET_KEY')
jwt_secret_key = os.getenv('JWT_SECRET_KEY')
url = os.getenv('DATABASE_URL')


class Config:
    """ This class defines common variables to all environment """
    ERROR_404_HELP = False
    SECRET_KEY = secret_key
    JWT_SECRET_KEY = jwt_secret_key
    DATABASE_URL = url


class TestConfig(Config):
    """ This class defines variables for the testing environment """
    TESTING = True

class DevelopmentConfig(Config):
    """ This class defines variables for the development environment """
    DEBUG = True


class ProductionConfig(Config):
    """ This class defines variables for the production environment """
    DEBUG = False


app_config = {
    'testing': TestConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
