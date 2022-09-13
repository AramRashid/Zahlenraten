from flask import Blueprint, render_template, request, session
from .database.ScoreManager import ScoreManager

win = Blueprint('win', __name__)

@win.route('/win', methods=['GET', 'POST'])
def show_winner():
    if request.method == 'POST':
        if 'name' in request.form:
            name = request.form.get('name')
            points = int(session['points'])
            scoreMgr = ScoreManager()

            try:
                scoreMgr.InsertScore(name, points)
                scores = scoreMgr.GetScores()
            except:
                return render_template('scores.html', error=True)
           
            return render_template('scores.html', scores=scores)

    return render_template('win.html')