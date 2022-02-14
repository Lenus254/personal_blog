from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.config import Config
from flask_migrate import Migrate
from app.config import config_options
from flask_mail import Mail


login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


app = Flask(__name__)
mail = Mail()
db = SQLAlchemy()

def create_app(config_name):
    
    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    
    app.config['SECRET_KEY'] = 'lenus254'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://lenus:2580/flaskblog'
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    app.config['DEBUG']=True
    db.init_app(app)
    # bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    
    from app.users.views import users 
    from app.posts.views import posts
    from app.main.views import main 
    
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app

