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
    results = [row for row in cur]
    con.close()
    return results

def format_result(result):
    d = {}
    d['id']         = result[0]
    d['latitude']   = result[1]
    d['longitude']  = result[2]
    d['title']      = result[3]
    d['comment']    = result[4]
    d['posted_by']  = result[5]
    d['created_at'] = result[6]
    return d

def results2dict(results):
    data = []
    for r in results:
        data.append(format_result(r))
    return data
    
def cgi_header():
    print 'Content-Type: application/json'
    print 'Access-Control-Allow-Origin: *'
    print ''
    
if __name__ == '__main__':
    results = select()
    data = results2dict(results)

    cgi_header()
    import json
    print json.dumps(data, indent=True, sort_keys=True)
