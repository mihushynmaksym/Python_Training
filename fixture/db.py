import mysql.connector
from model.group import Group


class DbFixture:

    def __init__(self, host,name,user,password):
       self.host = host
       self.name = name
       self.user = user
       self.password = password
       self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)

    def destroy(self):
        self.connection.close()

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_header, group_footer, group_id From group_list")
            for row in cursor:
                (id,name,header,footer) = row
                list.append(Group(id=id,name=name,header=header,footer=footer))
        finally:
            cursor.close()
        return list
    
