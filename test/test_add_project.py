from model.project import Project


def test_add_project(app, json_project, db):
    username = "administrator"
    password = "root"
    project = json_project
    old_projects = app.soap.get_project_list(username, password)
    app.project.add_project(project)
    new_projects = app.soap.get_project_list(username, password)
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
