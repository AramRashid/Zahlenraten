from ast import List
from .. import db
from ..models import Score

class ScoreManager:
    def InsertScore(self, name: str, points: int) -> None:
        if not name or len(name) == 0:
            raise ValueError('name must be specified')

        if not points:
            raise ValueError('points must be specified')

        new_score = Score(name=name, points=points)
        db.session.add(new_score)
        db.session.commit()

    def GetScores(self) -> List:
        scores = Score.query.order_by(Score.points.desc()).all()
        return scores

