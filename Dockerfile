FROM python:3.11-slim

WORKDIR /app

# Cài đặt Poetry
RUN pip install --no-cache-dir poetry

# Cấu hình Poetry để không tạo môi trường ảo bên trong project
# và để cài đặt các thư viện vào site-packages của hệ thống.
RUN poetry config virtualenvs.create false

# Sao chép các file cần thiết để cài đặt thư viện
# Điều này tận dụng cache của Docker, chỉ cài lại khi các file này thay đổi
COPY pyproject.toml poetry.lock* ./

# Cài đặt tất cả các thư viện (production và development)
RUN poetry install --no-interaction --no-ansi --no-root

COPY . .

ENTRYPOINT ["/app/entrypoint.sh"]