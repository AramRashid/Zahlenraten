from flask import Blueprint, render_template, request, session

game = Blueprint('game', __name__)

@game.route('/game', methods=['GET', 'POST'])
def show_gamegame():
    
    if request.method == 'POST':
        guess = request.form.get('guess')
        status = get_status(int(guess))

        return render_template('game.html', status=status)
    return render_template('game.html')

def get_status(guess):
    if 'rndNumber' in session:
        if int(session['rndNumber']) < guess:
            return 'tiefer'

        if int(session['rndNumber']) > guess:
            return 'höher'

        return 'gewonnen'
    
    return ''

