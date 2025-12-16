# Makefile for managing Docker environment

.PHONY: help up down logs shell migrate revision seed test test-cov

help:
	@echo "Usage: make [command]"
	@echo ""
	@echo "Commands:"
	@echo "  up        Start all services and build images if necessary."
	@echo "  down      Stop and remove all services."
	@echo "  logs      Follow logs for the app service in real-time."
	@echo "  shell     Get a shell inside the running app container."
	@echo "  migrate   Manually run database migrations."
	@echo "  revision  Create a new alembic revision. Usage: make revision msg=\"Your message\""
	@echo "  seed      Seed the database with mock data."
	@echo "  test      Run the automated tests."

up:
	@echo "Starting up services in attached mode..."
	docker compose up --build

down:
	@echo "Stopping services..."
	docker compose down

logs:
	@echo "Following logs for app service..."
	docker compose logs -f app

shell:
	@echo "Accessing shell in app container..."
	docker compose exec app /bin/sh

migrate:
	@echo "Running database migrations..."
	docker compose exec app python -m alembic upgrade head

test:
	@echo "Running tests..."
	docker compose run --rm --no-deps --entrypoint "" app python -m pytest -v

test-cov:
	@echo "Running tests with coverage report..."
	docker compose run --rm --no-deps --entrypoint "" app python -m pytest --cov=app --cov-report=term-missing -v

# Biến msg sẽ được truyền vào từ dòng lệnh
msg ?= "New migration"
revision:
	@echo "Creating new revision: $(msg)"
	docker compose exec app python -m alembic revision --autogenerate -m "$(msg)"

seed:
	@echo "Seeding database with mock data..."
	docker compose exec app python app/db/seed.py
