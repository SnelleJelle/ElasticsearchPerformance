#!/usr/bin/env python2

from elasticsearch import Elasticsearch
import time

es_host = "localhost"
es_port = 9200
es_index = "forum"
es_type = "users"

es = Elasticsearch(["http://" + es_host + ":" + str(es_port)])

term = "turbo"
term = "*" + term + "*"

body = {
    "size": 10000,
    "query":
        {"query_string": {"query": term}}
}

total = 0
runs = 100
for i in range(0, runs - 1):
    before = time.time()
    search = es.search(index=es_index, doc_type=es_type, body=body)
    after = time.time()
    elapsed_millis = (after - before) * 1000
    print("Elapsed: " + str(elapsed_millis))
    total += elapsed_millis

    print("Count(results): " + str(len(search["hits"]["hits"])))
    print("On attempt: " + str(i))

average = total / runs
print("Elasticsearch Average(milliseconds): \t" + str(average))
