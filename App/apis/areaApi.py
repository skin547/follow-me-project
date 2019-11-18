import time
import json
from flask_restful import Resource, reqparse
from ..models import area
from ..models import frame
from .. import db

class areaApi(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument("user", type=int)
        parser.add_argument("name", type=str)
        parser.add_argument("capacity", type=int)
        parser.add_argument("id", type=int)
        self.__parser = parser

    def get(self,id):
        target = area.query.get(id)
        if(target):
            return ({"id": target.id, 'name': target.name, 
            'capacity': target.capacity, 'userid': target.user, 
            'time': str(target.time),'status':self.compute_status(target)}), 200
        return 201

    def post(self):
        args = self.__parser.parse_args()
        print("request arguments:")
        print(args)
        new_area = area(args['user'], args['name'], args['capacity'])
        if(new_area == None):
            print("fail to create area")
            return 201
        db.session.add(new_area)
        db.session.commit()
        return 201

    def compute_status(self,area):
        if(area.capacity == 0):
            return None
        area_frame = frame.query.filter(frame.area == area.id)
        if(area_frame != None):
            latest_frame = area_frame.order_by(frame.id.desc()).first()
            current_num_of_people = latest_frame.number
            congestion = current_num_of_people/area.capacity
            if(congestion <0.25):
                status = 'green'
            elif(congestion < 0.5):
                status = 'yellow'
            elif(congestion < 0.75):
                status = 'red'
            else:
                status = 'purple'
            return status
        return None
