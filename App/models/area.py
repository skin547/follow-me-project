from datetime import datetime
import json
from .frame import frame
from ..import db


class area(db.Model):
    __tablename__ = 'Area'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.Integer)
    name = db.Column(db.String)
    capacity = db.Column(db.Integer)
    time = db.Column(db.DateTime)

    def __init__(self, user, name, capacity):
        self.user = user
        self.name = name
        self.capacity = capacity
        self.time = datetime.now()

    def compute_status(self):
        if(self.capacity == 0):
            return None
        area_frame = frame.query.filter(frame.area == area.id)
        if(area_frame != None):
            latest_frame = area_frame.order_by(frame.id.desc()).first()
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
        return None
