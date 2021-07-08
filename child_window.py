import tkinter as tk 

class ChildWindow(tk.Tk):
    def __init__(self,parent, w, h , title, resizable = [False, False] ):
        super().__init__()
        self = self.Toplevel(parent)
        self.title(title)
        self.geometry(f"{w}x{h}+200+200")
        self.resizable(resizable[0], resizable[1])
        