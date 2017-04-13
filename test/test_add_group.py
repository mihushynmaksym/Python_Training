# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()  # Check lists + 1 (add group)
    group = Group(name="xzczx", header="sadwqe", footer="vbngt")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()  # Check lists + 1 (add group)
    new_group = app.group.get_group_list()  # Check lists + 1 (add group)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max) # assert lists


# def test_add_empty_group(app):
#     old_groups = app.group.get_group_list()  # Check lists + 1 (add group)
#     group = Group(name="", header="", footer="")
#     app.group.create(group)
#     new_group = app.group.get_group_list()  # Check lists + 1 (add group)
#     assert len(old_groups) + 1 == len(new_group)  # Check lists + 1 (add group)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max) # assert lists














