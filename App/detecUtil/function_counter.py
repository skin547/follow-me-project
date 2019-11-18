import numpy as np
from imutils.object_detection import non_max_suppression
import cv2

def detector(video):
    cap = cv2.VideoCapture(video.source)
    # cap = video
    print(cap.isOpened())
    sec_num = 0
    counter = 0
    while(cap.isOpened()):
            ret, frame = cap.read()
            frame = cv2.flip(frame,0)
            counter = counter + 1
            if ret == True:
                if(counter >= 24):
                    counter = 0
                    sec_num = sec_num + 1
                    yield (detect(frame))
                if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
            else:
                break


def detect(frame):
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    rects, weights = hog.detectMultiScale(
        frame,
        winStride=(4, 4), 
        padding=(2, 2), 
        scale=1.5
    )
    for (x, y, w, h) in rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
    
    people_detected = 0
    
    for (xA, yA, xB, yB) in pick:
        people_detected += 1
    return (people_detected)
    
