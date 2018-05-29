import os
<<<<<<< HEAD

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


=======
class Config:
    '''
    Describe the general configuarations
    '''
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
     
    # Simple Mde Configs
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    # Sending Emails
    # MAIL_SERVER=os.environ.get('MAIL_SERVER')
    # MAIL_PORT=os.environ.get('MAIL_PORT')
    # MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS')
    # MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')

    UPLOADED_PHOTOS_DEST = 'app/static/photos'
>>>>>>> b3a4641111124f9321b173e15e0cbef1545eba88
    @staticmethod
    def init_app(app):
        pass

<<<<<<< HEAD

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
=======
class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DEBUG = False

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    DEBUG = True

class TestConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_TEST')
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
>>>>>>> b3a4641111124f9321b173e15e0cbef1545eba88
}