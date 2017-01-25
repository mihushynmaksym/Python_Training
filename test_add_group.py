# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add_group(self):
        success = True
        wd = self.wd
        self.Open_home_page(wd)
        self.Login(wd, user_name="admin", password="secret")
        self.Open_group_page(wd)
        self.Fill_group_form(wd, name="xzczx", header="sadwqe", footer="vbngt")
        self.Submit_group_creation(wd)
        self.Logout(success, wd)

    def test_add_empy_group(self):
        success = True
        wd = self.wd
        self.Open_home_page(wd)
        self.Login(wd, user_name="admin", password="secret")
        self.Open_group_page(wd)
        self.Fill_group_form(wd, name="", header="", footer="")
        self.Submit_group_creation(wd)
        self.Logout(success, wd)

    def Logout(self, success, wd):
        wd.find_element_by_link_text("Logout").click()


    def Submit_group_creation(self, wd):
        wd.find_element_by_name("submit").click()
        self.Return_to_group_creation(wd)

    def Return_to_group_creation(self, wd):
        wd.find_element_by_link_text("group page").click()

    def Fill_group_form(self, wd, name, header, footer):
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(footer)

    def Open_group_page(self, wd):
        wd.find_element_by_name("new").click()

    def Login(self, wd, user_name, password):
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def Open_home_page(self, wd):
        wd.get("http://localhost/addressbook/group.php")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
