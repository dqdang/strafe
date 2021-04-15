import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

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
