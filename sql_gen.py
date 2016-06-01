import MySQLdb
from itertools import product

mysql_host = "localhost"
mysql_user = "root"
mysql_password = "root"
mysql_database = "forum"

connection = MySQLdb.connect(
    host=mysql_host,
    user=mysql_user,
    passwd=mysql_password)

cursor = connection.cursor()
cursor.execute("USE " + mysql_database)
cursor.execute("TRUNCATE `forum`.`users`")


class Generator:
    def __init__(self):
        self.__chars = "abcdefghijklmnopqrstuvwxyz"
        self.__extended_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.__iter = product(self.__chars, repeat=25)

    def get_value(self):
        return "".join(next(self.__iter))

    def firstname(self):
        return self.get_value()

    def lastname(self):
        return self.get_value()

    def username(self):
        return self.get_value()

    def email(self):
        return self.get_value() + "." + self.get_value() + "@" + self.get_value() + ".com"


gen = Generator()

total_runs = 10000
sub_routines = total_runs / 1000
for r in range(0, sub_routines):

    sql = "INSERT INTO `users` (`firstname`, `lastname`, `username`, `email`) VALUES "
    for i in range(0, 999):
        sql += "('{}','{}','{}','{}'), ".format(gen.firstname(), gen.lastname(), gen.username(), gen.email())
    sql += "('{}','{}','{}','{}')".format(gen.firstname(), gen.lastname(), gen.username(), gen.email())

    cursor.execute(sql)
    connection.commit()
    print("Posted 1000 records on routine: " + str(r))

connection.close()
