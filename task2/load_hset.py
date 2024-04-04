import redis
import json
import time

NAME = 'News_Category_Dataset_v3.json'
r = redis.Redis(host='localhost', port=6379, db=1)

with open(f'/Users/stepan/Downloads/{NAME}', 'r') as file:
    data_news = [json.loads(line) for line in file]

r.flushdb()

start_time = time.time()
for i, news in enumerate(data_news):
    for key, value in news.items():
        r.hset(f'news_hset:{i}', key, value)
end_time = time.time()
print(f"Time taken to save as hashes: {end_time - start_time} seconds")

start_time = time.time()
for i in range(len(data_news)):
    news_hash = r.hgetall(f'news:{i}')
end_time = time.time()
print(f"Time taken to read from hashes: {end_time - start_time} seconds")
