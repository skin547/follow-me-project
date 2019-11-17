import time
import json
from flask_restful import Resource, reqparse
from ..models import area
from .. import db

class areaApi(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument("user", type=int)
        parser.add_argument("name", type=str)
        parser.add_argument("number", type=int)
        parser.add_argument("id", type=int)
        self.__parser = parser

    def get(self,id):
        target = area.query.get(id)
        if(target):
            return ({"id":target.id, 'name':target.name,'number':target.number, 'userid':target.user,'time':str(target.time)}),200
        return 201

    def post(self):
        args = self.__parser.parse_args()
        print("request arguments:")
        print(args)
        new_area = area(args['user'],args['name'],args['number'])
        if(new_area == None):
            print("fail to create area")
            return 201
        db.session.add(new_area)
        db.session.commit()
        return 201
