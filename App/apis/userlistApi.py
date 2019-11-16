from flask_restful import Resource, reqparse
from ..models import user
from .. import db

class userlistApi(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", type=int)
        parser.add_argument("password", type=str)
        parser.add_argument("name", type=str)
        self.__parser = parser

    def get(self):
        users = user.query.all()
        result = []
        for item in users:
            result.append({'id': item.id, 'name': item.name})
        return result,201

    def post(self):
        args = self.__parser.parse_args()
        print("request arguments:")
        print(args)
        new_user = user(args['name'])
        db.session.add(new_user)
        db.session.commit()
        return {"id": new_user.id, "name": new_user.name}, 201
