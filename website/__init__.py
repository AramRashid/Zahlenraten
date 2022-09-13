from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
DATABASE = "zahlenraten"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'freibier'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/' + DATABASE
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .layout import layout
    app.register_blueprint(layout, url_prefix='/')
    from .scores import scores
    app.register_blueprint(scores, url_prefix='/')
    from .game import game
    app.register_blueprint(game, url_prefix='/')
    from .win import win
    app.register_blueprint(win, url_prefix='/')
    return app


