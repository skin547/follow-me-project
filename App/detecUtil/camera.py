import cv2
import json
import numpy as np
from flask import Response
from imutils.object_detection import non_max_suppression
from .function_counter import detect, detector
from ..models import frame
from ..import db


class Camera():
    print("initialize HOG object...")
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def __init__(self,video_source):
        print("initialize camera...")
        self.flip = False
        if ".MOV" in video_source:
            self.flip = True
        if(video_source == '0'):
            video_source = 0
        self.video = cv2.VideoCapture(video_source)
        
    def __del__(self):
        print("release Camera...")
        self.video.release()
    
    def get_frame(self):
        success, frame = self.video.read()
        if(success):
            if(self.flip):
                frame = cv2.flip(frame, 0)
            frame = cv2.resize(frame, (900,650))
            jpeg = cv2.imencode('.jpg', frame)[1]
            jpeg = jpeg.tobytes()
            return jpeg
        print("end of video")
        self.__del__()    
        return None

    def get_detected_frame(self):
        success, frame = self.video.read()
        if(success):
            if(self.flip):
                frame = cv2.flip(frame, 0)
            rects, weights = self.hog.detectMultiScale(
                frame,
                winStride=(4, 4),
                padding=(2, 2),
                scale=1.5
            )
            for (x, y, w, h) in rects:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
            pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
            for (xA, yA, xB, yB) in pick:
                cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)

            frame = cv2.resize(frame, (900, 650))
            jpeg = cv2.imencode('.jpg', frame)[1]
            jpeg = jpeg.tobytes()
            return jpeg
        print("end of video")
        self.__del__()
        return None


    def stream_video(self):
        while (self.video.isOpened()):
            jpeg = self.get_detected_frame()
            if(jpeg != None):
                yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + jpeg + b'\r\n')
        yield (b'--frame')

    def stream_data(self, area_id):
        commit_count = 0
        while (self.video.isOpened()):
            commit_count+=1
            success, jpeg = self.video.read()
            if(commit_count >= 100):
                db.session.commit()
            if(success):
                num_of_people = detect(jpeg)
                detected_frame = frame(area_id, num_of_people)
                db.session.add(detected_frame)
                db.session.flush()
                data = {"number": detected_frame.number, 
                        "time": str(detected_frame.time),
                        "id": detected_frame.id, 
                        "area_id": detected_frame.area_id}
                yield (u'--frame\r\n'
                       u'Content-Type: Application/json\r\n\r\n' + json.dumps(data) + u'\r\n')
        db.session.commit()
        yield (b'--frame')

    
