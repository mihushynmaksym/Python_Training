__author__ = 'Max'

class SessionHelper:

    def __init__(self,app):
        self.app = app

    def login(self,user_name, password):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def find_group_button(self):
        wd = self.app.wd
        wd.find_element_by_text("group").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def is_login_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_login_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text == "(" + username + ")"

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_login_in():
            self.logout()

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_login_in():
            if self.is_login_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
