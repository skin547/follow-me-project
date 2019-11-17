from App import app
from App.config import configs


class HerokuConfig(configs['default']):
    import os
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


if __name__ == '__main__':
    app.config.from_object(HerokuConfig)
    app.run(debug=True, threaded=True)
