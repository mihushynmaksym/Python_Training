__author__ = "Max"


from model.group import Group


def test_modify_group_name(app):
    app.session.Login(user_name="admin", password="secret")
    app.group.modify_group_name(Group(name="changed group name",header=None,footer=None))
    app.group.submit_update()
    app.session.Logout()


def test_modify_group_header(app):
   app.session.Login(user_name="admin", password="secret")
   app.group.modify_group_header(Group(name=None,header="new header",footer=None))
   app.group.submit_update()
   app.session.Logout()


def test_modify_group_footer(app):
   app.session.Login(user_name="admin", password="secret")
   app.group.modify_group_footer(Group(name=None,header=None,footer="new header"))
   app.group.submit_update()
   app.session.Logout()
