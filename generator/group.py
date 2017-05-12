from model.group import Group
import random
import string
import os.path
import jsonpickle  # framework for write and read JSON file
import getopt
import sys
__author__ = 'Max'


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5                   # additional parametr -n 10 (where 10 = 11 random generate test data for group)
f = "data/groups.json"  # additional parametr - f "here fie name"(some file name by defaul groups.json)

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix,maxlen):
    # have some issues with "spaces"
    # if add method + string.punctuation we can find bugs with '  symbols.
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(name="", header="", footer="")] + \
           [Group(name=random_string("name", 10),header=random_string("header", 20),footer=random_string("footer", 20))
            for i in range(n)
            ]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file,'w') as out:
    jsonpickle.set_encoder_options("json", indent=2) # intend 2 = formating at groups.js
    out.write(jsonpickle.encode(testdata))