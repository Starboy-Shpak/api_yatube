#  Социальная сеть "Yatube"

Социальная сеть. Микроблог.

## Что проект умеет?
Любой посетитель сайта может зарегистрироваться, создавать посты самостоятельно, публиковать их в отдельных группах по категориям. Реализованы добавление и удаление своих постов, комментирование постов других пользователей. Реализована подписка на других авторов с возможностью отслеживания новостей среди своих предпочтений.
 
### Технологии
- Python 3.7 
- Django 2.2.19
- MySQL

### Как запустить проект:
- Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:Starboy-Shpak/api_yatube.git
``` 
- Создать и активировать виртуальное окружение:
```
python -m venv env
source env/Scripts/activate
``` 
- Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
``` 
- Перейти в каталог и выполнить миграции:
```
python manage.py migrate
``` 
- Запустить проект:
```
python manage.py runserver
``` 
### Примеры запросов к API:

Получить список всех постов (GET):

```
http://127.0.0.1:8000/api/v1/posts/
```

Получить определенный пост (GET):

```
http://127.0.0.1:8000/api/v1/posts/1/
```

Получить комментарии определенного поста (GET):

```
http://127.0.0.1:8000/api/v1/posts/1/comments/
```

Получить список всех групп (GET):

```
http://127.0.0.1:8000/api/v1/groups/
```

Создать новый пост (POST):

(Требуется аутентификация)

```
http://127.0.0.1:8000/api/v1/posts/
```
---
Автор: Вадим Шпак. Связаться со мной можно в [телеграм](https://t.me/starboy_shpak/)
