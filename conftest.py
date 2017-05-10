
import pytest
import json
from selenium import webdriver
from fixture.sesion import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
__author__ = 'Max'


fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        with open(request.config.getoption("--target")) as config_file:
            target = json.load(config_file)
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


class Application:

    def __init__(self,browser,base_url):
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


