from app import db
from app.projects.models import Project
from flask import Blueprint, redirect, render_template, request, url_for

project = Blueprint("project", __name__)


@project.route("/projects/index")
def index():
    projects = Project.query.all()
    db.session.commit()
    return render_template("project_templates/index.html", projects=projects)


@project.route("/projects/create")
def create():
    return render_template("project_templates/create.html")


@project.route("/projects/insert", methods=["POST"])
def insert():
    title = request.form.get("title")
    description = request.form.get("description")
    github_url = request.form.get("github_url")

    project = Project(title, description, github_url)
    db.session.add(project)
    db.session.commit()

    return redirect(url_for("project.index"))


@project.route("/projects/edit/<int:id>")
def edit(id):
    project = Project.query.get_or_404(id)
    return render_template("project_templates/edit.html", project=project)


@project.route("/projects/update/<int:id>", methods=["POST"])
def update(id):
    project = Project.query.get_or_404(id)
    project.title = request.form.get("title")
    project.description = request.form.get("description")
    project.github_url = request.form.get("github_url")

    db.session.add(project)
    db.session.commit()

    return redirect(url_for("project.index"))


@project.route("/projects/delete/<int:id>")
def delete(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()

    return redirect(url_for("project.index"))
