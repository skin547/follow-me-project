from flask import Flask, render_template
from flask_restful import Resource, Api
import time
import json
from models.Region import Region, RegionController

app = Flask(__name__, template_folder="client/build",
            static_folder="client/build/static")
            
api = Api(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print("Current path:" + path)
    return render_template('index.html')
    # return 'You want path: %s' % path

api.add_resource(RegionController, '/regions')

if __name__ == '__main__':
    app.run(debug=True)
