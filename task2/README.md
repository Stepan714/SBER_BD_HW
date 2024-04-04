## Запуск Redis с помощью Docker
```
docker pull redis
```
```
docker run --name=redis-devel --publish=6379:6379 --hostname=redis --restart=on-failure --detach redis:latest
```
<image src="../images/redis_server.jpg"
Далее с помощью Python подключаемся к БД и сохраняем датасет (>= 100Mb) в качестве разных типов:
___

### Строка
<image src="../images/load_str.jpg" alt="Загрузка">
____
  
### Hset
<image src="../images/load_hset.jpg" alt="Загрузка">
____
  
### Zset
<image src="../images/load_zset.jpg" alt="Загрузка">
____
  
### List
<image src="../images/load_list.jpg" alt="Загрузка">
____

Далее создаем создаем кластер. Прописываем docker-compose.yml, redis1.conf. redis2.conf, redis3.conf
Открываю 3 терминала, запускаем каждую ноду, а затем нужные ноды "знакомим" с остальными:
<image src="../images/redis_3.jpg"
<image src="../images/redis_nodes.jpg"
<image src="../images/redis_conf.jpg"
