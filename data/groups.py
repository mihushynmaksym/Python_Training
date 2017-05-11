from model.group import Group
import random
import string
__author__ = 'Max'


testdata = [
    Group(name="name1",header="header1",footer="footer1"),  # constant for debug
    Group(name="name2",header="header2",footer="footer2")
           ]


# def random_string(prefix,maxlen):
#     symbols = string.ascii_letters + string.digits + ""*10  # have some issues with "spaces"
#     return prefix + " ".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
# testdata = [Group(name="", header="", footer="")] + \
#            [Group(name=random_string("name", 10),header=random_string("header", 20),footer=random_string("footer", 20))
#             for i in range(50)
#             ]


# testdata = [
#       Group(name=name, header=header, footer=footer)     //
#       for name in ["", random_string("name", 10)]        //
#       for header in ["", random_string("header", 20)]    //   list comprehension (pairwise)
#       for footer in ["", random_string("footer", 20)]    //
#       for i in range(5)                                  //
#            ]