__author__ = 'Max'


def test_delete_first_group(app):
    app.group.if_not_group_create_group() # if not have any groups = create group
    old_groups = app.group.get_group_list()  # Check lists - 1 (delete group)
    app.group.delete_first_group()
    new_group = app.group.get_group_list()  # Check lists - 1 (delete group)
    assert len(old_groups) - 1 == len(new_group)  # Check lists - 1 (delete group)
    old_groups[0:1] = []  # Check lists - 1 (delete group)
    assert old_groups == new_group  # Check lists - 1 (delete group)


