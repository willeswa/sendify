""" This modules holds classes for different environment config """


class Config:
    """ This class defines common variables to all environment """
    SECRET_KEY = 'SOME SUPER SECRET'
    ERROR_404_HELP = False
    DATABASE_URI = 'postgres://postgres:star2030@localhost:/db_sendify'


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
