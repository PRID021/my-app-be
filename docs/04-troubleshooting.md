# 4. Gỡ lỗi các Vấn đề Thường gặp

Đây là danh sách các lỗi phổ biến có thể xảy ra trong quá trình phát triển và cách khắc phục chúng.

---

### 1. Lỗi: `ModuleNotFoundError: No module named 'psycopg2'`

-   **Nguyên nhân**: Script đang chạy (ví dụ: `seed.py` hoặc `alembic`) sử dụng engine SQLAlchemy đồng bộ, yêu cầu driver `psycopg2`, nhưng driver này chưa được cài đặt.
-   **Giải pháp**: Thêm `psycopg2-binary = "*"` vào tệp `pyproject.toml` và build lại Docker image (`make up-dev`).

---

### 2. Lỗi: `ImportError: cannot import name '...' from partially initialized module (most likely due to a circular import)`

-   **Nguyên nhân**: Xảy ra một vòng lặp import. Ví dụ: `models/post.py` import từ `db/base.py`, và `db/base.py` lại import ngược lại từ `models/post.py`.
-   **Giải pháp**: Phá vỡ vòng lặp. Di chuyển các import model (ví dụ: `from app.models.post import Post`) từ `db/base.py` vào tệp `db/migrations/env.py`. Đây là nơi Alembic cần chúng để tự động phát hiện model.

---

### 3. Lỗi: `AttributeError: module 'app.schemas' has no attribute 'Post'`

-   **Nguyên nhân**: Lệnh `from app import schemas` chỉ import package `schemas`, chứ không import các module bên trong nó.
-   **Giải pháp**: Import trực tiếp và cụ thể hơn. Thay đổi `from app import schemas` và `schemas.Post` thành `from app.schemas.post import Post as PostSchema`. Việc sử dụng alias (`as PostSchema`) là một good practice để tránh xung đột tên với model SQLAlchemy.

---

### 4. Lỗi: `FAILED: No config file 'alembic.ini' found`

-   **Nguyên nhân**: Lệnh `alembic` được chạy bên trong container nhưng không tìm thấy tệp `alembic.ini`.
-   **Giải pháp**: Đảm bảo rằng `Dockerfile.dev` có một lệnh `COPY alembic.ini ./` để sao chép tệp cấu hình vào working directory của container.

---

### 5. Lỗi: `dependency failed to start: container my_postgres_db is unhealthy`

-   **Nguyên nhân**: Lệnh `healthcheck` trong `docker-compose.yml` cho service `db` bị lỗi. Thường là do các biến môi trường như `${POSTGRES_USER}` không được thay thế đúng cách.
-   **Giải pháp**: Sử dụng cú pháp `$$` để escape biến, cho phép shell bên trong container tự thay thế.
    ```yaml
    healthcheck:
      test: ["CMD-SHELL", "sh -c 'pg_isready -U $$POSTGRES_USER -d $$POSTGRES_DB'"]
    ```

---

### 6. Lỗi: `Import "..." could not be resolved` trong VS Code

-   **Nguyên nhân**: VS Code đang không sử dụng đúng Python interpreter từ môi trường ảo (`.venv`) mà Poetry đã tạo.
-   **Giải pháp**: Mở Command Palette (`Ctrl+Shift+P`), chọn `Python: Select Interpreter` và chọn interpreter có nhãn **(Poetry)**. Chi tiết xem tại tệp `02-setup.md`.

---

### 7. Lỗi: `ModuleNotFoundError: No module named 'sqlalchemy'` trong GitHub Actions

-   **Nguyên nhân**: Lệnh `poetry install --only dev` trong workflow của GitHub Actions chỉ cài đặt các gói trong group `dev`, bỏ qua các dependency chính của ứng dụng như `sqlalchemy` hay `fastapi`. Tuy nhiên, các bài test lại cần những dependency này để import và chạy.
-   **Giải pháp**: Xóa cờ `--only dev` khỏi lệnh `poetry install` trong tệp `.github/workflows/test-dev.yml`. Lệnh đúng phải là `poetry install --no-interaction --no-root` để cài đặt tất cả các dependency cần thiết.
