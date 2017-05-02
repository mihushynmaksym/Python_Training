__author__ = 'Max'
from random import randrange


# def test_delete_some_group(app):
#         app.group.find_group_button() # find button "group" on the page
#         app.group.if_not_group_create_group() # if not have any groups = create group
#         old_groups = app.group.get_group_list()  # Check lists - 1 (delete group)
#         index =(len(old_groups))  # add random for delete groups
#         app.group.delete_group_by_index(index)  # add random for delete groups
#         new_group = app.group.get_group_list()  # Check lists - 1 (delete group)
#         assert len(old_groups) - 1 == len(new_group)  # Check lists - 1 (delete group)
#         old_groups[index:index + 1] = []  # Check lists - 1 (delete group), add random for delete groups
#         assert old_groups == new_group  # Check lists - 1 (delete group)


def test_delete_some_group(app):
        app.group.find_group_button() # find button "group" on the page
        app.group.if_not_group_create_group() # if not have any groups = create group
        old_groups = app.group.get_group_list()  # Check lists - 1 (delete group)
        index = randrange(len(old_groups))  # add random for delete groups
        app.group.delete_group_by_index(index)  # add random for delete groups
        new_group = app.group.get_group_list()  # Check lists - 1 (delete group)
        assert len(old_groups) - 1 == len(new_group)  # Check lists - 1 (delete group)
        old_groups[index:index + 1] = []  # Check lists - 1 (delete group), add random for delete groups
        assert old_groups == new_group  # Check lists - 1 (delete group)

