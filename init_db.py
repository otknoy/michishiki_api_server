#!/usr/bin/env python
import sqlite3

def create_db(sql, filename):
    con = sqlite3.connect(filename, isolation_level=None)
    con.execute(sql)
    con.close()

if __name__ == '__main__':
    sql = u'''create table posts (
  id integer primary key autoincrement,
  latitude real,
  longitude real,
  title text,
  comment text,
  posted_by text,
  created_at integer
);
'''
    import config    
    create_db(sql, config.db_path)
