from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'freibier'

    from .views import views
    app.register_blueprint(views, url_prefix='/')
    from .scores import scores
    app.register_blueprint(scores, url_prefix='/')
    from .game import game
    app.register_blueprint(game, url_prefix='/')
    return app


