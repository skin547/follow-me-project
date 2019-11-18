import time
from flask import Flask, render_template
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
# from .config import configs
from .dev_config import configs

app = Flask(__name__,
            template_folder="./frontend/build",
            static_folder="./frontend/build/static")
app.config.from_object(configs['development'])
# CORS(app)
api = Api(app)
db = SQLAlchemy(app)

from .models.user import user
from .models.area import area
from .apis.userApi import userApi
from .apis.areaApi import areaApi
from .apis.arealistApi import arealistApi
from .apis.userlistApi import userlistApi
from .apis.videoApi import videoApi
from .apis.frameApi import frameApi

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print("Current path:" + path)
    return render_template('index.html')


api.add_resource(arealistApi, '/api/areas', )
api.add_resource(areaApi, '/api/areas/<int:id>', )
api.add_resource(userlistApi, '/api/users', )
api.add_resource(userApi, '/api/users/<int:id>', )
api.add_resource(videoApi, '/api/video', '/api/video/<int:id>')
api.add_resource(frameApi, '/api/frame', )
