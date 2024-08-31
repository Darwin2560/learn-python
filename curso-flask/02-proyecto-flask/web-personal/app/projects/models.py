class Project:
    def __init__(self, title, description, github_url):
        self.title = title
        self.description = description
        self.github_url = github_url


p1 = Project(
    "Proyecto 1", "Descripción del proyecto 1", "https://github.com/Darwin2560"
)
p2 = Project(
    "Proyecto 2", "Descripción del proyecto 2", "https://github.com/Darwin2560"
)
p3 = Project(
    "Proyecto 3", "Descripción del proyecto 3", "https://github.com/Darwin2560"
)

PROJECTS = [p1, p2, p3]
