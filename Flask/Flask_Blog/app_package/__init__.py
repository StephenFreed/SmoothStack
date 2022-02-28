from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

# key for WT Forms CRF Token
app.config["SECRET_KEY"] = "639ded68629a54ac"
# SQLite development database // use PostgreSQL for production
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

# db = SQLAlchemy.create_engine(f'sqlite:///db1.db')
db = SQLAlchemy(app)

# used to encrypt/decrypt passwords
bcrypt = Bcrypt(app)

# Login Manager
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_categor = "info"

from app_package import routes
