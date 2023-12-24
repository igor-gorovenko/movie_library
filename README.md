# movie_library

Сервис для фильмов и сериалов

## Функции

- Каталог фильмов и сериалов
- Фильтры по жанрам, дате, рейтингу
- Последние добавления
- Детальная фильма, автора, актеров
- Возможность оставить комментарий под фильмом

## Gettign started


#### 1. Clone this repository

```
git clone git@github.com:igor-gorovenko/movie_library.git
```

Переходим в проек

```
cd movie_library
```

#### 2. Install dependencies:

У вас должен быть установлен python3
www.python.org/downloads

Создаем виртуальное окружение

```
python3 -m venv .venv
```

Активируем виртуальное окружение

```
source .venv/bin/activate
```

Устанавливаем зависимости

```
pip install -r requirements.txt
```

создаем админа с помощью
python manage.py createsuperuser

логин, почта, и пароль 2 раза
почту можем пропустить нажимаем Enter

```
admin
test1234
```

Теперь по адрес сайта + /admin
мы можем войти в админку с помощью данных, которые создали супер пользователя.



