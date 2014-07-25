#!/usr/bin/env python
import sqlite3

def cgi_header():
    print 'Content-Type: text/html'
    print

def init_db(path):
    con = sqlite3.connect('db/michishiki.sqlite3')
    sql = u"""
"""
    

if __name__ == '__main__':
    import cgitb
    cgitb.enable()

    cgi_header()
    
    data = {'a': 1, 'b': 2, 'c': 3}

    import json
    print json.dumps(data)

