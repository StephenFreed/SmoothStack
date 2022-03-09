from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
api = Api(application)

# SQLite development database // use PostgreSQL for production
application.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/database.db"
application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(application)

from app_package import resources
