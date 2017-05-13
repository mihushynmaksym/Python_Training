from model.group import Group

__author__="Max"


def test_group_list(app, db):
    app.group.find_group_button()
    ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())  # delete spaces in DB for assert
    db_list=map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

