from App.config import configs
from App import app

if __name__ == '__main__':
    app.config.from_object(configs['heroku'])
    app.run(debug=True, threaded=True)
