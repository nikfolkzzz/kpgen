import tkinter as tk
from tkinter.constants import VERTICAL 
from Detail import Detail
import os
from data import *



class Details(tk.Tk):
    def __init__(self,arr):
        super().__init__()


        self.arr = arr
        self.all_details = []
        self.geometry('500x500')
        self.profile = 'shapes'

        self.draw_num_label = tk.Label(self, text = 'Номер чертежа квадратного!!! компенсатора', bg='pink')
        self.draw_num_entry = tk.Entry(self,)

        self.draw_num_label.pack(side=tk.TOP,)
        self.draw_num_entry.pack(side=tk.TOP,)




        self.form_canvas = tk.Canvas(self,bg='lightgreen')
        self.form_canvas.pack(side=tk.LEFT, fill= tk.BOTH , expand=1)

        self.form_frame = tk.Frame(self.form_canvas , bg='lightblue')

        self.scrollbar = tk.Scrollbar(self.form_canvas, orient=VERTICAL, command=self.form_canvas.yview)

        self.scrollbar.pack(side=tk.RIGHT, fill= tk.Y)

        self.form_canvas.configure(yscrollcommand=self.scrollbar.set)


        self.form_canvas.bind('<Configure>', self.task_width)



        self.canvas_frame = self.form_canvas.create_window((0,0), window=self.form_frame, anchor='nw',)

        for d in self.arr: 
            detail = Detail(self.form_frame,d)
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


        self.bind("<Configure>", self.on_frame_configure)

        self.bind_all("<MouseWheel>", self.mouse_scroll)    



    def task_width(self,e): 
        # canvas_width = e.width
        self.form_canvas.itemconfig(self.canvas_frame, width = e.width)

    def mouse_scroll(self, event): 
            if event.delta: 
                self.form_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
            else: 
                if event.num == 5: 
                    move = 1

                else:
                    move = -1 

                self.form_canvas.yview_scroll(move,"units")

    def calc_all_forms(self,evt = None):
        # https://pypi.org/project/htmltabletomd/ - html to md 
        table_strings = []

        draw_name = self.draw_num_entry.get()
        table_strings.append(draw_name)
        all_price = []

        for d in self.all_details: 
            answer_string = d.func()['answer']
            one_detail_cost = d.func()['cost']
            all_price.append(one_detail_cost)
            table_strings.append(f'{answer_string}\n')

        table_strings.append(f'цена компенсатора по чертежу {draw_name} : {str(sum(all_price))}₽')
        table_strings_formated = ''.join(table_strings)
        table = f'''
            {table_strings_formated}
        
         '''
        with open(f'{draw_name}.txt','w', encoding='utf-8') as tb:
            print(table, file=tb)





    def on_frame_configure(self, event=None):
      self.form_canvas.configure(scrollregion=self.form_canvas.bbox("all"))    

    def run(self): 
        self.mainloop()



if __name__ == "__main__":
    b = Details(rect_2ug)
    b.mainloop()
