from flask_restful import Resource, reqparse
from ..models import area, video
from ..import db
from multiprocessing import Process

class arealistApi(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument("user_id", type=int)
        parser.add_argument("name", type=str)
        parser.add_argument("capacity", type=int)
        parser.add_argument("id", type=int)
        parser.add_argument("source",type=str)
        self.__parser = parser

    def get(self):
        areas = area.query.all()
        result = []
        for item in areas:
            status = item.compute_status()
            result.append({"id": item.id,	'time': str(
                item.time), 'user_id': item.user_id, 'name': item.name,
                 'capacity': item.capacity, 'status':status['congestion'],
                 'number':status['number']})
        print(result)
        return result, 200


    def post(self):
        args = self.__parser.parse_args()
        print("request arguments:")
        print(args)
        new_area = area(args['user_id'], args['name'], args['capacity'])
        db.session.add(new_area)
        db.session.flush()
        db.session.refresh(new_area)
        new_video = video(new_area.id, args['source'])
        if(new_area == None or new_video == None):
            print("fail to create area or Video")
            return 201
        db.session.add(new_video)
        db.session.commit()
        return new_area.id,200

