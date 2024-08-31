from flask import Flask
from app.views import base
from app.projects.views import project

app = Flask(__name__)
app.register_blueprint(base)
app.register_blueprint(project)
# from app import views
