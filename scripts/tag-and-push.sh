#!/bin/sh

# Dừng script nếu có lỗi
set -e

# Lấy các tag mới nhất từ remote để đảm bảo chúng ta có thông tin cập nhật
echo "Fetching latest tags from origin..."
git fetch --tags

# Tìm tag mới nhất có dạng 'test-v*'
# `2>/dev/null` để ẩn lỗi nếu không tìm thấy tag nào
LATEST_TAG=$(git describe --tags --match "test-v*" --abbrev=0 2>/dev/null)

# Nếu không tìm thấy tag nào, bắt đầu từ v0.1.0
if [ -z "$LATEST_TAG" ]; then
  echo "No existing 'test-v*' tags found. Starting with test-v0.1.0"
  NEW_TAG="test-v0.1.0"
else
  echo "Latest tag found: $LATEST_TAG"

  # Xóa tiền tố 'test-v' để lấy chuỗi phiên bản
  VERSION=$(echo $LATEST_TAG | sed 's/test-v//')

  # Tách phiên bản thành các phần MAJOR.MINOR.PATCH
  MAJOR=$(echo $VERSION | cut -d. -f1)
  MINOR=$(echo $VERSION | cut -d. -f2)
  PATCH=$(echo $VERSION | cut -d. -f3)

  # Tăng số PATCH lên 1
  NEW_PATCH=$((PATCH + 1))

  # Tạo tên tag mới
  NEW_TAG="test-v$MAJOR.$MINOR.$NEW_PATCH"
fi

echo "Creating and pushing new tag: $NEW_TAG"
git tag $NEW_TAG
git push origin $NEW_TAG

echo "Successfully pushed tag $NEW_TAG to origin."