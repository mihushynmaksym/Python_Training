
import os.path
import pytest
import json
from selenium import webdriver
from fixture.sesion import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
import importlib
import jsonpickle
import mysql.connector
from model.group import Group

__author__ = 'Max'


fixture = None
target = None


@pytest.fixture(scope="session") # run all tests in one session
def app(request):
    global fixture
    web_config = load_config(request.config.getoption("--target"))['web']
    browser = request.config.getoption("--browser")
    if fixture is None or fixture.is_valid():
        fixture = Application(browser,base_url=web_config["baseUrl"])
    fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    return fixture

@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config['host'],name=db_config['name'], user=db_config['user'],
                          password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture



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

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),file )
        with open(config_file) as f:  # set up permanent default directory for work
            target = json.load(f)
    return target

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

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)

    def destroy(self):
        self.connection.close()

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id,name,header,footer) = row
                list.append(Group(id=str(id),name=name,header=header,footer=footer))
        finally:
            cursor.close()
        return list