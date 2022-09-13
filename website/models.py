from . import db

class Score(db.Model):
    __name__ = 'score'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    points = db.Column(db.Integer)