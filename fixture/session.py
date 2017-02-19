__author__ = 'Max'


class SessionHelper:

    def __init__(self,app):
        self.app = app

    def Login(self,user_name, password):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/group.php")
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def Logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()