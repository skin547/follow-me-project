from App.config import configs


class HerokuConfig(configs['default']):
    import os
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

from App import app

if __name__ == '__main__':
    app.config.from_object(HerokuConfig)
    app.run(debug=True, threaded=True)
