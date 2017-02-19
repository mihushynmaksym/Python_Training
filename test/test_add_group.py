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
    app.group.Create(Group(name="xzczx", header="sadwqe", footer="vbngt"))
    app.group.Submit_creation()
    app.session.Logout()


def test_add_empy_group(app):
    app.session.Login(user_name="admin", password="secret")
    app.group.Create(Group(name="", header="", footer=""))
    app.group.Submit_creation()
    app.session.Logout()













