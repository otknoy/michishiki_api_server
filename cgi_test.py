#!/usr/bin/env python

if __name__ == '__main__':
    import utils
    utils.cgi_header()
    
    data = {'a': 1, 'b': 2, 'c': 3}
    import json
    print json.dumps(data)

