#!/usr/bin/env python2

# install prerequisites
# pip install MySQL-python
# pip install requests
# pip install elasticsearch

import MySQLdb
import requests
from elasticsearch import Elasticsearch
from elasticsearch import helpers

mysql_host = "localhost"
mysql_user = "root"
mysql_password = "root"
mysql_database = "forum"

es_host = "localhost"
es_port = 9200
es_index = mysql_database + ""

# reset es
requests.delete("http://" + es_host + ":" + str(es_port) + "/_all")
es = Elasticsearch(["http://" + es_host + ":" + str(es_port)])
body = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    }
}
es.indices.create(index=es_index, body=body)

connection = MySQLdb.connect(
    host=mysql_host,
    user=mysql_user,
    passwd=mysql_password)

cursor = connection.cursor()
cursor.execute("USE " + mysql_database)
cursor.execute("SHOW TABLES")
cursor.fetchall()

for (table_name,) in cursor:
    print("==>Working on: " + table_name)

    table_cursor = connection.cursor()
    table_cursor.execute("SHOW columns FROM " + table_name)
    table_columns = [column[0] for column in table_cursor.fetchall()]
    print("Tables: " + str(table_columns))

    table_cursor.execute("SELECT * FROM " + table_name)
    bulk = []
    for record in table_cursor.fetchall():
        id = record[0]
        document = {
            "_index": es_index,
            "_type": table_name,
            "_id": id,
            "_source": {}
        }
        for i in range(1, len(record)):
            document["_source"][table_columns[i]] = record[i]
        bulk.append(document)
        if id % 25000 == 0:
            helpers.bulk(es, bulk)
            bulk = []
            print("Docs w/ id: {0} -> {1}".format(id - 25000, id))

    table_cursor.close()
    helpers.bulk(es, bulk)
    print("Done table: " + table_name)

cursor.close()
connection.close()
