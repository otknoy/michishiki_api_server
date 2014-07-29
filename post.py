#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import sqlite3
import time

import config


def fs2dict(fs):
    '''Field strage to dict'''
    params = {}
    for k in fs.keys():
        params[k] = fs[k].value
    return params

def valid(qs):
    required_keys = ['latitude', 'longitude', 'title', 'comment', 'posted_by']
    return all([qs.has_key(k) for k in required_keys])

def post(latitude, longitude, title, comment, posted_by):
    created_at = int(time.time())
    sql = u'insert into posts (id, latitude, longitude, title, comment, posted_by, created_at) values (null,?,?,?,?,?,?);'

    con = sqlite3.connect(db_path, isolation_level=None)
    con.execute(sql, (latitude, longitude, title, comment, posted_by, created_at))
    con.close()

    
if __name__ == '__main__':
    qs = fs2dict(cgi.FieldStorage())

    if valid(qs):
        query_string = [qs[k].decode('utf-8') for k in ['latitude', 'longitude', 'title', 'comment', 'posted_by']]
        post(*query_string)
        result = '{"message": "Successfully posted!"}'
    else:
        result = '{"message": "Invalid query string"}'

    import utils
    utils.cgi_header()
    print result
