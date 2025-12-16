import pytest
from httpx import AsyncClient
from starlette import status

# Đánh dấu tất cả các test trong file này là test asyncio
pytestmark = pytest.mark.asyncio


async def test_create_post(client: AsyncClient):
    """
    Test a-pi tạo một bài viết mới.
    """
    # Dữ liệu đầu vào
    post_data = {"title": "Test Title", "content": "Test Content"}

    # Gửi request POST
    response = await client.post("/api/v1/posts/", json=post_data)

    # Kiểm tra response
    assert response.status_code == status.HTTP_201_CREATED

    # Kiểm tra nội dung response
    response_data = response.json()
    assert response_data["title"] == post_data["title"]
    assert response_data["content"] == post_data["content"]
    assert "id" in response_data
    assert "created_at" in response_data


async def test_get_all_posts_empty(client: AsyncClient):
    """
    Test lấy danh sách bài viết khi database rỗng.
    """
    response = await client.get("/api/v1/posts/")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []


async def test_get_all_posts_with_data(client: AsyncClient):
    """
    Test lấy danh sách bài viết sau khi đã tạo một bài.
    """
    # Tạo một bài viết trước
    post_data = {"title": "Another Post", "content": "Some more content"}
    await client.post("/api/v1/posts/", json=post_data)

    # Lấy danh sách
    response = await client.get("/api/v1/posts/")

    # Kiểm tra
    assert response.status_code == status.HTTP_200_OK

    response_data = response.json()
    assert len(response_data) == 1
    assert response_data[0]["title"] == post_data["title"]
