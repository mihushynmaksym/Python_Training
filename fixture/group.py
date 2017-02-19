__author__ = 'Max'



class GroupHelper:

    def __init__(self,app):
        self.app = app

    def Submit_creation(self):
        wd = self.app.wd
        #submit
        wd.find_element_by_name("submit").click()
        # click return to home page
        wd.find_element_by_link_text("group page").click()

    def Create(self, group):
        wd = self.app.wd
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


    def delete_first_group(self):
        #Login
        wd = self.app.wd
        #select first group
        wd.find_element_by_name("selected[]").click()
        #submit deletion
        wd.find_element_by_name("delete").click()
        #click return to home page
        wd.find_element_by_link_text("group page").click()
