from flask_restful import Resource, reqparse
import time
import json
from ..import db


class user(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)

    def __init__(self,name):
        print("Initialize Model: user ...")
        self.name = name
        # self.__users = []

    def list_all(self):
        return self.__users

    def add_user(self, args):
        newUser = {"userId": args['userId'], "password": args['password']}
        self.__users.append(newUser)
        # print(self.__regions)
        return newUser
    
    def login(self,args):
        if(args['userId'] == "1" and args['password'] == "1"):
            return True
        return False
