from tkinter import PhotoImage, scrolledtext

import base64
import os
import sys
import time
import tkinter as tk
import threading
import win32gui
import win32con

state_name = "state.txt"
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)
state_path = os.path.join(application_path, state_name)

class TkinterThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.dark_mode = True

    def run(self):
        img = \
        """
        iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAATlBMVEUAAAABAQF9fX2ZmZmsrKyL
        i4u2trYHBwd5eXm0tLSdnZ2Dg4OJiYmoqKiRkZGNjY36+vr09PTk5OTW1tbMzMzExMS9vb1qampj
        Y2NpaWk2P5IbAAACsklEQVR4nO3djXKaQBSG4bMYWFTU1sakvf8b7fIjYjqthOqY7+z7jjNBg2Ef
        EIwjMfbt+/HH6+upqtbrl91uM7TaH8oyXboOZbMtirpY1LYp/1W7mP1qs7rZ5mVO62rS27o67Y62
        Md+9W2UxWrAwKd0+TpwLi7q5/PN8w5zXX66ufmKhw9fYXqyxXRLGePmmTeaZDGPJ6ptzv2VrbrYw
        Wp2EwUbhZCYL/z+K/r63jDZr9c1b3tW12N5S2Kr12QfifR6lZ8Htcd+J+GG22N5QpCNNq41/LvRT
        I/3bmGaMbM52nr28MPlhvatO23DJ4CUK50fp3dbhVwuhfgj1y0bYPR/6fL4YtyFC2QbhPguh00PN
        ICzdCxv3wnLxS/gvH0L9EOqHUD+E+iHUD6F+CPVDqB9C/RDqh1A/hPoh1C8bYdNNPnswD2kQbs27
        sDhP+usi9LojDsLa/TukdX/a87NH84guQvN9Lob//bBweyhF6CCE+iHUD6F+CPVDqB9C/RDqh1A/
        hPoh1A+hfgj1m75D6v2dGYSqIdQPoX7jOVFe3+TO57w2hMIh1A+hfgj1Q6gfQv0Q6odQP4T6IdQP
        oX4I9UOoH0L9EOqHUL9shIcshL7/Hr80p1tw+vk0XonjNvR+9uXe3G7EQdj9Z7kMhC6JF6FTIEIH
        IdQPoX4I9UOoH0L9EOqHUD+E+iHUD6F+CPVDqB9C/RDqh1C/bIQb98IXt0CEDkKoH0L9EOqHUD+E
        +iHUD6F+CPVDqB9C/RDqh1A/hPoh1A+hfpkJXRonQt+f/OFfuDavu2E+wioLoVPjldAlcSp0fSxF
        KBxC/RDqN/7WFmOw+OzRPKB+w9VpG/bT7rLYqjph8CkM0UJC9q8tfD5KbRCeLO2ISfjsNf6AYnuk
        2abX+L57t+PPpq63hcM61a+339l2GAd91T5eAAAAAElFTkSuQmCC
        """
        root = tk.Tk()
        img = base64.b64decode(img)
        img = PhotoImage(data=img)
        root.wm_iconphoto(True, img)
        root.wm_iconbitmap("icon.ico")
        root.title("Strafe")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        font = "Source Code Pro"
        root.geometry("300x160")
        root.resizable(width=True, height=True)
        root.configure(bg="black")

        text_area = scrolledtext.ScrolledText(root,
                                              wrap=tk.WORD,
                                              width=25,
                                              height=10,
                                              font=(font,
                                                    15),)

        text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        #dark mode
        if(self.dark_mode):
            text_area.config(background="#1D1F21",
                            foreground="white",
                            insertbackground = 'white',
                            selectforeground = 'black',
                            selectbackground = 'gray20',
                            highlightbackground = 'gray20',
                            highlightcolor      = 'gray10',)

        thread3 = AutoSaveThread(3, "Thread-3", 3, text_area)
        try:
            with open(state_path, "r") as state:
                lines = state.readlines()
                for line in lines:
                    print("Now inserting line: " + line)
                    text_area.insert(tk.INSERT, line)
        except FileNotFoundError:
            text_area.insert(tk.INSERT, "")

        text_area.focus()
        root.lift()
        thread3.start()

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

class AutoSaveThread(threading.Thread):
    def __init__(self, threadID, name, counter, text_area):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.text_area = text_area
        self.first_pass = True

    def run(self):
        while True: 
            if(not self.first_pass):
                with open(state_path, "w") as f:
                    state = self.text_area.get("1.0", tk.END).rstrip("\n")
                    print("Now writing line: " + state)
                    f.write(state)
            else:
                self.first_pass = False
            # autosave every 10 seconds
            time.sleep(10)


if __name__ == "__main__":
    thread1 = TkinterThread(1, "Thread-1", 1)
    thread2 = FocusWindowThread(2, "Thread-2", 2)
    thread1.start()
    time.sleep(1)
    thread2.start()
