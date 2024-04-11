## Запуск CuuchDB с помощью Docker
```
docker pull couchdb
```

<image src="../images/step1.jpg">
____

### Далее запускаем контейнер с проставленными admin и password и создаем БД:

```
docker run -d \
  --name couchdb \             
  -p 5984:5984 \
  -e COUCHDB_USER=YOUR_NAME \
  -e COUCHDB_PASSWORD=YOUR_PASSWORD \     
  couchdb
```
<image src="../images/step2.jpg">

```
curl -X PUT http://stepan:123@localhost:5984/couchdb
```
Затем в .html файле изменяем это: 
```
Remote: new PouchDB('http://YOUR_NAME:YOUR_PASSWORD@localhost:5984/couchdb')
```
___
### После с помощью curl добавляем фамилию в БД:

```
curl -X POST \                                      
  http://stepan:123@localhost:5984/couchdb \
  -H 'Content-Type: application/json' \
  -d '{
        "name": "YOUR_NAME"
      }'
```

<image src="../images/step3.jpg">
___
### После всего этого вставляем ссылку и настраиваем CORS:
http://localhost:5984/_utils/
<image src="../images/step4.jpg">
____

### Далее открываем .html файл:
<image src="../images/step5.jpg">

