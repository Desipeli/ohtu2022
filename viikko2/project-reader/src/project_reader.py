from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        import toml
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)
        parsettuToml = toml.loads(content)
        print(parsettuToml)
        print()
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(
            parsettuToml["tool"]["poetry"]["name"],
            parsettuToml["tool"]["poetry"]["description"],
            parsettuToml["tool"]["poetry"]["dependencies"],
            parsettuToml["tool"]["poetry"]["dev-dependencies"])
