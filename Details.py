import tkinter as tk
from tkinter.constants import VERTICAL 
from Detail import Detail
import os

shapes = [

    ['circle','radius','calc_circle_area'],
    ['rectangular', 'width', 'height','calc_rectangular_area'],
    ['гибкая вставка ', 'L', 'D','calc_rectangular_area'],

     ]


dogs= [ 
        ["boc", 'red', 'tail', 'test_func'], 
        ["boc", 'red', 'tail', 'test_func'],
        ["boc", 'red', 'tail', 'test_func'],
        ["boc", 'red', 'tail', 'test_func'],
]

data = {'shapes': shapes, 'dogs': dogs}


class Details(tk.Tk):
    def __init__(self,arr):
        super().__init__()
        self.arr = arr
        self.all_details = []
        self.geometry('500x500')
        self.profile = 'shapes'


        self.form_frame = tk.Frame(self, bg='coral')
        self.form_frame.pack(fill=tk.BOTH, expand=1)

        self.form_canvas = tk.Canvas(self.form_frame,bg='lightgreen')
        self.form_canvas.pack(side=tk.LEFT, fill= tk.BOTH , expand=1)

        self.scrollbar = tk.Scrollbar(self.form_canvas, orient=VERTICAL, command=self.form_canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill= tk.Y)

        self.form_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.form_canvas.bind('<Configure>', lambda e: self.form_canvas.configure(scrollregion=self.form_canvas.bbox("all")))

        self.second_frame = tk.Frame(self.form_canvas,bg='grey')
        self.second_frame.pack(side=tk.TOP ,fill=tk.X)

        self.form_canvas.create_window((0,0), window=self.second_frame, anchor='nw',)

        for d in self.arr: 
            detail = Detail(self.second_frame,d)
            self.all_details.append(detail)
            detail.pack(pady=10)
# 
# 
# 
        self.btn = tk.Button(self, text='расчет', bg='lightblue',font=("Arial",15))
        self.btn.bind("<Button-1>", self.calc_all_forms)
        self.btn.pack(side=tk.TOP,)
# 
# 
# 
        self.btn_profile_shapes = tk.Button(self, text= 'shapes', )
        self.btn_profile_shapes.pack(side=tk.TOP, )
        
        self.btn_profile_dogs = tk.Button(self, text= 'dogs', )
        self.btn_profile_dogs.pack(side=tk.TOP, )

    def set_profile(self,e,profile):
        print(profile)
        self.profile = profile

    def calc_all_forms(self,evt = None):
        for d in self.all_details: 
            d.func()

    def run(self): 
        self.mainloop()



if __name__ == "__main__":
    b = Details(data['dogs'])
    b.mainloop()
