@echo on
pyinstaller strafe_win.py --hidden-import=pkg_resources --onefile --noconsole --icon icon.icon
xcopy icon.ico dist