## sql-alchemy_educational_project
***Учебный проект с курса START ML школы Karpov.Courses***

Практиковалась в:
- Освоении баз данных в Python и ORM 
- Обращении к удаленной БД через SQL-Alchemy
- Написании endpoinds FastAPI 
- Валидации результатов запроса через pydantic

**Структура проекта**

* [app.py](app.py) - основной файл, в котором реализованы endpoints FastAPI
* [schema.py](schema.py) - описание классов `UserGet`, `PostGet`, `FeedGet` как моделей pydantic
* [table_feed.py](table_feed.py) -  описание класса `Feed`, который описывает таблицу `feed` на языке ORM
* [table_post.py](table_post.py) - описание класса `Post`, который описывает таблицу `post` на языке ORM
* [table_user.py](table_user.py) - описание класса `User`, который описывает таблицу `user` на языке ORM

**Структура базы данных**

> Таблица `user` содержит данные о пользователях

![img](https://sun9-83.userapi.com/impg/ApsVGlL5COpZIMMiTJNND_D_pb4qz_b9UswLFg/otQpMcK4kUo.jpg?size=190x216&quality=95&sign=8485ffdd633d15fc7a80c971402a4c0b&type=album)

> Таблица `post` содержит данные о постах

![img2](https://sun9-66.userapi.com/impg/MFYVqytBlaamDmICWdlkFT5Q-eUwK4xSpW2ELw/utDw0DLjwk4.jpg?size=107x100&quality=95&sign=3c28810fff10277548dfabeef4773d59&type=album)

> Таблица `feed_action` содержит данные о взаимодействии пользователей с постами

![img3](https://sun9-81.userapi.com/impg/SKb6hnQjYFHQlQJL9kDdlsrpjsyLWSEKZ4Nj8A/9GH7iPfU_JM.jpg?size=285x117&quality=95&sign=d5b86fd87679b2392dc43d481396e8fa&type=album)

**Содержание app.py**

1. Endpoints `GET /user/{id}`, `GET /post/{id}` возвращают одну запись из таблиц `user` или `post` с соответсвующим `id` в формате JSON, при отсуствии в базе возвращают `HTTPException(status_code=404, detail="post not found")` 

2. Endpoint `GET /post/{id}/feed`возвращает все действия (в количестве `limit`) из `feed` для поста с `id = {id}` (из запроса). Если действия в базе для этого `id` отсутствуют, то возвращает status code 200(ОК) и пустой список.

3. Endpoint `GET /post/recommendations/` является baseline-моделью для системы рекомендаций постов для пользователя.
Endpoint возвращает топ `limit` постов, отсортированных в порядке убывания по количеству лайков для пользователя в качестве рекомендации. То есть, для каждого пользователя выдается одинаковый топ `limit` самых залайканных постов.
