import time
import json
from flask_restful import Resource, reqparse
from ..models import area
from ..models import frame
from ..models import video
from .. import db

class areaApi(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument("user", type=int)
        parser.add_argument("name", type=str)
        parser.add_argument("capacity", type=int)
        parser.add_argument("source", type=str)
        self.__parser = parser

    def get(self,id):
        target = area.query.get(id)
        if(target):
            status = target.compute_status()
            user = target.user
            frames_list = []
            for frame in target.frames:
                frames_list.append({"number":frame.number,'time':str(frame.time)})
            return ({"id": target.id, 
                    'name': target.name, 
                    'capacity': target.capacity, 
                    'time': str(target.time), 
                    'status': status['congestion'], 
                    'number': status['number'], 
                    'user': {"name": user.name,
                             "id": user.id} ,
                    'video_id':target.video[0].id,
                     'frames': frames_list}), 200
        return 201

    def post(self):
        args = self.__parser.parse_args()
        print("request arguments:")
        print(args)
        new_area = area(args['user'], args['name'], args['capacity'])
        new_video = video(new_area.id,args['source'])
        if(new_area == None or new_video == None):
            print("fail to create area or Video")
            return 201
        db.session.add(new_area)
        db.session.commit()
        return 200

