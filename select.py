#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import cgi
import sqlite3

DB_PATH = './data/michishiki.sqlite3'


def select():
    sql = u'select * from posts'

    con = sqlite3.connect(DB_PATH, isolation_level=None)
    cur = con.cursor()
    cur.execute(sql)
    result = [row for row in cur]
    con.close()
    return result

def format_result(result):
    keys = ['id', 'latitude', 'longitude', 'title', 'comment', 'posted_by', 'created_at']
    data = []
    for r in result:
        d = {}
        for k, v in zip(keys, r):
            d[k] = v
        data.append(d)
    return data
    
def cgi_header():
    print 'Content-Type: text/html'
    print
    
if __name__ == '__main__':
    result = select()
    data = format_result(result)

    cgi_header()
    import json
    print(json.dumps(data, indent=True, sort_keys=True))
