from . import db

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer)
    points = db.Column(db.String(255))