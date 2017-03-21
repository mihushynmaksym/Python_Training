__author__ = 'Max'

from selenium import webdriver
from fixture.sesion import SessionHelper
from fixture.group import GroupHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome("D:\Chromedriver\chromedriver")
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

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