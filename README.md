michishiki_api_server
=====================

# Setup

1. Create empty database
 * run init script: `./init_db.py`
 * and then `./data/michishiki.sqlite3' generated.
2. Change permission
 * `data/` directory and `data/michishiki.sqlite3`
 * `chmod 777 data/; chmod 777 data/michishiki.sqlite3`

# API reference
 
## post.py

* required keys
 * posted_by
 * title
 * comment
 * localite
 * latitude
 * longitude


## select.py

* Filter by map range
 * lat1, lng1: northwest end point latitude and longitude on a map
 * lat2, lng2: southeast end point latitude and longitude on a map
* Order by *
 * order_by: specify row name
 * order: *ascend* or *descend*
* Limitation
 * limit: number of returned items
* sample query
 * http://localhost/michishiki_api_server/select.py?lat1=0&lng1=0&lat2=90&lng2=180&order_by=latitude&order=ascend&limit=3
