@echo on
pyinstaller strafe_win.py --hidden-import=pkg_resources --onefile --noconsole 
