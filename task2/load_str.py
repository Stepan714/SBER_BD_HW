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
    r.set(f'news:{i}', json.dumps(news))
end_time = time.time()
print(f"Time taken to save as strings: {end_time - start_time} seconds")

start_time = time.time()
for i in range(len(data_news)):
    news_str = r.get(f'news:{i}')
end_time = time.time()
print(f"Time taken to read from strings: {end_time - start_time} seconds")
