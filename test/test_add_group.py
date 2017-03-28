# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="xzczx", header="sadwqe", footer="vbngt"))
    app.group.submit_creation()
    new_group = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_group)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    app.group.submit_creation()
    new_group = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_group)














