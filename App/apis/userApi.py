import time
import json
import cv2
import flask
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
        self.__parser = parser


    def get(self,id):
        target = user.query.get(id)
        if(target):
            return ({'id': target.id, 'name': target.name}), 200
        return 201

    def post(self):
        args = self.__parser.parse_args()
        print("request arguments:")
        print(args)
        new_user = user(args['name'])
        db.session.add(new_user)
        db.session.commit()
        return {"id":new_user.id, "name":new_user.name},201
    
    
