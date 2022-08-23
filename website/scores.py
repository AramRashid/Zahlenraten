from flask import Blueprint, render_template
from .models import Score

scores = Blueprint('scores', __name__)

@scores.route('/scoreboard')
def scoreboard():
    scores = Score.query.all();
    return render_template('scores.html', scores=scores)