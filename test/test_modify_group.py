__author__ = "Max"

from model.group import Group
from random import randrange


def test_modify_group_name(app):
    app.group.find_group_button() # find button "group" on the page
    app.group.if_not_group_create_group()  # if not have any groups = create group
    old_groups = app.group.get_group_list()  # Check lists == 0(modify group)
    index = randrange(len(old_groups))  # add random for modify group
    group = (Group(name="New group"))
    group.id = old_groups[index].id  # save ID for assert = 0
    app.group.modify_group_by_index(index, group)  # add random for modify group
    new_group = app.group.get_group_list()  # Check lists == 0(modify group)
    assert len(old_groups) == len(new_group)  # Check lists == 0(modify group)
    old_groups[index] = group  # save ID for assert = 0
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)  # assert lists


# def test_modify_group_header(app):
#     app.group.if_not_group_create_group()  # if not have any groups = create group
#     old_groups = app.group.get_group_list()  # Check lists == 0(modify group)
#     index = randrange(len(old_groups))
#     group = (Group(header="New header"))
#     group.id = old_groups[index].id  # save ID for assert = 0
#     app.group.modify_group_by_index(index, group)
#     new_group = app.group.get_group_list()  # Check lists == 0(modify group)
#     assert len(old_groups) == len(new_group)  # Check lists == 0(modify group)
#     old_groups[index] = group  # save ID for assert = 0
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)  # assert lists
#
#
# def test_modify_group_footer(app):
#     app.group.if_not_group_create_group()  # if not have any groups = create group
#     old_groups = app.group.get_group_list()  # Check lists == 0(modify group)
#     index = randrange(len(old_groups))
#     group = (Group(footer="New footer"))
#     group.id = old_groups[index].id  # save ID for assert = 0
#     app.group.modify_group_by_index(index, group)
#     new_group = app.group.get_group_list()  # Check lists == 0(modify group)
#     assert len(old_groups) == len(new_group)  # Check lists == 0(modify group)
#     old_groups[index] = group  # save ID for assert = 0
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)  # assert lists

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
