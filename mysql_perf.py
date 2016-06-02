#!/usr/bin/env python2

import MySQLdb
import time

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

term = "turbo"

sql = """
SELECT * FROM {0}
WHERE
firstname LIKE "%{1}%" OR
lastname LIKE "%{1}%" OR
username LIKE "%{1}%" OR
email LIKE "%{1}%;"
""".format(mysql_table, term)

total = 0
cursor.execute("USE " + mysql_database)
runs = 100
for i in range(0, runs - 1):
    before = time.time()
    cursor.execute(sql)
    after = time.time()
    elapsed_millis = (after - before) * 1000
    print("Elapsed: " + str(elapsed_millis))
    total += elapsed_millis

    print("Count(results): " + str(len(cursor.fetchall())))
    print("On attempt: " + str(i))

average = total / runs
print("MySql Average(milliseconds): \t\t\t" + str(average))
connection.close()
