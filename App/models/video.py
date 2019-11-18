from .. import db


class video(db.Model):
    __tablename__ = 'video'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    area = db.Column(db.Integer)
    source = db.Column(db.String)

    def __init__(self, areaid, source):
        self.area = areaid
        self.source = source
