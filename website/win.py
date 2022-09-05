from flask import Blueprint, render_template, request, session
from . import db
from .models import Score

win = Blueprint('win', __name__)

@win.route('/win', methods=['GET', 'POST'])
def show_winner():
    if request.method == 'POST':
        if 'name' in request.form:
            name = request.form.get('name')
            points = calc_points()
            new_score = Score(name=name, points=points)
            db.session.add(new_score)
            db.session.commit()
            scores = Score.query.all();
            return render_template('scores.html', scores=scores)

    return render_template('win.html')

def calc_points():
    guesses = int(session['noGuesses'])
    points = 100 - (guesses * 10)
    if points < 0:
        points = 0

    return points