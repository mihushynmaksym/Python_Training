# -*- coding: utf-8 -*-
from group import Group
from application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add__group(app):
    app.Login(user_name="admin", password="secret")
    app.Create_group(Group(name="xzczx", header="sadwqe", footer="vbngt"))
    app.Submit_group_creation()
    app.Logout()

def test_add_empy_group(app):
    app.Login(user_name="admin", password="secret")
    app.Create_group(Group(name="", header="", footer=""))
    app.Submit_group_creation()
    app.Logout()













