import os
import cv2

# Đường dẫn tới thư mục chứa các ảnh cần thay đổi kích thước
path = r"F:\HK6 2022-2023\AI\CODE_VID\TEST"

# Đường dẫn tới thư mục mới để lưu các ảnh đã chỉnh sửa
new_path = r"F:\HK6 2022-2023\AI\CODE_VID\TEST_FIX"

# Kích thước mới của ảnh
new_size = (1280, 1280)

# Điều chỉnh kích thước và đổi đuôi ảnh cho tất cả các ảnh trong thư mục
for filename in os.listdir(path):
    # Kiểm tra xem tệp có phải là file ảnh không
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        # Đọc ảnh từ file
        img = cv2.imread(os.path.join(path, filename))
        # Thay đổi kích thước ảnh
        img_resized = cv2.resize(img, new_size)
        # Tạo tên tệp mới cho ảnh đổi kích thước
        new_filename = os.path.splitext(filename)[0] + "_resized.jpg"
        # Ghi ảnh mới vào thư mục mới với định dạng .jpg
        cv2.imwrite(os.path.join(new_path, new_filename), img_resized, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
        # Xóa ảnh cũ
        os.remove(os.path.join(path, filename))