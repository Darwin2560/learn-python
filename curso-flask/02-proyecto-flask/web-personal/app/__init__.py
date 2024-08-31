from app.projects.views import project
from app.views import base
from flask import Flask

app = Flask(__name__)
app.register_blueprint(base)
app.register_blueprint(project)
# from app import views
