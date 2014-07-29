#!/usr/bin/env python
import sqlite3

def create_db(sql, filename):
    con = sqlite3.connect(filename, isolation_level=None)
    con.execute(sql)
    con.close()

if __name__ == '__main__':
    sql = open('data/import.sql').read()
    import config    
    create_db(sql, config.db_path)
