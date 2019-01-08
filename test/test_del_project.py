from model.project import Project
import random


def test_del_project(app, db):
    username = "administrator"
    password = "root"
    if len(app.soap.get_project_list(username, password)) == 0:
        app.project.add_project(Project(name="project 111", status="development", view_status="public", description="description project 111"))
    old_projects = app.soap.get_project_list(username, password)
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = app.soap.get_project_list(username, password)
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert old_projects == new_projects
