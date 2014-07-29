#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import sqlite3

import config

def select():
    sql = u'select * from posts'

    con = sqlite3.connect(config.db_path, isolation_level=None)
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
    
if __name__ == '__main__':
    results = select()
    data = results2dict(results)

    import utils
    utils.cgi_header()
    
    import json
    print json.dumps(data, indent=True, sort_keys=True)
