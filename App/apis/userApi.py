import time
import json
import cv2
from flask import Response
from flask_restful import Resource, reqparse
from ..models.user import user
from ..detecUtil.function_counter import detector
from ..import db

class userApi(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", type=int)
        parser.add_argument("password", type=str)
        parser.add_argument("name", type=str)
        parser.add_argument("image_path",type=str)
        self.__parser = parser


    def get(self,id):
        target = user.query.get(id)
        if(target):
            areas = [] 
            if(target.areas):
                for area in target.areas:
                    status = area.compute_status()
                    area_item = {"name": area.name, 
                                 "id": area.id, 
                                 "video_id": area.video[0].id, 
                                 "capacity": area.capacity,
                                 "number": status['number'],
                                 "status": status['congestion']}
                    areas.append((area_item))
            # else: areas is empty
            else:
                area_item = {"name": "未開放",
                             "id": 1, 
                             "video_id": 1, 
                             "capacity": 0,
                             "number": 0, 
                             "status": 'grey'}
                areas.append((area_item))
            return ({'id': target.id, 'name': target.name,'image_path':target.image_path,'areas':areas}, 200 )
        return 201

    def post(self):
        args = self.__parser.parse_args()
        print("request arguments:")
        print(args)
        new_user = user(args['name'],args['image_path'])
        db.session.add(new_user)
        db.session.commit()
        return {"id":new_user.id, "name":new_user.name},201
    
