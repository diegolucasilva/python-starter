import redis
import json

JSON_CONNECTIONS = '[{"host": "localhost", "port":"6379", "db":"0"},{"host": "localhost", "port":"6379", "db":1}]'
#connections = [{'host': 'localhost', 'port':6379, 'db':0},{'host': 'localhost', 'port':6379, 'db':1}]
connections = json.loads(JSON_CONNECTIONS)
CHUNK_SIZE = 2

def scanClean():
    for connection in connections:
        print(connection)
        cache = redis.Redis(host=connection['host'], port=connection['port'],db=connection['db'])
        mock()
        clean("*", cache, connection)

def clean(pattern, cache, connection):
    cursor = '0'
    deleted_count = 0
    while cursor != 0:
        cursor, keys = cache.scan(cursor=cursor, match=pattern, count=CHUNK_SIZE)
        if keys:
            deleted_count += cache.delete(*keys)
    
    cache.close()
    print('{} registries deleted from: {} DB {}'.format(deleted_count,connection['host'],connection['db']))

def mock():
    cache = redis.Redis(host='localhost', port=6379,db=0)
    for key, value in (('A', '1'), ('B', '2'), ('C', '3'),('D', '3')):
        cache.set(key, value)

    cache2 = redis.Redis(host='localhost', port=6379,db=1)
    for key, value in (('F', '1'),('G', '1')):
        cache2.set(key, value)

scanClean()