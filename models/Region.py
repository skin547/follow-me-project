import time
import json
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument("name",type=str)
parser.add_argument("counted",type=int)

class RegionController(Resource):
    def __init__(self, Model):
        # print("Initialize Region Controller...")
        self.__region = Model

    def get(self):
        return self.__region.list_all()

    def post(self):
        args = parser.parse_args()
        # print("request arguments:")
        print(args)
        new_region = self.__region.add_region(args)
        return new_region, 201

class Region():
    def __init__(self):
        print("Initialize Model: Region ...")
        self.__regions = []

    def list_all(self):
        return self.__regions

    def add_region(self,args):
        new_region = {"name":args['name'],"date":time.time(),"counted":args['counted']}
        self.__regions.append(new_region)
        # print(self.__regions)
        return new_region
