#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import sqlite3
import time

import config

def valid(qs):
    required_keys = ['title', 'comment', 'posted_by', 'localite', 'latitude', 'longitude']
    return all([qs.has_key(k) for k in required_keys])

def post(title, comment, posted_by, localite, latitude, longitude):
    rate = 0
    created_at = int(time.time())
    updated_at = created_at

    sql = u'insert into posts (id, title, comment, posted_by, localite, rate, latitude, longitude, created_at, updated_at) values (null,?,?,?,?,?,?,?,?,?);'

    con = sqlite3.connect(config.db_path, isolation_level=None)
    con.execute(sql, (title, comment, posted_by, localite, rate, latitude, longitude, created_at, updated_at))
    con.close()

    
if __name__ == '__main__':
    import utils

    qs = utils.fs2dict(cgi.FieldStorage())

    if valid(qs):
        keys = ['title', 'comment', 'posted_by', 'localite', 'latitude', 'longitude']
        query_string = [qs[k].decode('utf-8') for k in keys]
        post(*query_string)
        result = '{"message": "Successfully posted!"}'
    else:
        result = '{"message": "Invalid query string"}'

    utils.cgi_header()
    print result
