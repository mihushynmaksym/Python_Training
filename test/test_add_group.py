
from model.group import Group

__author__ = 'Max'



def test_add_group(app,data_groups):
    group = data_groups
    app.group.find_group_button() # find button "group" on the page
    old_groups = app.group.get_group_list()  # Check lists + 1 (add group)
    app.group.create(group)  # init create group
    assert len(old_groups) + 1 == app.group.count()  # Check lists + 1 (add group) hesh
    new_group = app.group.get_group_list()  # Check lists + 1 (add group)
    old_groups.append(group) # add group for old_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max) # assert lists

