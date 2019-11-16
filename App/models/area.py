from datetime import datetime
import json
from ..import db


class area(db.Model):
    __tablename__ = 'Area'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.Integer)
    name = db.Column(db.String)
    number = db.Column(db.Integer)
    time = db.Column(db.DateTime)

    def __init__(self,user,name,number):
        self.user = user
        self.name = name
        self.number = number
        self.time = datetime.now()
