import tkinter as tk
from tkinter.constants import TRUE 

from calc_functions import *

class Detail(tk.Frame):

    # принимает массив с названиями параметров и названием функции. Метод func возвращает строку которую нужно будет вставить в ткп 

    def __init__(self,master,arr):
        super().__init__(master)
        self.name = arr[0]
        tk.Label(self,bg='lightblue',font=("Times New Roman", 16), text=self.name).pack()
        self.labels = arr[1:-1]
        self.widget_entrs = []
        self.detail_function = eval(arr[len(arr)-1] )





        
        for label in self.labels:
            tk.Label(self,text=label , bg='#fff').pack(side=tk.TOP)
            en = tk.Entry(self, validate='key' ,validatecommand = (self.register(self.validate_inp),'%P'))
            self.widget_entrs.append(en)
            en.pack(side=tk.TOP)

    def collect_calculable_args(self,arr):
        args = []
        for item in arr:
            args.append(int(item.get()))
        return args

    def func(self, event = None):
        args = self.collect_calculable_args(self.widget_entrs)
        print(self.detail_function(args))

    def validate_inp(self, input): 
        try:
            x = int(input)
            return True
        except ValueError:
            return False

    def run(self):
      self.mainloop()


# how test this??

# if __name__ == '__main__':
#   d = Detail(['jojo','age','favorite_cace'])
#   d.run()