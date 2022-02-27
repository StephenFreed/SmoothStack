from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# key for WT Forms CRF Token
app.config["SECRET_KEY"] = "639ded68629a54ac"
# SQLite development database // use PostgreSQL for production
app.config["SQLAlCHEMY_DATABASE_URI"] = "sqlite:////site.db"

db = SQLAlchemy(app)

from app_package import routes
