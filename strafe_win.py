import time
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import threading
import win32gui
import win32con

class TkinterThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        root = tk.Tk()
        root.title("Strafe")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        font = "Times New Roman"
        root.geometry("300x160")
        root.resizable(width=True, height=True)

        text_area = scrolledtext.ScrolledText(root,
                                              wrap=tk.WORD,
                                              width=25,
                                              height=10,
                                              font=(font,
                                                    15),)

        text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        text_area.focus()
        root.lift()

        tk.mainloop()

class FocusWindowThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        hwnd = win32gui.FindWindow(None, 'Strafe')
        while hwnd == 0:
            hwnd = win32gui.FindWindow(None, 'Strafe')

        rect = win32gui.GetWindowRect(hwnd)
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, x, y, w, h, 0)


if __name__ == "__main__":
    thread1 = TkinterThread(1, "Thread-1", 1)
    thread2 = FocusWindowThread(2, "Thread-2", 2)
    thread1.start()
    time.sleep(1)
    thread2.start()
