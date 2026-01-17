[app]
title = System Service
package.name = systemservice
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Requirements: Thêm android để hỗ trợ các hàm hệ thống
requirements = python3,kivy==2.3.0,pyjnius,android

orientation = portrait

# QUYỀN TRUY CẬP: Cực kỳ quan trọng để kết nối Socket
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# Cấu hình API ổn định cho GitHub Actions
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

# Buildozer settings
log_level = 2
warn_on_root = 0

[buildozer]
bin_dir = ./bin
