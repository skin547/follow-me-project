class BaseConfig(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(BaseConfig):
    TESTING = True

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/followmeproject'
    DEBUG = True

configs = {'default': BaseConfig,
        'Testing' : TestingConfig,
        'development':DevelopmentConfig,
        }
