__author__ = 'Max'
from model.group import Group


def test_add_group(app):
    app.group.find_group_button() # find button "group" on the page
    old_groups = app.group.get_group_list()  # Check lists + 1 (add group)
    group = Group(name="xzczx", header="sadwqe", footer="vbngt")
    app.group.create(group) # init create group
    assert len(old_groups) + 1 == app.group.count()  # Check lists + 1 (add group) hesh
    new_group = app.group.get_group_list()  # Check lists + 1 (add group)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max) # assert lists


def test_add_empty_group(app):
    app.group.find_group_button() # find button "group" on the page
    old_groups = app.group.get_group_list()  # Check lists + 1 (add group)
    group = Group(name="", header="", footer="")
    app.group.create(group) # init create group
    assert len(old_groups) + 1 == app.group.count()  # Check lists + 1 (add group) hesh
    new_group = app.group.get_group_list()  # Check lists + 1 (add group)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max) # assert lists













