""" This modules holds classes for different environment config """
import os


# secret_key = os.getenv('SECRET_KEY')


class Config:
    """ This class defines common variables to all environment """
    ERROR_404_HELP = False
    SECRET_KEY='i like my women tall and bulky'
    JWT_SECRET_KEY='i said i like my women tall and bulky'
    


class TestConfig(Config):
    """ This class defines variables for the testing environment """
    TESTING = True
    DATABASE_URI = 'postgres://postgres:star2030@localhost:/testdb_sendify'


class DevelopmentConfig(Config):
    """ This class defines variables for the development environment """
    DEBUG = True
    DATABASE_URI = 'postgresql-rectangular-91541'
    # DATABASE_URI = 'postgres://postgres:star2030@localhost:/db_sendify'


class ProductionConfig(Config):
    """ This class defines variables for the production environment """
    DEBUG = False
    DATABASE_URI = 'postgresql-rectangular-91541'

app_config = {
    'testing': TestConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
