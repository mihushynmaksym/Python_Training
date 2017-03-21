__author__ = 'Max'


from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
       app.group.create(Group(name="xzczx", header="sadwqe", footer="vbngt"))
       app.group.submit_creation()
    app.group.delete_first_group()