# 3. Các Gói và Lệnh

## 📦 Các Gói (Packages) Quan trọng

Dưới đây là danh sách các thư viện chính được sử dụng trong dự án và vai trò của chúng:

-   **fastapi**: Framework chính để xây dựng API.
-   **uvicorn**: Server ASGI để chạy ứng dụng FastAPI.
-   **sqlalchemy**: ORM để tương tác với cơ sở dữ liệu PostgreSQL.
-   **asyncpg**: Driver *bất đồng bộ* cho PostgreSQL, được SQLAlchemy sử dụng.
-   **psycopg2-binary**: Driver *đồng bộ* cho PostgreSQL, được sử dụng trong các script (như `seed.py`) và Alembic.
-   **alembic**: Công cụ quản lý migration cho schema cơ sở dữ liệu.
-   **pydantic** & **pydantic-settings**: Dùng để xác thực dữ liệu, định nghĩa các schema API và quản lý cấu hình từ biến môi trường.
-   **structlog** & **python-json-logger**: Thư viện để ghi log có cấu trúc, giúp việc phân tích log dễ dàng hơn.
-   **pytest** & **pytest-asyncio**: Framework để viết và chạy các bài test, hỗ trợ test các hàm bất đồng bộ.
-   **ruff** & **black**: Công cụ để đảm bảo chất lượng và tính nhất quán của code.

## 🛠️ Các Lệnh `Makefile`

`Makefile` cung cấp các lối tắt tiện lợi để quản lý môi trường Docker.

### Lệnh cho Môi trường Development

-   `make up-dev`:
    -   **Tác dụng**: Khởi chạy toàn bộ môi trường development (app + db).
    -   **Lệnh gốc**: `docker compose -f docker-compose.yml up --build`.
    -   **Ghi chú**: Tự động build lại image nếu có thay đổi và áp dụng migration DB khi khởi động.

-   `make down-dev`:
    -   **Tác dụng**: Dừng và dọn dẹp hoàn toàn môi trường dev (container, network, volume, image).
    -   **Lệnh gốc**: `docker compose down --rmi local --volumes`.

-   `make logs-dev`:
    -   **Tác dụng**: Theo dõi log của service `app` trong thời gian thực.

-   `make shell-dev`:
    -   **Tác dụng**: Mở một phiên shell (`/bin/sh`) bên trong container `app` để debug hoặc chạy lệnh thủ công.

-   `make migrate-dev`:
    -   **Tác dụng**: Áp dụng các migration đang chờ xử lý lên cơ sở dữ liệu dev.
    -   **Lệnh gốc**: `docker compose exec app poetry run alembic upgrade head`.

-   `make revision msg="<message>"`:
    -   **Tác dụng**: Tự động tạo một tệp migration mới dựa trên các thay đổi trong model SQLAlchemy.
    -   **Lệnh gốc**: `docker compose exec app poetry run alembic revision --autogenerate -m "<message>"`.

-   `make seed-dev`:
    -   **Tác dụng**: Chạy script `app/db/seed.py` để điền dữ liệu mẫu vào cơ sở dữ liệu.
    -   **Lệnh gốc**: `docker compose exec app poetry run python app/db/seed.py`.

-   `make test`:
    -   **Tác dụng**: Chạy bộ test của dự án bằng `pytest`.

### Lệnh cho Môi trường Production

-   `make up-prod`:
    -   **Tác dụng**: Khởi chạy môi trường production ở chế độ detached (`-d`).

-   `make down-prod`:
    -   **Tác dụng**: Dừng và xóa các container của môi trường production (không xóa volume và image để an toàn).

-   `make migrate-prod`:
    -   **Tác dụng**: Áp dụng các migration lên cơ sở dữ liệu production.
    -   **Lệnh gốc**: `docker compose -f docker-compose.prod.yml exec app ./.venv/bin/alembic upgrade head`.

### Lệnh Git

-   `make new-test-tag`:
    -   **Tác dụng**: Tạo một tag Git mới với định dạng `test-vX.Y.Z` và đẩy lên remote. Hữu ích cho việc đánh dấu các phiên bản thử nghiệm.