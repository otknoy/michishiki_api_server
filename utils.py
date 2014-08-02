def cgi_header():
    print 'Content-Type: text/html'
    print 'Access-Control-Allow-Origin: *'
    print

def fs2dict(fs):
    '''Field strage to dict'''
    params = {}
    for k in fs.keys():
        params[k] = fs[k].value
    return params
    
