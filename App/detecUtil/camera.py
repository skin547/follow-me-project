import cv2
import json
from .function_counter import detect
from ..models import frame
from flask import Response

# def detector(video):
#     print(video.isOpened())
#     sec_num = 0
#     counter = 0
#     while(video.isOpened()):
#         ret, frame = video.read()
#         counter = counter + 1
#         if ret == True:
#             if(counter >= 24):
#                 counter = 0
#                 sec_num = sec_num + 1
#                 yield (detect(frame))
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#         else:
#             break

# def detect_generator(detector):
#     for count in detector:
#         frame = frame(1,count)
#         # yield area
#         yield (u'--frame\r\n'
#                u'Content-Type: application/json\r\n\r\n' + json.dumps(frame) + u'\r\n')

class Camera():

    def __init__(self,video):
        stream_video = cv2.VideoCapture(video.source)
    
    def get_frame(self):
        if(self.stream_video.isOpened()):
            success,frame = self.stream_video.read()
            if(success):
                jpeg = cv2.imencode('.jpg', frame)[1]
                jpeg = jpeg.tobytes()
                return jpeg

def stream(video_source):
    stream_video = cv2.VideoCapture(video_source)
    while(stream_video.isOpened()):
        success, frame = stream_video.read()
        frame = cv2.flip(frame,0)
        if(success):
            jpeg = cv2.imencode('.jpg', frame)[1]
            jpeg = jpeg.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + jpeg + b'\r\n')

# def stream(video):
#     Camera(video)
