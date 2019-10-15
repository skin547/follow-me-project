import time
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument("name",type=str)
parser.add_argument("counted",type=int)

class RegionController(Resource):
    def __init__(self):
        self.region = Region()

    def get(self):
        return self.region.list_all()

    def post(self):
        args = parser.parse_args()
        print(args)
        new_region = self.region.add_region(args)
        return new_region, 201

class Region():
    def __init__(self):
        self.regions = [{"name": "Region A", "date": time.time(), "counted": 112}, 
                        {"name": "Region B", "date": time.time(), "counted": 26},]

    def list_all(self):
        return self.regions

    def add_region(self,args):
        new_region = {"name":args['name'],"date":time.time(),"counted":args['counted']}
        self.regions.append(new_region)
        print(self.regions)
        return new_region