import cv2
import json
import numpy as np
from flask import Response
from imutils.object_detection import non_max_suppression
from .function_counter import detect
from ..models import frame


class Camera():
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
        # self.video = cv2.VideoCapture("rtsp://140.125.84.174:554/user=admin&password=1111f&channel=2&stream=0.sdp?real_stream--rtp-caching=100")
        
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
