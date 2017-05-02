__author__ = 'Max'
from model.group import Group
import pytest
import random
import string


def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits + ""*10  # have some issues with "spaces"
    return prefix + " ".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(name="", header="", footer="")] + \
           [Group(name=random_string("name", 10),header=random_string("header", 20),footer=random_string("footer", 20))
            for i in range(50)
            ]


# testdata = [
#       Group(name=name, header=header, footer=footer)     //
#       for name in ["", random_string("name", 20)]        //
#       for header in ["", random_string("header", 20)]    //   list comprehension
#       for footer in ["", random_string("footer", 20)]    //
#       for i in range(5)                                  //
#            ]
#
#
@pytest.mark.parametrize("group", testdata, ids = [repr(x) for x in testdata])  # python bug with (x).
def test_add_group(app,group):
    app.group.find_group_button() # find button "group" on the page
    old_groups = app.group.get_group_list()  # Check lists + 1 (add group)
    app.group.create(group)  # init create group
    assert len(old_groups) + 1 == app.group.count()  # Check lists + 1 (add group) hesh
    new_group = app.group.get_group_list()  # Check lists + 1 (add group)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max) # assert lists


# def test_add_empty_group(app):
#     app.group.find_group_button() # find button "group" on the page
#     old_groups = app.group.get_group_list()  # Check lists + 1 (add group)
#     group = Group(name="cc ccc ", header="aa aa", footer="www ww")
#     app.group.create(group) # init create group
#     assert len(old_groups) + 1 == app.group.count()  # Check lists + 1 (add group) hesh
#     new_group = app.group.get_group_list()  # Check lists + 1 (add group)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max) # assert lists