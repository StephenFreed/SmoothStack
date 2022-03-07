from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

application = Flask(__name__)
application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# key for WT Forms CRF Token
application.config["SECRET_KEY"] = "639ded68629a54ac"

# SQLite development database // use PostgreSQL for production
application.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/site.db"

# db = SQLAlchemy.create_engine(f'sqlite:///db1.db')
db = SQLAlchemy(application)

# used to encrypt/decrypt passwords
bcrypt = Bcrypt(application)

# Login Manager
login_manager = LoginManager(application)
login_manager.login_view = "login"
login_manager.login_message_categor = "info"

# access to routes
from app_package import routes
