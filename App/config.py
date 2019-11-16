class BaseConfig(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/followmeproject'

class TestingConfig(BaseConfig):
    TESTING = True

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class HerokuConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'postgres://zedkxxduqmtjgk:37eed2f1e3997e1690806a7ad79e077d762e5c6d4ed8546cb0447494970404f0@ec2-54-83-202-132.compute-1.amazonaws.com:5432/daee2gu6ugu8i2'

configs = {'default': BaseConfig,
        'Testing' : TestingConfig,
        'development':DevelopmentConfig,
        'heroku': HerokuConfig}
