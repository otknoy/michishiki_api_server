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
    required_keys = ['title', 'comment', 'posted_by', 'latitude', 'longitude']
    return all([qs.has_key(k) for k in required_keys])

def post(title, comment, posted_by, latitude, longitude):
    rate = 0
    created_at = int(time.time())
    updated_at = created_at

    sql = u'insert into posts (id, title, comment, posted_by, rate, latitude, longitude, created_at, updated_at) values (null,?,?,?,?,?,?,?,?);'

    con = sqlite3.connect(config.db_path, isolation_level=None)
    con.execute(sql, (title, comment, posted_by, rate, latitude, longitude, created_at, updated_at))
    con.close()

    
if __name__ == '__main__':
    qs = fs2dict(cgi.FieldStorage())

    keys = ['title', 'comment', 'posted_by', 'latitude', 'longitude']
    if valid(qs):
        query_string = [qs[k].decode('utf-8') for k in keys]
        post(*query_string)
        result = '{"message": "Successfully posted!"}'
    else:
        result = '{"message": "Invalid query string"}'

    import utils
    utils.cgi_header()
    print result
