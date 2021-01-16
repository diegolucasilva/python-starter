import redis
import json

JSON_CONNECTIONS = '[{"host": "localhost", "port":"6379", "db":"0"},{"host": "localhost", "port":"6379", "db":1}]'
#connections = [{'host': 'localhost', 'port':6379, 'db':0},{'host': 'localhost', 'port':6379, 'db':1}]
connections = json.loads(JSON_CONNECTIONS)
CHUNK_SIZE = 2

def scanClean():
    for connection in connections:
        print(connection)
        client = redis.Redis(host=connection['host'], port=connection['port'],db=connection['db'])
        mock()
        clean("*", client, connection)

def clean(pattern, client, connection):
    cursor = '0'
    deleted_count = 0
    while cursor != 0:
        cursor, keys = client.scan(cursor=cursor, match=pattern, count=CHUNK_SIZE)
        if keys:
            deleted_count += client.delete(*keys)
        
    print('{} registries deleted from: {} DB {}'.format(deleted_count,connection['host'],connection['db']))

def mock():
    client = redis.Redis(host='localhost', port=6379,db=0)
    for key, value in (('A', '1'), ('B', '2'), ('C', '3'),('D', '3')):
        client.set(key, value)

    client2 = redis.Redis(host='localhost', port=6379,db=1)
    for key, value in (('F', '1'),('G', '1')):
        client2.set(key, value)

scanClean()