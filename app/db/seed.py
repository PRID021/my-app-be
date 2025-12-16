import asyncio
import logging
from app.db.session import AsyncSessionLocal
from app.models.post import Post

# Cấu hình logging cơ bản
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def seed_data():
    """
    Hàm để nạp dữ liệu mẫu vào database.
    """
    db = AsyncSessionLocal()
    try:
        logger.info("Bắt đầu nạp dữ liệu mẫu...")

        # Dữ liệu mẫu
        mock_posts = [
            Post(
                title="Chào mừng đến với FastAPI!",
                content="Đây là bài viết đầu tiên được tạo tự động trong một ứng dụng FastAPI với kiến trúc sạch.",
            ),
            Post(
                title="Docker và Makefile",
                content="Sử dụng Docker và Makefile giúp đơn giản hóa quá trình cài đặt và chạy ứng dụng một cách đáng kinh ngạc.",
            ),
            Post(
                title="SQLAlchemy 2.0 Async",
                content="Thao tác với database ở chế độ bất đồng bộ (async) với SQLAlchemy 2.0 và asyncpg mang lại hiệu năng cao.",
            ),
            Post(
                title="Clean Architecture in Python",
                content="Applying clean architecture principles makes the codebase scalable, testable, and maintainable.",
            )
        ]
        
        # Thêm dữ liệu vào session và commit
        db.add_all(mock_posts)
        await db.commit()
        
        logger.info(f"Đã nạp thành công {len(mock_posts)} bài viết mẫu vào database.")

    finally:
        await db.close()

if __name__ == "__main__":
    asyncio.run(seed_data())
