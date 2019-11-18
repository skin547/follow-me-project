from flask_restful import Resource,reqparse
from datetime import datetime
from ..models import frame
from .. import db

class frameApi(Resource):
    
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument("area", type=int)
        parser.add_argument("number", type=int)
        self.__parser = parser

    def put(self):
        # result = frame.query.get(id)
        result = frame.query.order_by(frame.id.desc()).first()
        print(result)
        return {"id":result.id,"area":result.area,"number":result.number,"time":str(result.time)},200

    def get(self):
        frames = frame.query.all()
        result = []
        for item in frames:
            result.append({'id': item.id, 'number': item.number,'area':item.area,'time':str(item.time)})
        return result, 200
    
    def post(self):
        args = self.__parser.parse_args()
        print("request arguments:")
        print(args)
        new_frame = frame(args['area'],args['number'])
        if(new_frame == None):
            print("fail to create frame")
            return 201
        db.session.add(new_frame)
        db.session.commit()
        return {"id":new_frame.id,"number":new_frame.number} ,201

