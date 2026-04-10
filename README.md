# Лабораторная работа №2
## REST API на FastAPI + SQLAlchemy

### Функционал
- Создание задачи (POST)
- Получение списка с пагинацией (GET)
- Получение одной задачи (GET)
- Полное обновление (PUT)
- Частичное обновление (PATCH)
- Мягкое удаление (DELETE)

### Запуск

pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 4200
### API Эндпоинты
Метод	URI	Описание
POST	/items/	Создать
GET	/items/	Список
GET	/items/{id}	Получить
PUT	/items/{id}	Полное обновление
PATCH	/items/{id}	Частичное обновление
DELETE	/items/{id}	Удаление
### Пример ответа (

{
  "data": [...],
  "total": 2,
  "page": 1,
  "limit": 10,
  "total_pages": 1
}
