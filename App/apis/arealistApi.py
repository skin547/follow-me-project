from flask_restful import Resource, reqparse
from ..models import area
from ..import db

class arealistApi(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument("user", type=int)
        parser.add_argument("name", type=str)
        parser.add_argument("capacity", type=int)
        parser.add_argument("id", type=int)
        self.__parser = parser

    def get(self):
        areas = area.query.all()
        result = []
        for item in areas:
            result.append({"id": item.id,	'time': str(
                item.time), 'user': item.user, 'name': item.name, 'capacity': item.capacity})
        print(result)
        return result, 200

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
        result = {"id": new_area.id, "userId": new_area.user, "name": new_area.name,
                  "capacity": new_area.capacity, "time": str(new_area.time)}
        return result, 201

    # def post(self):
    #     args = self.__parser.parse_args()
    #     # print("request arguments:")
    #     print(args)
    #     newArea = self.__areaModel.addArea(
    #         args['id'], args['name'], args['counted'])
    #     if(newArea == None):
    #         print("fail to create area")
    #         return 201
    #     return newArea, 201
        
