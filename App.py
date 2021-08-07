import tkinter as tk
from tkinter.constants import VERTICAL 
from Detail import Detail
from DrawMeta import DrawMeta 
import os
from data import *




class App(tk.Tk):
    def __init__(self):
        super().__init__() 

        self.arr = exp_type['circ']
        self.all_details = []
        self.geometry('800x600')

        self.btn_circ = tk.Button(self, text= 'cirlce' , command= lambda : self.refresh('circ'))
        self.btn_circ.pack()

        self.btn_rect = tk.Button(self, text= 'rect' , command= lambda: self.refresh('rect'))
        self.btn_rect.pack()


        self.draw_meta = DrawMeta(self)
        self.draw_meta.pack(fill=tk.BOTH)





        self.form_canvas = tk.Canvas(self,bg='lightgreen')
        self.form_canvas.pack(side=tk.LEFT, fill= tk.BOTH , expand=1)

        self.form_frame = tk.Frame(self.form_canvas , bg='lightblue')

        self.scrollbar = tk.Scrollbar(self.form_canvas, orient=VERTICAL, command=self.form_canvas.yview)

        self.scrollbar.pack(side=tk.RIGHT, fill= tk.Y)

        self.form_canvas.configure(yscrollcommand=self.scrollbar.set)


        self.form_canvas.bind('<Configure>', self.task_width)



        self.canvas_frame = self.form_canvas.create_window((0,0), window=self.form_frame, anchor='nw',)

        self.put_details()
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



    def put_details(self):
        
        for idx, d in enumerate(self.arr): 
            detail = Detail(self.form_frame,d)
            self.all_details.append(detail)
            pos_num = divmod(idx,2)[1]
            if pos_num==0:
                detail.grid(row=idx, column=0,sticky='s')
               
            else :
                detail.grid(row=idx-1, column=1 ,sticky='n')
                


    def refresh(self,fej_type):
        self.arr = exp_type[fej_type]
        print(fej_type)

        all_frames = [f for f in self.all_details]
        for f_name in all_frames:
            self.nametowidget(f_name).destroy()
        self.all_details = []
        self.put_details()
        print('все детали',self.all_details)




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

        draw_name = self.draw_meta.meta_info()
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
    b = App()
    b.mainloop()
