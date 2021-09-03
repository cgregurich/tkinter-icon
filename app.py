from tkinter import *

root = Tk()

root.title("booter")
root.iconbitmap("images/mycon.ico")
root.mainloop()


# pyinstaller --icon "images/mycon.ico" --add-data "images;images" -w app.py