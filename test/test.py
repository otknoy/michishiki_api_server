#!/usr/bin/env python
import sys
import os

# add '../' directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


if __name__ == '__main__':
    import config
    config.db_path = '../data/michishiki.sqlite3'

    from get_post import SQLBuilder
    from get_post import select

    b = SQLBuilder()
    b.set_range_condition(-74, -18, 52, -61)
    print b.build()
    print len(select(b.build()))

    b = SQLBuilder()
    b.set_range_condition(-74, -33, 52, -75)
    print b.build()
    print len(select(b.build()))
