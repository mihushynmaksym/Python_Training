__author__ = 'Max'


import pytest
from fixture.application import Application


@pytest.fixture #(scope="session") нужно найти решение (уходит в логаут только если юзать тесты по одному)
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture