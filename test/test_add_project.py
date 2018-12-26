
def test_add_project(app, json_project, db):
    project = json_project
    old_projects = db.get_project_list()
    app.project.add_project(project)
    new_projects = db.get_project_list()
    old_projects.append(project)
    assert old_projects == new_projects

