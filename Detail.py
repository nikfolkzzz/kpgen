import tkinter as tk
from tkinter.constants import ANCHOR, LEFT, TRUE 
import os 

from calc_functions import *

class Detail(tk.Frame):

    # принимает массив с названиями параметров и названием функции. Метод func возвращает строку которую нужно будет вставить в ткп 

    def __init__(self,master,arr,):
        super().__init__(master)

        self.configure(borderwidth=5, relief="groove", highlightcolor = 'pink',bg='#FFA78D' )

        self.name = arr[0]
        tk.Label(self,font=("Arial", 12), bg='#120132', fg='white', anchor='w',  text=arr[0]).grid(row=0,column=0 , columnspan = 2)

        self.labels = arr[1:-1]
        self.widget_entrs = []
        self.detail_function = eval(arr[len(arr)-1] )


        





        for index, label in enumerate(self.labels):

            frame = tk.Frame(self, padx=10, pady=10 ,bg='#FEBC8E')
            label_name =  tk.Label(frame,text=label, bg='#5C0758' , fg='white' , anchor='w')
            en = tk.Entry(frame, validate='key' ,width=10 ,)
            label_name.grid(row=0,column=0)
            en.grid(row=1,column=0)

            if index <= 3 : 
                frame.grid(row = 1 , column = index)

            else:
                frame.grid(row=2, column= index - 4 )

            self.widget_entrs.append(en)

        

    def collect_calculable_args(self,arr):
        args = []
        for item in arr[:-1]:
            args.append(int(item.get()))

        args.append(arr[len(arr)-1].get())
        return args 

    def func(self, event = None):
        args = self.collect_calculable_args(self.widget_entrs)
        func_answer = self.detail_function(args)
        return func_answer


        

    def validate_inp(self, input): 
        try:
            x = int(input)
            return True
        except ValueError:
            return False

    

    def run(self):
      self.mainloop()


