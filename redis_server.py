import redis

r = redis.Redis(
    host='localhost', 
    port=6379
)

r.set('beg','phonexx')

print(r.get('beg'))