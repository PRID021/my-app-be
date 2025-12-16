# My FastAPI Backend

![Build Status](https://github.com/<your-username>/<your-repo>/actions/workflows/ci.yml/badge.svg)
[![codecov](https://codecov.io/gh/<your-username>/<your-repo>/branch/main/graph/badge.svg)](https://codecov.io/gh/<your-username>/<your-repo>)
[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


A complete FastAPI backend with clean architecture, asynchronous database operations, and production-ready logging. This project is fully containerized with Docker for easy setup and execution.

## 🚀 Quickstart: Running with Docker (Recommended)

With Docker and Docker Compose installed, you can get the entire stack (app + database) running with a single command.

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/) (usually included with Docker Desktop)
- `make` (On Windows, you can install it via [Chocolatey](https://chocolatey.org/packages/make) or use WSL)

###
**Run the application:**

```bash
make up
```

That's it! 

The application will be available at `http://127.0.0.1:8000`. The `entrypoint.sh` script will automatically wait for the database and apply migrations on startup.

### Makefile Commands

- `make up`: Builds the images and starts all services.
- `make down`: Stops and removes all containers and networks.
- `make logs`: View real-time logs from the FastAPI application.
- `make shell`: Open a shell inside the running application container (useful for debugging).
- `make migrate`: Manually apply database migrations.
- `make revision msg="your message"`: Create a new database migration file.
- `make seed`: Populate the database with initial mock data.
- `make test`: Run the automated tests against an in-memory test database.

---

## 💻 Local Development (Without Docker)

If you prefer to run the application directly on your machine, follow these steps.

### 1. Prerequisites

- Python 3.11 or higher
- PostgreSQL database running

## Features

- **Python 3.11+**, **FastAPI**
- **Clean Architecture**: `api`, `services`, `repositories`, `schemas`
- **Database**: **PostgreSQL** with **SQLAlchemy 2.0 (async)**
- **Migrations**: **Alembic**
- **Validation**: **Pydantic V2**
- **Configuration**: `pydantic-settings` with `.env` file
- **Logging**: **Structlog** for JSON logging with rotation

## Project Structure

```
.
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   └── posts.py
│   │   └── router.py
│   ├── core/
│   │   ├── config.py
│   │   └── logger.py
│   │   └── security.py
│   ├── db/
│   │   ├── base.py
│   │   ├── session.py
│   │   └── migrations/
│   │       ├── versions/
│   │       │   └── ...
│   │       ├── env.py
│   │       └── script.py.mako
│   ├── models/
│   │   └── post.py
│   ├── repositories/
│   │   └── post_repository.py
│   ├── schemas/
│   │   └── post_schema.py
│   ├── services/
│   │   └── post_service.py
│   ├── main.py
│   └── __init__.py
├── alembic.ini
├── requirements.txt
└── .env
```

## Setup and Installation

### 1. Prerequisites

- Python 3.11 or higher
- PostgreSQL database running

### 2. Clone the Repository

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 3. Create a Virtual Environment

Poetry will automatically manage the virtual environment for you.

### 4. Install Dependencies

```bash
poetry install
```

### 5. Configure Environment Variables

Create a file named `.env` inside the `app` directory and add your database connection URL.

**`app/.env`:**
```env
DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/mydb
LOG_LEVEL=INFO
```
*Replace `user`, `pass`, `localhost`, `5432`, and `mydb` with your actual PostgreSQL credentials and database name.*

### 6. Run Database Migrations

Before running the application for the first time, you need to apply the database migrations to create the necessary tables.

```bash
alembic upgrade head
```
*(Run this command from the root directory of the project)*

## Running the Application

To start the FastAPI server, run the following command from the root directory:

```bash
uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

You can access the interactive API documentation (Swagger UI) at `http://127.0.0.1:8000/docs`.

- **`GET /api/v1/posts/`**: Retrieve a list of all posts.
- **`POST /api/v1/posts/`**: Create a new post.

**Example `POST` request body:**
```json
{
  "title": "My First Post",
  "content": "This is the content of my first post."
}
```
.........