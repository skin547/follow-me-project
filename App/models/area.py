from datetime import datetime
import json
from .frame import frame
from ..import db

class area(db.Model):
    __tablename__ = 'Area'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    frames = db.relationship("frame", backref='area')
    video = db.relationship("video", backref='area')
    name = db.Column(db.String)
    capacity = db.Column(db.Integer)
    time = db.Column(db.DateTime)

    def __init__(self, user_id, name, capacity):
        self.user_id = user_id
        self.name = name
        self.capacity = capacity
        self.time = datetime.now()

    def compute_status(self):
        if(self.capacity == 0):
            return {"congestion": None, "number": None}
        area_frame = frame.query.filter(frame.area_id == self.id)
        if(area_frame != None):
            latest_frame = area_frame.order_by(frame.id.desc()).first()
            if(latest_frame != None):
                current_num_of_people = latest_frame.number
                congestion = current_num_of_people/self.capacity
                if(congestion < 0.25):
                    status = 'green'
                elif(congestion < 0.5):
                    status = 'yellow'
                elif(congestion < 0.75):
                    status = 'red'
                else:
                    status = 'purple'
                return {"congestion": status, "number": current_num_of_people}
        return {"congestion": "grey", "number": 0}

    # def stream_data(self):
    #     while (self.video.isOpened()):
    #         detected_num = detect(self.get_frame())
    #         new_frame = frame()
    #         if(data != None):
    #             yield (b'--data\r\n'
    #                    b'Content-Type: application/json\r\n\r\n' + data + b'\r\n')
    #     yield (b'--data')
