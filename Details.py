import tkinter as tk 
from Detail import Detail
import os

shapes = [

    ['circle','radius','calc_circle_area'],
    ['rectangular', 'width', 'height','calc_rectangular_area'],
    ['rectangular', 'width', 'height','calc_rectangular_area'],
    ['rectangular', 'width', 'height','calc_rectangular_area'],
    ['rectangular', 'width', 'height','calc_rectangular_area'],
    ['rectangular', 'width', 'height','calc_rectangular_area'],
    ['rectangular', 'width', 'height','calc_rectangular_area'],
    ['rectangular', 'width', 'height','calc_rectangular_area'],

    ]

class Details(tk.Tk):
    def __init__(self,arr):
        super().__init__()
        self.arr = arr
        self.all_details = []


        self.form_canvas = tk.Canvas(self)

        self.form_frame = tk.Frame(self.form_canvas)


        self.scrollbar = tk.Scrollbar(self.form_canvas, orient='vertical', command=self.form_canvas.yview)

        self.form_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.geometry('500x500')

        self.form_canvas.pack(side=tk.TOP , fill=tk.BOTH ,expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.form_frame.pack(side=tk.BOTTOM, fill=tk.X , expand=1)

        self.bind_all("<MouseWheel>", self.mouse_scroll)

        self.canvas_frame = self.form_canvas.create_window((100, 0), window=self.form_frame, anchor="n")


        for d in self.arr: 
            detail = Detail(self.form_frame,d)
            self.all_details.append(detail)
            detail.pack(pady=10)


        self.btn = tk.Button(self, text='расчет', bg='lightblue',font=("Arial",15))
        self.btn.bind("<Button-1>", self.calc_all_forms)
        self.btn.pack(side=tk.TOP,)


    def calc_all_forms(self,evt = None):
        for d in self.all_details: 
            d.func()

    def run(self): 
        self.mainloop()

    def mouse_scroll(self, event): 
        if event.delta: 
            self.form_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        # если есть изменения в значении скрола, то в метод изменения скролинга передаем цифры 

        else: 
            if event.num == 5: 
                move = 1

            else:
                 move = -1 

            self.form_canvas.yview_scroll(move,"units")

if __name__ == "__main__":
    b = Details(shapes)
    b.mainloop()
