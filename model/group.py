__author__ = "Max"

from sys import maxsize


class Group:

    def __init__(self,name=None, header=None, footer=None, id=None):  # constructor for create groups (Header etc)
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.name, self.footer, self.header)  # add more info in console for debug (compare lists)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

