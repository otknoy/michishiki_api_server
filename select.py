#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import sqlite3

import config

def select():
    sql = u'select * from posts'
    conn = sqlite3.connect(config.db_path, isolation_level=None)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(sql)
    results = rows2dict(cur.fetchall())
    conn.close()
    return results

def rows2dict(rows):
    '''list of sqlite3.Row to dict'''
    return [dict(zip(r.keys(), r)) for r in rows]


if __name__ == '__main__':
    result = select()

    import utils
    utils.cgi_header()
    
    import json
    print json.dumps(result, indent=True, sort_keys=True)
