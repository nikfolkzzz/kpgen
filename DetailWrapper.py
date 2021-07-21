import tkinter as tk
from tkinter.constants import VERTICAL
from typing import Text 
from Detail import Detail
 
from Details import Details
import os
from data import *
from tkinter.ttk import Notebook


class Wrapper(tk.Tk):
    def __init__(self,data):
        super().__init__()

        self.data = data
        self.geometry('600x600')

                # TABS
        self.notebook = Notebook(self)
        self.notebook.pack(pady= 20 )

        self.shapes_frame  = tk.Frame(self.notebook , bg='red' ,width=600, height=600)
        self.dogs_frame = tk.Frame(self.notebook, bg='blue' ,width=600, height=600)

        self.shapes_frame.pack(fill=tk.BOTH , expand=1 )
        self.dogs_frame.pack(fill=tk.BOTH , expand=1 )

        self.notebook.add(self.shapes_frame , text = 'shapes')
        self.notebook.add(self.dogs_frame, text = 'dogs')

        self.s = Details(self.shapes_frame,self.data['shapes'])
        self.s.pack(side=tk.TOP , expand=1 )    


        self.d = Details(self.dogs_frame,self.data['dogs'])
        self.d.pack(side=tk.TOP)


        # TABS



if __name__ == "__main__":
    r = Wrapper(data)
    r.mainloop()

