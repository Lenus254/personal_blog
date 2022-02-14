from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.config import Config
from flask_migrate import Migrate
from app.config import config_options


login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


app = Flask(__name__)
mail = Mail()
db = SQLAlchemy()

