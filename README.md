# Students app

Students app -- веб-приложение, позволяющее получить список студентов, добавлять/удалять студента по id.
##

Запуск приложения
```bash
uvicorn app.api:app --host 0.0.0.0
```

Запуск БД
```bash
docker-compose up
```

Миграция БД (запустить после подъема докера, но перед приложением)
```bash
python3 init_db.py  # (Костыль, чтобы не кодить миграции)
````


## Usage of API
GET REQUEST: 
get all students
```bash
curl -i http://localhost:8000/students
```

GET REQUEST: 
get student by id
```bash
curl -i http://localhost:8000/students/<student_id>
```

DELETE REQUEST:
delete a student
```bash
curl -X DELETE http://localhost:8000/students/<id: id of student>
```

POST REQUEST:
add a student
```bash
curl -i -H "Content-Type: application/json" -X POST -d "{\"id\": 3232, \"full_name\":\"Кихтенко Татьяна Михайловна\", \"rating\":100, \"age\":20, \"photo_link\": \"http:/IIIvan\", \"speciality\":\"Математика и КН\", \"group\":\"КН-302\", \"sex\":\"f\", \"fav_colour\":\"red\"}" http://localhost:8000/students
```

## Автор
@pornoiya
