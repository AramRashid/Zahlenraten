from random import randrange
from flask import Blueprint, render_template, session

layout = Blueprint('views', __name__)

@layout.route('/', methods=['GET', 'POST'])
def home():
    rndNumber = randrange(0, 100)
    session['rndNumber'] = rndNumber
    session['noGuesses'] = 0
    return render_template('main.html')