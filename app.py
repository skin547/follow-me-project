from flask import Flask, render_template
from flask_cors import CORS
from flask_restful import Resource, Api
import time
from models.Region import Region, RegionController

app = Flask(__name__, template_folder="client/build",
            static_folder="client/build/static")
            
api = Api(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print("Current path:" + path)
    return render_template('index.html')
    
api.add_resource(RegionController, '/regions', resource_class_kwargs={'Model':Region()})

if __name__ == '__main__':
    CORS(app)
    app.run(host='0.0.0.0',debug=True)
