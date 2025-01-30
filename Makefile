.PHONY: build up down migrations migrate superuser seed test

build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

migrations:
	docker compose run --rm api python manage.py makemigrations

migrate:
	docker compose run --rm api python manage.py migrate

superuser:
	docker compose run --rm api python manage.py createsuperuser

seed:
	docker compose run --rm api python manage.py seed_data

test:
	docker compose run --rm api python manage.py test