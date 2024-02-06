# main.py
import tkinter as tk
from src.gui import HRMGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = HRMGUI(root)
    root.mainloop()
