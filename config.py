import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'cbade74258af26705d532a4b10ba91f3'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    JSON_AS_ASCII = False


class ProductionConfig(Config):
    DEBUG = False




class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
