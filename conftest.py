
import os.path
import pytest
import json
from selenium import webdriver
from fixture.sesion import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
import importlib
import jsonpickle
__author__ = 'Max'


fixture = None
target = None


@pytest.fixture(scope="session", autouse=True) # run all tests in one session
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:  # set up permanent default directory for work
            target = json.load(f)
    if fixture is None or fixture.is_valid():
        fixture = Application(browser,base_url=target["baseUrl"])
    fixture.session.ensure_login(username=target["username"], password=target["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)  # run all tests in one session
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    # hooks for browsers
    parser.addoption("--browser",action="store",default="chrome")
    # hooks for links
    parser.addoption("--target",action="store",default="target.json")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata=load_form_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids = [str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_form_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids = [str(x) for x in testdata])

def load_form_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_form_json(file):
    # find dir with JSON file and read
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())


class Application:

    def __init__(self,browser,base_url):
        # hooks for browsers (additional options) default = "chrome"
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "IE":
            self.wd = webdriver.Ie()
        elif browser == "Opera":
            self.wd = webdriver.Opera()
        elif browser == "Edge":
            self.wd = webdriver.Edge()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        # self.wd.implicitly_wait(5) Delay timer for dynamic web pages
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def submit_group_creation(self):
        wd = self.wd
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()

    def create_group(self,group):
        wd = self.wd
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
