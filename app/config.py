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
    DATABASE_URL = 'postgres://cehhfgwlmiqsap:5ffee63b8115d83936323f5111a4d00f4107ecab5e66793d61490ab4f9a8cea8@ec2-54-235-178-189.compute-1.amazonaws.com:5432/d7th6ear304m3k'


class DevelopmentConfig(Config):
    """ This class defines variables for the development environment """
    DEBUG = True
    DATABASE_URL = 'postgres://cehhfgwlmiqsap:5ffee63b8115d83936323f5111a4d00f4107ecab5e66793d61490ab4f9a8cea8@ec2-54-235-178-189.compute-1.amazonaws.com:5432/d7th6ear304m3k'
    # DATABASE_URL = 'postgres://postgres:star2030@localhost:/db_sendify'


class ProductionConfig(Config):
    """ This class defines variables for the production environment """
    DEBUG = False
    DATABASE_URL = 'postgresql-rectangular-91541'

app_config = {
    'testing': TestConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
