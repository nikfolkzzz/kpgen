import tkinter as tk
from tkinter.constants import VERTICAL 
from Detail import Detail
from DrawMeta import DrawMeta 
import os
from data import *
from MainMenu import MainMenu



class App(tk.Tk):
    def __init__(self):
        super().__init__() 

        # self.tk.call('source', 'azure.tcl / azure-dark.tcl')
        # self.ttk.Style().theme_use('azure / azure-dark')
        self.geometry('800x600')
        self.arr = exp_type['circ']
        self.all_details = []
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
        self.put_menu()
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




    def put_menu(self):
        self.config(menu = MainMenu(self))

    def put_details(self):

        mp = self.draw_meta.meta_info()['metall_price']
        fp = self.draw_meta.meta_info()['fabric_price']
        bp = self.draw_meta.meta_info()['draw_num']

        for idx, d in enumerate(self.arr): 
            detail = Detail(self.form_frame,d,mp,fp,bp)
            self.all_details.append(detail)
            pos_num = divmod(idx,2)[1]
            detail.grid(row=idx, column=0,sticky='ew')
               

                
    def quit(self):
        self.destroy()


    def refresh(self,fej_type):
        self.arr = exp_type[fej_type]
        print(fej_type)


        for f_name in self.all_details:
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


    def meta_data_returner(self):
        metall_price = self.draw_meta.meta_info()['metall_price']
        fabric_price = self.draw_meta.meta_info()['fabric_price']
        bolt_price = self.draw_meta.meta_info()['draw_num']

        meta_data = [metall_price,fabric_price,bolt_price]

        return meta_data
        

    def calc_all_forms(self,evt = None):
        # https://pypi.org/project/htmltabletomd/ - html to md 
        table_strings = []

        draw_num = self.draw_meta.meta_info()['draw_num']


        table_strings.append(draw_num)
        all_price = []

        for d in self.all_details: 
            answer_string = d.func()['answer']
            one_detail_cost = d.func()['cost']
            all_price.append(one_detail_cost)
            table_strings.append(f'{answer_string}\n')

        table_strings.append(f'цена компенсатора по чертежу {draw_num} : {str(sum(all_price))}₽')
        table_strings_formated = ''.join(table_strings)
        table = f'''
            {table_strings_formated}
        
         '''
        with open(f'{draw_num}.txt','w', encoding='utf-8') as tb:
            print(table, file=tb)





    def on_frame_configure(self, event=None):
      self.form_canvas.configure(scrollregion=self.form_canvas.bbox("all"))    

    def run(self): 
        self.mainloop()



if __name__ == "__main__":
    b = App()
    b.mainloop()
