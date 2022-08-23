from random import randrange
from flask import Blueprint, render_template, session

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    rndNumber = randrange(0, 100)
    session['rndNumber'] = rndNumber
    session['noGuesses'] = 0
    return render_template('main.html')