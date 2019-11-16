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

    def detect_generator(self,detector):
        id_counter = 0
        for count in detector:
            id_counter += 1
            area = self.__user.addArea(id_counter,"area"+str(id_counter),count)
            # yield area
            yield (u'--frame\r\n'
                   u'Content-Type: application/json\r\n\r\n' + json.dumps(area) + u'\r\n')

    def get(self,id):
        target = user.query.get(id)
        if(target):
            return ({'id': target.id, 'name': target.name}), 200
        return 201
        # video = cv2.VideoCapture('App/detecUtil/VIDEO0003.mp4')
        # detecor = detector(video)
        # # for count in detecor:
        # #     print(count)
        # # for detect in self.detect_generator(detecor):
        # #     print(detect)

        # return Response(self.detect_generator(detecor), mimetype='multipart/x-mixed-replace; boundary=frame')
        # return {"status":"detect end"}
        # return self.__user.list_all()

    def post(self):
        args = self.__parser.parse_args()
        print("request arguments:")
        print(args)
        new_user = user(args['name'])
        db.session.add(new_user)
        db.session.commit()
        return {"id":new_user.id, "name":new_user.name},201
        # print("now login")
        # if self.__user.login(args):
        #     print(args['userId'])
        #     print("Login Successful")
        #     return {"status":"login success!"}
        # else:
        #     print("login fail")
        #     new_user = self.__user.add_user(args)
        #     return new_user, 201
    
    
