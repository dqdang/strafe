@echo off
rmdir /q /s build
rmdir /q /s dist
pyinstaller strafe_win.py --hidden-import=pkg_resources --onefile --noconsole --icon icon.ico
xcopy icon.ico dist
