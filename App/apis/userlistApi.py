from flask_restful import Resource, reqparse
from ..models import user
from .. import db

class userlistApi(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", type=int)
        parser.add_argument("password", type=str)
        parser.add_argument("name", type=str)
        parser.add_argument("image_path", type=str)
        self.__parser = parser

    def get(self):
        users = user.query.all()
        result = []
        for item in users:
            areas = []
            for area in item.areas:
                status = area.compute_status()
                area = ({"name": area.name,"video_id":area.video[0].id, "id": area.id, "capacity": area.capacity,
                         "number": status['number'], "status": status['congestion']})
                areas.append(area)
            result.append({'id': item.id, 'name': item.name,'image_path':item.image_path,'areas':areas})
        return result,201

    def post(self):
        args = self.__parser.parse_args()
        print("request arguments:")
        print(args)
        new_user = user(args['name'], args['image_path'])
        db.session.add(new_user)
        db.session.commit()
        return {"id": new_user.id, "name": new_user.name}, 201
