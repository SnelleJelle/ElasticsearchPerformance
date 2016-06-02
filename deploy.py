#!/usr/bin/env python2

import MySQLdb

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

with open("structure.sql") as f:
    sql = "".join(f.readlines())

cursor.execute(sql)
connection.close()
