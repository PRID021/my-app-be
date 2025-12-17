# Makefile for managing Docker environment

# Define compose files for different environments
COMPOSE_DEV := docker compose -f docker-compose.yml
COMPOSE_PROD := docker compose -f docker-compose.prod.yml

.PHONY: help up-dev down-dev logs-dev shell-dev migrate-dev revision seed-dev test test-cov up-prod down-prod logs-prod shell-prod migrate-prod new-test-tag

help:
	@echo "Usage: make [command]"
	@echo ""
	@echo "Development Commands (uses docker-compose.yml):"
	@echo "  up-dev        Start dev services and build images if necessary."
	@echo "  down-dev      Stop and remove dev services, containers, and local images."
	@echo "  logs-dev      Follow logs for the dev app service."
	@echo "  shell-dev     Get a shell inside the running dev app container."
	@echo "  migrate-dev   Manually run database migrations in the dev environment."
	@echo "  revision      Create a new alembic revision. Usage: make revision msg=\"Your message\""
	@echo "  seed-dev      Seed the database with initial data for development."
	@echo "  test          Run automated tests in a temporary dev container."
	@echo "  test-cov      Run tests with a coverage report."
	@echo ""
	@echo "Production Commands (uses docker-compose.prod.yml):"
	@echo "  up-prod       Start prod services in detached mode."
	@echo "  down-prod     Stop and remove prod services and containers."
	@echo "  logs-prod     Follow logs for the prod app service."
	@echo "  shell-prod    Get a shell inside the running prod app container."
	@echo "  migrate-prod  Run database migrations in the prod environment."
	@echo ""
	@echo "Git Commands:"
	@echo "  new-test-tag  Create and push a new incremental test tag (e.g., test-v0.1.5)."

# --- Development Commands ---
up-dev:
	@echo "Starting up development services..."
	$(COMPOSE_DEV) up --build

down-dev:
	@echo "Stopping development services and removing images..."
	$(COMPOSE_DEV) down --rmi local --volumes

logs-dev:
	@echo "Following logs for dev app service..."
	$(COMPOSE_DEV) logs -f app

shell-dev:
	@echo "Accessing shell in dev app container..."
	$(COMPOSE_DEV) exec app /bin/sh

migrate-dev:
	@echo "Running dev database migrations..."
	$(COMPOSE_DEV) exec app poetry run alembic upgrade head

# The 'msg' variable will be passed from the command line
msg ?= "New migration"
revision:
	@echo "Creating new revision: $(msg)"
	$(COMPOSE_DEV) exec app poetry run alembic revision --autogenerate -m "$(msg)"

seed-dev:
	@echo "Seeding database with mock data..."
	$(COMPOSE_DEV) exec app poetry run python -m app.db.seed

test:
	@echo "Running tests..."
	$(COMPOSE_DEV) run --rm --no-deps app poetry run pytest -v

test-cov:
	@echo "Running tests with coverage report..."
	$(COMPOSE_DEV) run --rm --no-deps app poetry run pytest --cov=app --cov-report=term-missing -v

# --- Production Commands ---
up-prod:
	@echo "Starting up production services in detached mode..."
	$(COMPOSE_PROD) up --build -d

down-prod:
	@echo "Stopping production services..."
	$(COMPOSE_PROD) down

logs-prod:
	@echo "Following logs for prod app service..."
	$(COMPOSE_PROD) logs -f app

shell-prod:
	@echo "Accessing shell in prod app container..."
	$(COMPOSE_PROD) exec app /bin/sh

migrate-prod:
	@echo "Running production database migrations..."
	$(COMPOSE_PROD) exec app ./.venv/bin/alembic upgrade head

# --- Git Commands ---
new-test-tag:
	@echo "Creating new test tag..."
	python ./scripts/tag_and_push.py
