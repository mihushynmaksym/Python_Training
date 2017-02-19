# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.Login(user_name="admin", password="secret")
    app.group.Create(Group(name="xzczx", header="sadwqe", footer="vbngt"))
    app.group.Submit_creation()
    app.session.Logout()


def test_add_empy_group(app):
    app.session.Login(user_name="admin", password="secret")
    app.group.Create(Group(name="", header="", footer=""))
    app.group.Submit_creation()
    app.session.Logout()













