## Установка Docker и MongoDB
Установил Докер, перенес в Applications

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



## Индексы
Посмотрим на анализ запроса на поиск до создания индекса:
<div class="boxed">
> db.titanic.find({ "Sex": "male" }).explain("executionStats")
{
	"queryPlanner" : {
		"plannerVersion" : 1,
		"namespace" : "Titanic.titanic",
		"indexFilterSet" : false,
		"parsedQuery" : {
			"Sex" : {
				"$eq" : "male"
			}
		},
		"winningPlan" : {
			"stage" : "COLLSCAN",
			"filter" : {
				"Sex" : {
					"$eq" : "male"
				}
			},
			"direction" : "forward"
		},
		"rejectedPlans" : [ ]
	},
	"executionStats" : {
		"executionSuccess" : true,
		"nReturned" : 577,
		"executionTimeMillis" : 1,
		"totalKeysExamined" : 0,
		"totalDocsExamined" : 891,
		"executionStages" : {
			"stage" : "COLLSCAN",
			"filter" : {
				"Sex" : {
					"$eq" : "male"
				}
			},
			"nReturned" : 577,
			"executionTimeMillisEstimate" : 0,
			"works" : 893,
			"advanced" : 577,
			"needTime" : 315,
			"needYield" : 0,
			"saveState" : 0,
			"restoreState" : 0,
			"isEOF" : 1,
			"direction" : "forward",
			"docsExamined" : 891
		}
	},
	"serverInfo" : {
		"host" : "ebfa49770a64",
		"port" : 27017,
		"version" : "4.4.29",
		"gitVersion" : "f4dda329a99811c707eb06d05ad023599f9be263"
	},
	"ok" : 1
}
<div class="boxed">

Далее создаем индекс и смотрим на результат запроса:
<image src="/images/index.jpg" alt="Создание индекса">

<div class="boxed1">
> db.titanic.find({ "Sex": "male" }).explain("executionStats")
{
	"queryPlanner" : {
		"plannerVersion" : 1,
		"namespace" : "Titanic.titanic",
		"indexFilterSet" : false,
		"parsedQuery" : {
			"Sex" : {
				"$eq" : "male"
			}
		},
		"winningPlan" : {
			"stage" : "FETCH",
			"inputStage" : {
				"stage" : "IXSCAN",
				"keyPattern" : {
					"Sex" : 1
				},
				"indexName" : "Sex_1",
				"isMultiKey" : false,
				"multiKeyPaths" : {
					"Sex" : [ ]
				},
				"isUnique" : false,
				"isSparse" : false,
				"isPartial" : false,
				"indexVersion" : 2,
				"direction" : "forward",
				"indexBounds" : {
					"Sex" : [
						"[\"male\", \"male\"]"
					]
				}
			}
		},
		"rejectedPlans" : [ ]
	},
	"executionStats" : {
		"executionSuccess" : true,
		"nReturned" : 577,
		"executionTimeMillis" : 1,
		"totalKeysExamined" : 577,
		"totalDocsExamined" : 577,
		"executionStages" : {
			"stage" : "FETCH",
			"nReturned" : 577,
			"executionTimeMillisEstimate" : 0,
			"works" : 578,
			"advanced" : 577,
			"needTime" : 0,
			"needYield" : 0,
			"saveState" : 0,
			"restoreState" : 0,
			"isEOF" : 1,
			"docsExamined" : 577,
			"alreadyHasObj" : 0,
			"inputStage" : {
				"stage" : "IXSCAN",
				"nReturned" : 577,
				"executionTimeMillisEstimate" : 0,
				"works" : 578,
				"advanced" : 577,
				"needTime" : 0,
				"needYield" : 0,
				"saveState" : 0,
				"restoreState" : 0,
				"isEOF" : 1,
				"keyPattern" : {
					"Sex" : 1
				},
				"indexName" : "Sex_1",
				"isMultiKey" : false,
				"multiKeyPaths" : {
					"Sex" : [ ]
				},
				"isUnique" : false,
				"isSparse" : false,
				"isPartial" : false,
				"indexVersion" : 2,
				"direction" : "forward",
				"indexBounds" : {
					"Sex" : [
						"[\"male\", \"male\"]"
					]
				},
				"keysExamined" : 577,
				"seeks" : 1,
				"dupsTested" : 0,
				"dupsDropped" : 0
			}
		}
	},
	"serverInfo" : {
		"host" : "ebfa49770a64",
		"port" : 27017,
		"version" : "4.4.29",
		"gitVersion" : "f4dda329a99811c707eb06d05ad023599f9be263"
	},
	"ok" : 1
}
<div class="boxed1">


Сравнение:

Первый запрос использует операцию COLLSCAN , что означает, что MongoDB сканирует все документы в коллекции для выполнения запроса. Индекс не используется.

Второй запрос использует операцию IXSCAN, что означает, что MongoDB использует индекс для поиска документов, удовлетворяющих условию запроса. Это более эффективно, чем полное сканирование коллекции.

Заметим, что появилась разница в значениях totalKeysExamined и totalDocsExamined между двумя запросами. Во втором запросе MongoDB просматривает только 577 ключей (индекс используется), в то время как в первом запросе просматривает все 891 документов в коллекции.

Тем самым можно сделать вывод, что использование индексов ускоряет запросы (Выбранный датасет не был большим, поэтому невооруженным взглядом разница не видна)
