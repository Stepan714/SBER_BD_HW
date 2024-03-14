## Установка Docker и MongoDB
Установил Докер, перенес в Applications. Далее в терминале вбил команду:

С помощью команды:
```console
docker run -d --name mongo-database -p 27017:27017 mongo:4
```
создал и запустил контейнер с MongoDB. После настроил соединение с MongoDB Compass.
_____
## Загружаем датасет Titanic

Создал базу данных titanic и загрузил датасет вот отсюда: https://www.kaggle.com/c/titanic/data?select=test.csv
<image src="/images/install.jpg" alt="Загрузка">


____
## CRUD

- INSERT:
```console
db.titanic.insertOne({
    "_id": "65f2c4a9f5a09dc44d0ba4cc",
    "PassengerId": 1,
    "Survived": 1,
    "Pclass": 1,
    "Name": "Smith, Mrs. Jane",
    "Sex": "female",
    "Age": 30,
    "SibSp": 0,
    "Parch": 1,
    "Ticket": "PC 17599",
    "Fare": 71.2833,
    "Embarked": "C"
});
```
<image src="/images/insert.jpg" alt="Вставка">
<image src="/images/insert1.jpg" alt="Вставка">

- FIND:
```console
db.titanic.find({ "Survived": 1 });

db.titanic.find({ "Sex": "female" });
```

<image src="/images/find1.jpg" alt="Поиск1">
<image src="/images/find2.jpg" alt="Поиск2">

- UPDATE:

<image src="/images/update.jpg" alt="Изменение">
<image src="/images/update1.jpg" alt="Результат Изменения">

- DELETE:

<image src="/images/delete.jpg" alt="Удаление">
<image src="/images/delete1.jpg" alt="Результат Удаления">


