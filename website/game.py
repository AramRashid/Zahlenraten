from flask import Blueprint, render_template, request, session, redirect, url_for

game = Blueprint('game', __name__)

@game.route('/game', methods=['GET', 'POST'])
def show_game():
    if request.method == 'POST':
        if 'guess' in request.form:
            guess = request.form.get('guess')
            if not guess:
                guess = 0

            rnd_number = int(session['rndNumber'])   
            status = get_status(int(guess), rnd_number)
            guess_count = int(session['noGuesses'])
            guess_count = guess_count + 1       
            session['noGuesses'] = guess_count
            points = calc_points(guess_count)
            session['points'] = points
            if status == 'Gewonnen':
                return redirect(url_for('win.show_winner'))
            else:       
                return render_template('game.html', status=status, counter=guess_count, points=points)
    return render_template('game.html')

def get_status(guess: int, rnd_number: int) -> str:
    if rnd_number < guess:
        return 'Tiefer'
    if rnd_number > guess:
        return 'Höher'

    return 'Gewonnen'

def calc_points(guesses: int) -> int:
    points = 100 - (guesses * 10)
    if points < 0:
        points = 0

    return points

