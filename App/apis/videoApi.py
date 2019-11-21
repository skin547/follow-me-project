from flask import Response
from flask_restful import Resource , reqparse
from ..models import video
from ..models import frame
from ..import db
from multiprocessing import Process
from ..detecUtil.camera import stream
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
        return Response(stream(vid.source), mimetype='multipart/x-mixed-replace; boundary=frame')

    def post(self):
        args = self.__parser.parse_args()
        new_video = video(args['area'], "App/detecUtil/IMG_2185.MOV")
        db.session.add(new_video)
        db.session.commit()
        result = {"id":new_video.id,'area':new_video.area,'source':new_video.source}
        ## TODO : implement people detect here
        print("start detecting area:" + str(new_video.area))
        Process(target = self.start_detect, args={new_video} ).start()
        # p1.start()
        return result, 200

    def start_detect(self,video):
        for detect_result in detector(video):
            new_frame = frame(video.area,detect_result)
            db.session.add(new_frame)
            db.session.commit()
        print("End of detect for area:" + str(video.area))