from flask import Flask, render_template
from flask_restful import Resource, Api
import time
import json
import models.Region

app = Flask(__name__, template_folder="client/build",
            static_folder="client/build/static")
api = Api(app)

class Region(Resource):
    def __init__(self):
        self.regions = [{"name": "Region A", "date": time.time(), "counted": 112}, {
            "name": "Region B", "date": time.time(), "counted": 26}]

    def get(self):
        return self.regions
        

@app.route('/prediction')
def predict():
    return "This is test api"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print("Current path:" + path)
    return render_template('index.html')
    # return 'You want path: %s' % path

api.add_resource(Region, '/regions')

if __name__ == '__main__':
    app.run(debug=True)
