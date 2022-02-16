import os


class Config:
    SECRET_KEY = 'SECRET_KEY'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lenus:2580@localhost/myblog'
    
    
    #  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lenus:2580@localhost/myblog'


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lenus:2580@localhost/myblog'
    DEBUG = True
    
    
config_options = {
'development': DevConfig,
'production': ProdConfig
}