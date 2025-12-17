# 5. Quy trình Phát triển

Tài liệu này hướng dẫn các bước tiêu chuẩn để thêm một tính năng mới (ví dụ: quản lý `Products`) vào dự án.

## Bước 1: Tạo Model

Định nghĩa cấu trúc dữ liệu trong cơ sở dữ liệu.

1.  Tạo một tệp mới, ví dụ: `app/models/product.py`.
2.  Định nghĩa class `Product` kế thừa từ `Base` của SQLAlchemy.

```python
# app/models/product.py
from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
```

## Bước 2: Tạo và Áp dụng Migration

Cập nhật schema của cơ sở dữ liệu để khớp với model mới.

1.  **Tạo tệp migration**: Lệnh này sẽ so sánh các model hiện tại với schema trong DB và tạo ra một script thay đổi.
    ```bash
    make revision msg="Create product table"
    ```

2.  **Áp dụng migration**: Chạy script vừa tạo để cập nhật cơ sở dữ liệu.
    ```bash
    make migrate-dev
    ```

## Bước 3: Tạo Schemas (Pydantic)

Định nghĩa cấu trúc dữ liệu cho API (dữ liệu nhận vào và trả về).

1.  Tạo tệp mới, ví dụ: `app/schemas/product.py`.
2.  Định nghĩa các class schema như `ProductBase`, `ProductCreate`, `Product`.

## Bước 4: Tạo API Router

Xây dựng các API endpoint để tương tác với dữ liệu.

1.  Tạo tệp mới, ví dụ: `app/api/v1/products.py`.
2.  Viết các hàm xử lý request (ví dụ: `create_product`, `read_products`) sử dụng `db: Session = Depends(deps.get_db)` để lấy session DB.

## Bước 5: Đăng ký Router

Thêm router mới vào ứng dụng FastAPI chính.

1.  Mở tệp `app/main.py`.
2.  Import và `include_router` cho router `products`.

```python
# app/main.py
from app.api.v1 import products as products_router

app.include_router(products_router.router, prefix="/api/v1/products", tags=["Products"])
```