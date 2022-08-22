from flask import Blueprint

scores = Blueprint('scores', __name__)

@scores.route('/scoreboard')
def scoreboard():
    return "<p>Scoreboard</p"