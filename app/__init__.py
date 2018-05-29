from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_simplemde import SimpleMDE
from config import config_options

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
photos = UploadSet('photos',IMAGES)
simple = SimpleMDE()

def create_app(config_name):
    
    app = Flask(__name__)

    # app configurations
    app.config.from_object(config_options[config_name])

    # initializing flask extensions
    config_options[config_name].init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    simple.init_app(app)

    # Register the main app blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # adding the admin app blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    configure_uploads(app,photos)

    return app