from app.projects.views import project
from app.views import base
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# configuration APP
app.config.from_object("config.DevelopmentConfig")

db = SQLAlchemy(app)

app.register_blueprint(base)
app.register_blueprint(project)
# from app import views

# create database and tables
with app.app_context():
    db.create_all()
