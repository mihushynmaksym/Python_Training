__author__ = "Max"


from model.group import Group


def test_modify_group_name(app):
    app.session.login(user_name="admin", password="secret")
    app.group.modify_group_name(Group(name="changed group name",header=None,footer=None))
    app.group.submit_update()
    app.session.logout()


def test_modify_group_header(app):
   app.session.login(user_name="admin", password="secret")
   app.group.modify_group_header(Group(name=None,header="new header",footer=None))
   app.group.submit_update()
   app.session.logout()


def test_modify_group_footer(app):
   app.session.login(user_name="admin", password="secret")
   app.group.modify_group_footer(Group(name=None,header=None,footer="new footer"))
   app.group.submit_update()
   app.session.logout()
