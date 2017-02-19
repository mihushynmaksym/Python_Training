__author__ = 'Max'


def test_delete_first_group(app):
    app.session.Login(user_name="admin", password="secret")
    app.group.delete_first_group()
    app.session.Logout()