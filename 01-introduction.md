# 1. Giới thiệu Dự án

Đây là tài liệu chuyển giao cho dự án backend được xây dựng với FastAPI. Mục tiêu của dự án là cung cấp một nền tảng API hiệu suất cao, dễ dàng mở rộng và bảo trì, sẵn sàng cho môi trường production.

## 🎯 Triết lý Dự án (Project Philosophy)

-   **Clean Code**: Tuân thủ các nguyên tắc code sạch, dễ đọc và dễ hiểu.
-   **Môi trường nhất quán**: Sử dụng Docker để đảm bảo môi trường development, testing và production giống hệt nhau, loại bỏ lỗi "it works on my machine".
-   **Tự động hóa**: Tự động hóa tối đa các quy trình kiểm tra code (linting, formatting, testing) thông qua CI/CD.
-   **Tài liệu hóa**: Mọi thành phần quan trọng của dự án đều cần được ghi lại rõ ràng.

## ✨ Các Tính năng Chính

- **Framework**: **FastAPI** cho hiệu suất API cao, dễ học và code nhanh.
- **Database**: **PostgreSQL** làm cơ sở dữ liệu quan hệ.
- **ORM**: **SQLAlchemy 2.0** cho các tương tác cơ sở dữ liệu mạnh mẽ và bất đồng bộ.
- **Migrations**: **Alembic** để quản lý các thay đổi schema của cơ sở dữ liệu.
- **Data Validation**: **Pydantic** để xác thực dữ liệu và quản lý cấu hình.
- **Containerization**: **Docker** và **Docker Compose** cho môi trường phát triển và production nhất quán.
- **Dependency Management**: **Poetry** để quản lý dependency một cách hiện đại và có thể dự đoán.
- **Testing**: **Pytest** với `pytest-asyncio` cho việc test bất đồng bộ.
- **Code Quality**:
  - **Ruff** để linting Python siêu nhanh.
  - **Black** để format code một cách thống nhất.
- **CI/CD**: **GitHub Actions** để tự động chạy test, linting và kiểm tra format code trên mỗi push lên nhánh `dev`.
- **Code Coverage**: **Coveralls** để theo dõi độ bao phủ của test.

## 📁 Cấu trúc Thư mục

Dưới đây là giải thích về cấu trúc thư mục chính của dự án:

```
.
├── .github/                    # Các workflow của GitHub Actions
│   └── workflows/
│       └── test-dev.yml        # Pipeline CI/CD cho nhánh 'dev'
├── app/                        # Mã nguồn chính của ứng dụng
│   ├── api/                    # Các router cho API endpoints
│   ├── core/                   # Các logic lõi (settings, config, logging)
│   ├── db/                     # Các module liên quan đến cơ sở dữ liệu
│   │   ├── migrations/         # Các script migration của Alembic
│   │   ├── deps.py             # Dependency Injection cho database session
│   │   └── session.py          # Khởi tạo SQLAlchemy session
│   ├── models/                 # Các model ORM của SQLAlchemy
│   ├── schemas/                # Các schema Pydantic để xác thực dữ liệu
│   └── main.py                 # Điểm vào (entrypoint) của ứng dụng FastAPI
├── docs/                       # Thư mục tài liệu dự án
├── .env.docker.example         # Biến môi trường mẫu cho Docker
├── alembic.ini                 # Tệp cấu hình của Alembic
├── docker-compose.yml          # Cấu hình Docker Compose cho môi trường dev
├── docker-compose.prod.yml     # Cấu hình Docker Compose cho môi trường prod
├── Dockerfile                  # Dockerfile cho môi trường production
├── Dockerfile.dev              # Dockerfile cho môi trường development
├── entrypoint.dev.sh           # Script entrypoint cho môi trường dev
├── Makefile                    # Các lệnh để quản lý dự án
├── poetry.lock                 # Tệp lock của Poetry để đảm bảo build nhất quán
└── pyproject.toml              # Tệp cấu hình dự án cho Poetry
```