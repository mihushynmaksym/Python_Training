__author__ = "Max"

from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="xzczx", header="sadwqe", footer="vbngt"))
        app.group.submit_creation()
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="New group"))
    new_group = app.group.get_group_list()
    assert len(old_groups) == len(new_group)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="xzczx", header="sadwqe", footer="vbngt"))
        app.group.submit_creation()
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New header"))
    new_group = app.group.get_group_list()
    assert len(old_groups) == len(new_group)


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="xzczx", header="sadwqe", footer="vbngt"))
        app.group.submit_creation()
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(footer="New footer"))
    new_group = app.group.get_group_list()
    assert len(old_groups) == len(new_group)

# Another way to test_modify_group
# def test_modify_group_name(app):
#     app.session.login(user_name="admin", password="secret")
#     app.group.modify_group_name(Group(name="changed group name",header=None,footer=None))
#     app.group.submit_update()
#     app.session.logout()
#
#
# def test_modify_group_header(app):
#    app.session.login(user_name="admin", password="secret")
#    app.group.modify_group_header(Group(name=None,header="new header",footer=None))
#    app.group.submit_update()
#    app.session.logout()
#
#
# def test_modify_group_footer(app):
#    app.session.login(user_name="admin", password="secret")
#    app.group.modify_group_footer(Group(name=None,header=None,footer="new footer"))
#    app.group.submit_update()
#    app.session.logout()
