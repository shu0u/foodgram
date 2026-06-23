# Foodgram

Foodgram - это веб-приложение для публикации рецептов. Пользователи могут регистрироваться, публиковать свои рецепты с фотографиями, добавлять чужие рецепты в избранное, подписываться на публикации других авторов и формировать список покупок. Список покупок можно скачать в виде текстового файла - ингредиенты из всех выбранных рецептов суммируются автоматически.

Функции проекта:
- Регистрация и авторизация по email
- Создание, редактирование и удаление рецептов
- Фильтрация рецептов по тегам
- Добавление рецептов в избранное
- Подписка на авторов
- Формирование и скачивание списка покупок
- Получение короткой ссылки на рецепт
- Загрузка аватара пользователя

## Развернутый проект

https://foodgram-shu0u.dynv6.net/

## Стек технологий

- Python 3.12
- Django 4.2
- Django REST Framework
- Djoser
- PostgreSQL
- Docker, Docker Compose
- Nginx
- Gunicorn
- GitHub Actions

## Как развернуть проект

1. Клонировать репозиторий:

```bash
git clone https://github.com/shu0u/foodgram.git
cd foodgram
```

2. Создать файл `.env` в папке `backend/` (см. раздел «Как заполнить .env»).

3. Запустить контейнеры:

```bash
cd infra
docker compose up -d --build
```

4. Применить миграции и собрать статику:

```bash
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py collectstatic --noinput
docker compose exec backend cp -r /app/collected_static/. /backend_static/static/
```

5. Создать суперпользователя:

```bash
docker compose exec backend python manage.py createsuperuser
```

## Загрузка тестовых данных

Загрузка ингредиентов из CSV:

```bash
docker compose exec backend python manage.py load_ingredients
```

Создание тегов через Django shell:

```bash
docker compose exec backend python manage.py shell
```

```python
from apps.recipes.models import Tag
Tag.objects.create(name='Завтрак', slug='breakfast')
Tag.objects.create(name='Обед', slug='lunch')
Tag.objects.create(name='Ужин', slug='dinner')
```

## Как заполнить .env

Создать файл `.env` в папке `backend/` со следующим содержимым:

```env
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,backend
POSTGRES_DB=foodgram
POSTGRES_USER=foodgram_user
POSTGRES_PASSWORD=foodgram_password
DB_HOST=db
DB_PORT=5432
```

## Спецификация API (ReDoc)

https://foodgram-shu0u.dynv6.net/api/docs/

## Автор

shu0u
