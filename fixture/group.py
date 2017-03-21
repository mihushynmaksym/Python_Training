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

    def group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        # initiate create group
        self.group_page()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first_group(self):
        # select first group
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        # wd.find_element_by_link_text("group page").click()
        self.select_first_group()
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification form
        self.submit_update()
        wd.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        # Login
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit delete
        wd.find_element_by_name("delete").click()
        # click return to home page
        wd.find_element_by_link_text("group page").click()

    def submit_update(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    # Another way to test_modify_group
    # def modify_group_name(self, group):
    #     # Login
    #     wd = self.app.wd
    #     # select first group
    #     wd.find_element_by_name("selected[]").click()
    #     # submit edit
    #     wd.find_element_by_name("edit").click()
    #     # click field group name, clear field
    #     wd.find_element_by_name("group_name").click()
    #     wd.find_element_by_name("group_name").clear()
    #     # change group name
    #     wd.find_element_by_name("group_name").send_keys(group.name)

    # def modify_group_header(self, group):
    #     # Login
    #     wd = self.app.wd
    #     # select first group
    #     wd.find_element_by_name("selected[]").click()
    #     # submit edit
    #     wd.find_element_by_name("edit").click()
    #     # click field Group header, clear field
    #     wd.find_element_by_name("group_header").click()
    #     wd.find_element_by_name("group_header").clear()
    #     # change group header
    #     wd.find_element_by_name("group_header").send_keys(group.header)

    # def modify_group_footer(self, group):
    #     # Login
    #     wd = self.app.wd
    #     self.select_first_group()
    #     # submit edit
    #     wd.find_element_by_name("edit").click()
    #     # click field Group header, clear field
    #     wd.find_element_by_name("group_footer").click()
    #     wd.find_element_by_name("group_footer").clear()
    #     # change group footer
    #     wd.find_element_by_name("group_footer").send_keys(group.footer)








