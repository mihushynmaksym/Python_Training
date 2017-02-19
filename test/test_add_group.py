# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.Login(user_name="admin", password="secret")
    app.Create_group(Group(name="xzczx", header="sadwqe", footer="vbngt"))
    app.Submit_group_creation()
    app.session.Logout()


def test_add_empy_group(app):
    app.session.Login(user_name="admin", password="secret")
    app.Create_group(Group(name="", header="", footer=""))
    app.Submit_group_creation()
    app.session.Logout()













