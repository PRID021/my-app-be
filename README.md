# My FastAPI Backend

[![Test on Dev Branch](https://github.com/your-username/your-repository/actions/workflows/test-dev.yml/badge.svg)](https://github.com/your-username/your-repository/actions/workflows/test-dev.yml)
[![Coverage Status](https://coveralls.io/repos/github/your-username/your-repository/badge.svg?branch=dev)](https://coveralls.io/github/your-username/your-repository?branch=dev)

This is a modern, robust backend starter project built with FastAPI, PostgreSQL, and Docker. It's designed to be high-performance, easy to set up, and ready for production.

> **Note:** Please replace `your-username/your-repository` in the badges above with your actual GitHub username and repository name.

## ✨ Features

- **Framework**: **FastAPI** for high-performance, easy-to-learn, and fast-to-code APIs.
- **Database**: **PostgreSQL** as the relational database.
- **ORM**: **SQLAlchemy 2.0** for powerful and asynchronous database interactions.
- **Migrations**: **Alembic** for handling database schema migrations.
- **Data Validation**: **Pydantic** for data validation and settings management, deeply integrated with FastAPI.
- **Containerization**: **Docker** and **Docker Compose** for a consistent development and production environment.
- **Dependency Management**: **Poetry** for modern, deterministic dependency management.
- **Testing**: **Pytest** with `pytest-asyncio` for asynchronous testing.
- **Code Quality**:
  - **Ruff** for extremely fast Python linting.
  - **Black** for uncompromising code formatting.
- **CI/CD**: **GitHub Actions** to automatically run tests, linting, and formatting checks on every push to the `dev` branch.
- **Code Coverage**: **Coveralls** for tracking test coverage.

## 🚀 Getting Started

The recommended way to run this project is with Docker and Docker Compose.

### Prerequisites

- Docker
- Docker Compose (usually included with Docker Desktop)

### Docker Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd my-app-be
    ```

2.  **Create the environment file:**
    Copy the example environment file. You can customize the database credentials if you wish, but the defaults are fine for local development.
    ```bash
    cp .env.docker.example .env.docker
    ```

3.  **Build and run the services:**
    This command will build the `app` image and start both the FastAPI application and the PostgreSQL database containers.
    ```bash
    docker-compose up --build
    ```

    The API will be available at http://localhost:8000. The interactive documentation (Swagger UI) will be at http://localhost:8000/docs.

    The application code is mounted as a volume, so any changes you make to the code will trigger an automatic reload of the server.

## 🗄️ Database Migrations (Alembic)

Alembic is used to manage database schema changes. Migrations are run from within the `app` container to ensure it has access to the database service.

1.  **Create a new migration:**
    After changing your SQLAlchemy models (e.g., in `app/models/`), generate a new migration script automatically.
    ```bash
    docker-compose exec app alembic revision --autogenerate -m "Your descriptive migration message"
    ```
    This will create a new file in `app/db/migrations/versions/`.

2.  **Apply migrations:**
    To apply all pending migrations to the database:
    ```bash
    docker-compose exec app alembic upgrade head
    ```

## 🧪 Running Tests

Tests are run using Pytest. The test suite is configured to run against a temporary, isolated test database.

To run all tests and generate a coverage report:
```bash
docker-compose exec app poetry run pytest
```

Or if you are developing locally with Poetry:
```bash
poetry run pytest
```

## 🧹 Code Quality

This project uses **Ruff** for linting and **Black** for formatting to ensure code is clean and consistent.

### Linting

To check for linting errors with Ruff:
```bash
poetry run ruff check .
```

To automatically fix linting errors:
```bash
poetry run ruff check . --fix
```

### Formatting

To check if the code is formatted correctly with Black:
```bash
poetry run black --check .
```

To automatically format the code:
```bash
poetry run black .
```

## ⚙️ Local Development without Docker

If you prefer not to use Docker, you can set up a local environment using Poetry.

1.  **Install Poetry.**

2.  **Install dependencies:**
    This will create a virtual environment inside the project directory (`.venv`).
    ```bash
    poetry install
    ```

3.  **Set up a local PostgreSQL database.**

4.  **Set the `DATABASE_URL` environment variable:**
    You can use a `.env` file or export it in your shell.
    ```sh
    export DATABASE_URL="postgresql+asyncpg://user:password@localhost:5432/dbname"
    ```

5.  **Run the application:**
    ```bash
    poetry run uvicorn app.main:app --reload
    ```