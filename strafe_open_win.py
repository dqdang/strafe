import subprocess
import time
import win32gui
import win32con


def call_strafe():
    cmd = ["python", "strafe_win.py"]
    ps = subprocess.Popen(
        cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

call_strafe()
time.sleep(1)
hwnd = win32gui.FindWindow(None, 'Strafe')
rect = win32gui.GetWindowRect(hwnd)
x = rect[0]
y = rect[1]
w = rect[2] - x
h = rect[3] - y
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, x, y, w, h, 0)
