import tkinter as tk
from tkinter.constants import LEFT, TRUE 
import os 

from calc_functions import *

class Detail(tk.Frame):

    # принимает массив с названиями параметров и названием функции. Метод func возвращает строку которую нужно будет вставить в ткп 

    def __init__(self,master,arr,metall_price, fabric_price, bolt_price):
        super().__init__(master)
        self.mp=metall_price
        self.fp=fabric_price
        self.bp=bolt_price
        self.configure(borderwidth=5, relief="groove", highlightcolor = 'pink' )

        self.name = arr[0]
        tk.Label(self,font=("Arial", 12),  text=arr[0]).grid(row=0,column=0 , columnspan = 2)

        self.labels = arr[1:-1]
        self.widget_entrs = []
        self.detail_function = eval(arr[len(arr)-1] )


        





        for index, label in enumerate(self.labels):

            frame = tk.Frame(self)
            label_name =  tk.Label(frame,text=label)
            en = tk.Entry(frame, validate='key' ,width=10 ,validatecommand = (self.register(self.validate_inp),'%P'))
            label_name.grid(row=0,column=0)
            en.grid(row=0,column=1)

            frame.grid(row = 1 , column = index)
            self.widget_entrs.append(en)

    def collect_calculable_args(self,arr):
        args = []
        for item in arr:
            args.append(int(item.get()))
        return args 

    def func(self, event = None):
        args = self.collect_calculable_args(self.widget_entrs)
        func_answer = self.detail_function(args,self.name,self.mp,self.bp,self.fp)
        calculated_string = func_answer['answer']
        cost = func_answer['cost']

        return func_answer


        

    def validate_inp(self, input): 
        try:
            x = int(input)
            return True
        except ValueError:
            return False

    

    def run(self):
      self.mainloop()


