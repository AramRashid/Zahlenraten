from flask import Blueprint, render_template
from .models import Score
from .database.ScoreManager import ScoreManager

scores = Blueprint('scores', __name__)

@scores.route('/scoreboard')
def scoreboard():
    scoreMgr = ScoreManager()
    scores = scoreMgr.GetScores()
    return render_template('scores.html', scores=scores)