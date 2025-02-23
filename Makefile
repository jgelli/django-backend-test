.PHONY: build up down migrations migrate superuser seed test

ENVIRONMENT ?= dev

ifeq ($(ENVIRONMENT), prod)
	COMPOSE_FILE = .docker/docker-compose.prod.yml
else
	COMPOSE_FILE = .docker/docker-compose.dev.yml
endif
  

build:
	docker compose -f $(COMPOSE_FILE) build

up:
	docker compose -f $(COMPOSE_FILE) up -d

down:
	docker compose -f $(COMPOSE_FILE) down

runserver:
	docker compose -f $(COMPOSE_FILE) run --rm api python manage.py runserver 0.0.0.0:8000

migrations:
	docker compose -f $(COMPOSE_FILE) run --rm api python manage.py makemigrations

migrate:
	docker compose -f $(COMPOSE_FILE) run --rm api python manage.py migrate

superuser:
	docker compose -f $(COMPOSE_FILE) run --rm api python manage.py createsuperuser

seed:
	docker compose -f $(COMPOSE_FILE) run --rm api python manage.py seed_data

test:
	docker compose -f $(COMPOSE_FILE) run --rm api python manage.py test

