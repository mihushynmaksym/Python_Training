__author__ = 'Max'

import pytest
from fixture.application import Application


@pytest.fixture(scope="session")# run all tests in one session
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

