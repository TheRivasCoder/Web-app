from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'QWERTYUIOPASDFGHJKL'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prfix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app