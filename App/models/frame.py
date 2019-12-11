from datetime import datetime
from ..import db

class frame(db.Model):
    __tablename__ = 'Frame'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    area_id = db.Column(db.Integer, db.ForeignKey('Area.id'))
    number = db.Column(db.Integer)
    time = db.Column(db.DateTime)

    def __init__(self,area_id,number):
        self.area_id = area_id
        self.number = number
        self.time = datetime.now()
    
    def get_latest_frame(self):
        latest_frame = self.query.order_by(self.id.desc()).first()
        return latest_frame
