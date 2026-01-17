[app]
title = My Application
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Requirements chuẩn nhất cho 2026
requirements = python3,kivy==2.3.0,pyjnius,android

orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.3.0

# Android specific
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# Buildozer specific
log_level = 2
warn_on_root = 0

[buildozer]
bin_dir = ./bin
