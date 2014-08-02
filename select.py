#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import sqlite3

import config

def select(sql):
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

class SQLBuilder:
    def __init__(self):
        self.sql = u'select * from posts'
        self.condition = u''
        self.order = u''
        self.limit = -1

    def set_range_condition(self, lat1, lng1, lat2, lng2):
        lat_condition = '%f < latitude and latitude < %f' % (lat1, lat2)
        lng_condition = '%f < longitude and longitude < %f' % (lng1, lng2)
        self.condition = u'where %s and %s' % (lat_condition, lng_condition)

    def set_order(self, order_by, ascend=True):
        self.order = u'order by %s %s' % (order_by, ('asc' if ascend  else 'desc'))

    def set_limit(self, limit):
        self.limit = u'limit %d' % limit

    def build(self):
        sql = self.sql
        if self.condition != u'': sql += ' ' + self.condition
        if self.order != u'': sql += ' ' + self.order
        if self.limit >= 0: sql += ' ' + self.limit
        return sql

if __name__ == '__main__':
    builder = SQLBuilder()
    builder.set_range_condition(0, 0, 90, 150.2)
    builder.set_order(order_by='created_at', ascend=False)
    builder.set_limit(limit=1)
    sql = builder.build()
    print sql

    result = select(sql)

    import utils
    utils.cgi_header()
    
    import json
    print json.dumps(result, indent=True, sort_keys=True)
