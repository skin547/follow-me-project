class BaseConfig(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/followmeproject'

class TestingConfig(BaseConfig):
    TESTING = True

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class HerokuConfig(BaseConfig):
    import os
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    
configs = {'default': BaseConfig,
        'Testing' : TestingConfig,
        'development':DevelopmentConfig,
        'heroku': HerokuConfig}
