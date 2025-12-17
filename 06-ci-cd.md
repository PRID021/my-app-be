# 6. CI/CD và Kiểm tra Tự động

Dự án sử dụng **GitHub Actions** để xây dựng một pipeline Tích hợp Liên tục (Continuous Integration) mạnh mẽ.

## Tệp Workflow

-   **Vị trí**: `.github/workflows/test-dev.yml`
-   **Kích hoạt**: Pipeline này sẽ tự động chạy mỗi khi có một commit được đẩy lên nhánh `dev`.

## Các Job trong Pipeline

Pipeline bao gồm 2 job chính chạy tuần tự:

1.  `test`: Job chính thực hiện các bước kiểm tra.
2.  `coveralls-finish`: Job phụ thuộc, chạy sau khi `test` hoàn thành để gửi tín hiệu hoàn tất cho Coveralls.

## Chi tiết các Bước trong Job `test`

1.  **Checkout code**: Tải mã nguồn của nhánh hiện tại về máy ảo của GitHub.

2.  **Set up Python & Poetry**: Cài đặt phiên bản Python và Poetry đã định nghĩa.

3.  **Load cached venv**:
    -   Sử dụng `actions/cache` để kiểm tra xem có môi trường ảo (`.venv`) nào đã được lưu cache từ lần chạy trước không.
    -   Key của cache được tạo dựa trên hệ điều hành, phiên bản Python và hash của tệp `poetry.lock`. Nếu `poetry.lock` thay đổi, cache sẽ bị vô hiệu hóa và các dependency sẽ được cài lại.

4.  **Install dependencies**:
    -   Chỉ chạy nếu không tìm thấy cache hợp lệ (`if: steps.cached-poetry-dependencies.outputs.cache-hit != 'true'`).
    -   Sử dụng `poetry install` để cài đặt các dependency cần thiết cho việc test.

5.  **Lint with Ruff & Format with Black**: Chạy các công cụ kiểm tra chất lượng code để đảm bảo code tuân thủ các tiêu chuẩn đã định.

6.  **Run tests with Pytest**:
    -   Thực thi bộ test bằng `pytest`.
    -   Tạo báo cáo độ bao phủ test (`--cov=app`) dưới dạng tệp `coverage.xml`.

7.  **Upload coverage to Coveralls**: Tải tệp `coverage.xml` lên dịch vụ Coveralls.io để theo dõi và trực quan hóa độ bao phủ của test theo thời gian.