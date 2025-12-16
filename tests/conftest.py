from typing import AsyncGenerator

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.db.base import Base
from app.db.session import get_db
from app.main import app

# --- Cài đặt Database Test ---
# Sử dụng SQLite trong bộ nhớ cho việc test để chạy nhanh và độc lập
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

engine = create_async_engine(TEST_DATABASE_URL, echo=False)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)


# --- Override Dependency ---
async def override_get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency override để sử dụng database test thay vì database thật.
    """
    async with TestingSessionLocal() as session:
        yield session


# Áp dụng việc override dependency cho app
app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="function")
async def test_db_setup():
    """
    Fixture để tạo và xóa các bảng database cho mỗi test function.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="function")
async def client(test_db_setup: None) -> AsyncGenerator[AsyncClient, None]:
    """
    Fixture để tạo một TestClient cho mỗi test function.
    Nó phụ thuộc vào test_db_setup để đảm bảo database đã được chuẩn bị.
    """
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as c:
        yield c
