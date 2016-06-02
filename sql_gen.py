#!/usr/bin/env python2

import MySQLdb

total_runs = 5000

mysql_host = "localhost"
mysql_user = "root"
mysql_password = "root"
mysql_database = "forum"
mysql_table = "users"

connection = MySQLdb.connect(
    host=mysql_host,
    user=mysql_user,
    passwd=mysql_password)

cursor = connection.cursor()
cursor.execute("USE " + mysql_database)
cursor.execute("TRUNCATE " + mysql_table)


class Generator:
    def __init__(self):
        self.__count = 0
        with open("words.txt") as f:
            self.__content = f.read().splitlines()
            self.__max = len(self.__content)

    def get_value(self):
        self.__count = (self.__count + 1) % self.__max
        return self.__content[self.__count]

    def firstname(self):
        return self.get_value()

    def lastname(self):
        return self.get_value()

    def username(self):
        return self.get_value()

    def email(self):
        return self.get_value() + "." + self.get_value() + "@" + self.get_value() + ".com"


gen = Generator()

sub_routines = int(total_runs / 1000)
for r in range(0, sub_routines):

    sql = "INSERT INTO " + mysql_table + " (`firstname`, `lastname`, `username`, `email`) VALUES "
    for i in range(0, 999):
        sql += "('{}','{}','{}','{}'), ".format(gen.firstname(), gen.lastname(), gen.username(), gen.email())
    sql += "('{}','{}','{}','{}')".format(gen.firstname(), gen.lastname(), gen.username(), gen.email())

    cursor.execute(sql)
    connection.commit()
    print("Posted 1000 records on routine: " + str(r))

connection.close()

execfile("bulk_migrate.py")
