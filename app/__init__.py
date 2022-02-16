
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import config_options
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

mail = Mail()

db = SQLAlchemy()

bootstrap = Bootstrap()

photos = UploadSet('photos',IMAGES)




def create_app(config_name):

    # Initializing application
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    mail.init_app(app)


    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .users import users as users_blueprint
    app.register_blueprint(users_blueprint,url_prefix = '/authenticate')
    
    from .posts import posts as posts_blueprint
    app.register_blueprint(posts_blueprint)
    
    
    

    # setting config
    # from .requests import configure_request

    # configure UploadSet
    configure_uploads(app,photos)

    # Will add the views and forms

    return app