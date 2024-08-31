from flask import render_template, Blueprint
from app.projects.models import PROJECTS

project = Blueprint('project', __name__)

@project.route('/index')
def index():
    return render_template('project_templates/index.html', projects=PROJECTS)