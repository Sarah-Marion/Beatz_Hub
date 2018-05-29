import os

# Class-based application configuration
class Config:
    """
    General configuration parent class
    """
    #pass
    SECRET_KEY = os.environ.get("SECRET_KEY")
    # DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME')


    #Flask-Mail SMTP server settings
    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SENDER_EMAIL = 'devsarahmarion@gmail.com'


    @staticmethod
    def init_app(app):
        pass


    # simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    BASIC_AUTH_USERNAME = 'Sarah'
    BASIC_AUTH_pASSWORD = os.environ.get("MAIL_PASSWORD")


    

class ProdConfig(Config):
    """
    Production configuration child class

    Args:
        Config: The parent configuration class with General
        configuration settings
    """
    # pass
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    # DEBUG = True



class DevConfig(Config):
    """
    Development configuration child class

    Args:
        Config: The parent configuration class with General
        configuration settings
    """
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DEBUG = True



class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
    # pass


config_options = {
    'development' : DevConfig,
    'production' : ProdConfig,
    'test' : TestConfig
}