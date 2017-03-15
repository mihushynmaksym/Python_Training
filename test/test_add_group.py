# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(user_name="admin", password="secret")
    app.group.create(Group(name="xzczx", header="sadwqe", footer="vbngt"))
    app.group.submit_creation()
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(user_name="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.group.submit_creation()
    app.session.logout()













