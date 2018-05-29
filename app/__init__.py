from flask import Flask
from flask_bootstrap import Bootstrap
<<<<<<< HEAD
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_admin import Admin
from flask_simplemde import SimpleMDE
from flask_basicauth import BasicAuth
from flask_uploads import UploadSet,configure_uploads,IMAGES



bootstrap = Bootstrap()
db = SQLAlchemy()
admin = Admin()
mail = Mail()
photos = UploadSet('photos',IMAGES)
simple = SimpleMDE()
basic_auth= BasicAuth()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'



def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations.
    app.config.from_object(config_options[config_name])

    # Intitializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)
    mail.init_app(app)
    simple.init_app(app)
    basic_auth.init_app(app)

    # configure upload setUp
    configure_uploads(app,photos)

    
    # Registering the blueprint

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

    # setting config
=======
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
>>>>>>> b3a4641111124f9321b173e15e0cbef1545eba88

    return app