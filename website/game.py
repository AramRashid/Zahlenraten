from flask import Blueprint, render_template, request, session, redirect, url_for

game = Blueprint('game', __name__)

@game.route('/game', methods=['GET', 'POST'])
def show_gamegame():
    
    if request.method == 'POST':
        if 'guess' in request.form:
            guess = request.form.get('guess')
            status = get_status(int(guess))
            guess_count = int(session['noGuesses'])
            guess_count = guess_count + 1
            session['noGuesses'] = guess_count
            if status == 'Gewonnen':
                return redirect(url_for('win.show_winner'))
            else:       
                return render_template('game.html', status=status, counter=guess_count)
    return render_template('game.html')

def get_status(guess):
    if 'rndNumber' in session:
        if int(session['rndNumber']) < guess:
            return 'Tiefer'

        if int(session['rndNumber']) > guess:
            return 'Höher'

        return 'Gewonnen'
    
    return ''

