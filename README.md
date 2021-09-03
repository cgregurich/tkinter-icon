Create .exe by running this command in the main project directory:

`pyinstaller --icon "images/mycon.ico" --add-data "images;images" -w app.py`

`root.iconbitmap("images/mycon.ico")` changes the icon of the application in the Tkinter window. So even if you run it as a Python program, the icon in the window bar will change, but not in the taskbar of your computer.

using the `--icon "images/mycon.ico"` flag in the pyinstaller command changes the icon of the actual program's .exe.
