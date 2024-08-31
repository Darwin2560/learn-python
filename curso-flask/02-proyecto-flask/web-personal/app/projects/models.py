from app import db


class Project(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    github_url = db.Column(db.String(255))

    def __init__(self, title, description, github_url):
        self.title = title
        self.description = description
        self.github_url = github_url

    def __repr__(self):
        return f"<Project {self.title}>"
