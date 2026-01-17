[app]
# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# QUAN TRỌNG: Cố định phiên bản Kivy và Cython để tránh lỗi máy chủ
requirements = python3,kivy==2.1.0,pyjnius,android

# (str) Supported orientations
orientation = portrait

# -----------------------------------------------------------------------------
# Android specific
# -----------------------------------------------------------------------------

# (int) Android API to use
# Dùng API 31 để ổn định nhất trên GitHub Actions hiện tại
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 31

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (list) Android architectures to build for
# Build cho cả điện thoại đời cũ và đời mới
android.archs = armeabi-v7a, arm64-v8a

# (bool) Allow skipping setup.py check
android.skip_setup_py = True

# -----------------------------------------------------------------------------
# Buildozer specific
# -----------------------------------------------------------------------------

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = no, 1 = yes)
warn_on_root = 0

[buildozer]
# (str) Path to build artifacts
bin_dir = ./bin
