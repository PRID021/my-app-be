#!/bin/sh

# Chờ database sẵn sàng và chạy migrations
echo "Waiting for postgres..."

# Vòng lặp để thử chạy migration, nếu thất bại, đợi và thử lại
# Điều này giúp đảm bảo app chỉ khởi động khi database đã sẵn sàng
while ! python -m alembic upgrade head; do
  echo "Migration failed, retrying in 5 seconds..."
  sleep 5
done

echo "PostgreSQL started and migrations applied"

# Chạy lệnh được truyền vào (CMD từ Dockerfile)
# exec "$@" sẽ thay thế tiến trình shell bằng tiến trình uvicorn
exec "$@"
