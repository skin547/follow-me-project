import json
from flask import Response
from flask_restful import Resource , reqparse
from ..models import video
from ..models import frame
from ..import db
from multiprocessing import Process
# from ..detecUtil.camera import stream
from ..detecUtil.camera import Camera
from ..detecUtil.function_counter import detector

class videoApi(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument("area", type=int)
        parser.add_argument("source", type=str)
        self.__parser = parser
    
    def get(self,id):
        vid = video.query.get(id)
        if(vid == None):
            return {"status":"video not found"},201
        camera = Camera(vid.source)
        return Response(camera.stream_video(),  mimetype='multipart/x-mixed-replace; boundary=frame')
        # return Response(self.start_detect(vid), mimetype='multipart/x-mixed-replace; boundary=frame')

    def post(self):
        args = self.__parser.parse_args()
        new_video = video(args['area'], args['source'])
        db.session.add(new_video)
        db.session.commit()
        result = {"id":new_video.id,'area':new_video.area_id,'source':new_video.source}
        ## TODO : implement people detect here
        print("start detecting area:" + str(new_video.area))
        Process(target = self.start_detect, args={new_video} ).start()
        # p1.start()
        return result, 200

