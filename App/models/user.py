from flask_restful import Resource, reqparse
import time
import json
from ..import db
from .area import area

class user(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    image_path = db.Column(db.String)
    areas = db.relationship('area', backref='user', lazy=True)

    def __init__(self,name,image_path):
        print("Initialize Model: user ...")
        self.name = name
        self.image_path = image_path


