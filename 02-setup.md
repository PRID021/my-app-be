# 2. Cài đặt và Cấu hình

Dự án được thiết kế để chạy chủ yếu với Docker, đảm bảo tính nhất quán giữa các môi trường.

## 🚀 Môi trường Development (Docker)

Đây là cách được khuyến khích để phát triển.

1.  **Tạo tệp môi trường:**
    Sao chép tệp `.env.docker.example` thành `.env.docker`.
    ```bash
    cp .env.docker.example .env.docker
    ```
    Tệp này chứa các biến môi trường cho cả service `db` và `app`.

2.  **Khởi chạy môi trường:**
    Sử dụng `Makefile` để khởi chạy các service. Lệnh này sẽ build image và khởi động các container.
    ```bash
    make up-dev
    ```

#### Quá trình khởi động (`entrypoint.dev.sh`)

Khi container `app` khởi động, script `entrypoint.dev.sh` sẽ tự động thực thi:
1.  Chạy `poetry run alembic upgrade head` để đảm bảo schema của cơ sở dữ liệu luôn được cập nhật lên phiên bản mới nhất.
2.  Khởi chạy server Uvicorn với chế độ auto-reload.

#### Biến môi trường (`.env.docker`)

-   `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`: Cấu hình cho service PostgreSQL để tạo người dùng và cơ sở dữ liệu ban đầu.
-   `DATABASE_URL`: Chuỗi kết nối mà ứng dụng FastAPI sử dụng để kết nối đến cơ sở dữ liệu. Lưu ý rằng host là `db`, tên của service PostgreSQL trong `docker-compose.yml`.
-   `LOG_LEVEL`: Cấp độ log (ví dụ: `INFO`, `DEBUG`).
-   `JSON_LOGGING`: Đặt thành `true` trong môi trường production để xuất log dưới dạng JSON.

## Môi trường Production (Docker)
 
Môi trường production sử dụng một `Dockerfile` đa giai đoạn để tạo ra một image nhỏ và an toàn hơn, cùng với một tệp `docker-compose.prod.yml` riêng biệt.

1.  **Tạo tệp môi trường production:**
    Tạo một tệp `.env.prod` với các thông tin xác thực và cấu hình cho môi trường production.

2.  **Khởi chạy môi trường:**
    Sử dụng lệnh `make` dành riêng cho production.
    ```bash
    make up-prod
    ```
    Lệnh này sẽ:
    -   Build image production bằng `Dockerfile`.
    -   Khởi chạy các service trong chế độ detached (`-d`).
    -   Sử dụng `gunicorn` để quản lý các worker `uvicorn`, mang lại hiệu suất và sự ổn định tốt hơn.

## 💻 Cấu hình Visual Studio Code

Để VS Code nhận diện đúng các thư viện đã cài đặt và cung cấp gợi ý code chính xác, bạn cần chọn đúng Python Interpreter.

1.  Mở Command Palette: `Ctrl+Shift+P` (hoặc `Cmd+Shift+P` trên macOS).
2.  Gõ và chọn `Python: Select Interpreter`.
3.  Chọn interpreter có đường dẫn chứa `.venv` và có nhãn **(Poetry)**. Ví dụ:
    ```
    Python 3.11.x ('.venv': Poetry)
    ./.venv/bin/python
    ```
Điều này sẽ giúp Pylance (công cụ phân tích code của VS Code) tìm thấy các gói như `structlog`, `fastapi`, v.v.

## ⚙️ Cài đặt không dùng Docker

1.  Cài đặt Poetry.
2.  Chạy `poetry install` để cài đặt các dependency.
3.  Thiết lập một database PostgreSQL cục bộ.
4.  Export biến môi trường `DATABASE_URL` trong terminal của bạn.
5.  Chạy `poetry run uvicorn app.main:app --reload`.