## Запуск Redis с помощью Docker
```
docker pull redis
```
```
docker run --name=redis-devel --publish=6379:6379 --hostname=redis --restart=on-failure --detach redis:latest
```
<image src="../images/redis_server.jpg" alt="Redis">
Далее с помощью Python подключаемся к БД и сохраняем датасет (>= 100Mb) в качестве разных типов:
_____

### Строка
<image src="../images/load_str.jpg" alt="String">
_____
  
### Hset
<image src="../images/load_hset.jpg" alt="Hset">
_____
  
### Zset
<image src="../images/load_zset.jpg" alt="Zset">
______
  
### List
<image src="../images/load_list.jpg" alt="List">
______

Далее создаем кластер. Прописываем docker-compose.yml, redis1.conf. redis2.conf, redis3.conf
Открываю 3 терминала, запускаем каждую ноду, а затем нужные ноды "знакомим" с остальными:
С помощью команды:
```
CLUSTER MEET <IP_адрес_контейнера_2> <порт_контейнера_2>
```
Узнать IP:
```
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' redis1
```

<image src="../images/redis_3.jpg">

<image src="../images/redis_nodes.jpg">

<image src="../images/redis_conf.jpg">
