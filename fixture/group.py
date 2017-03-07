__author__ = 'Max'


class GroupHelper:

    def __init__(self,app):
        self.app = app

    def submit_creation(self):
        wd = self.app.wd
        # submit
        wd.find_element_by_name("submit").click()
        # click return to home page
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        # initiate create group
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        # click submit
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def delete_first_group(self):
        # Login
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit delete
        wd.find_element_by_name("delete").click()
        # click return to home page
        wd.find_element_by_link_text("group page").click()

    def modify_group_name(self, group):
        # Login
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit edit
        wd.find_element_by_name("edit").click()
        # click field group name, clear field
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        # change group name
        wd.find_element_by_name("group_name").send_keys(group.name)

    def modify_group_header(self, group):
        # Login
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit edit
        wd.find_element_by_name("edit").click()
        # click field Group header, clear field
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        # change group header
        wd.find_element_by_name("group_header").send_keys(group.header)

    def modify_group_footer(self, group):
        # Login
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit edit
        wd.find_element_by_name("edit").click()
        # click field Group header, clear field
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        # change group footer
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def submit_update(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()






