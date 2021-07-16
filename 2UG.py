import tkinter as tk 



def calc_circle_area(arr):
    return f'circle area : {3.14*arr[0]**2/2}'

def calc_rectangular_area(arr):
    return f'rectangular area : {arr[0]*arr[1]}'


shapes = [

    ['circle','radius','calc_circle_area'],
    ['rectangular', 'width', 'height','calc_rectangular_area']

    ]
#


class Detail(tk.Frame):
    # принимает массив с названиями параметров и названием функции. Метод func возвращает строку которую нужно будет вставить в ткп 
    def __init__(self,master,arr):
        super().__init__(master)
        self.name = arr[0]
        # self.geometry('300x300')
        # self.title(f'{self.name}')
        tk.Label(self,bg='yellow', text=self.name).pack()
        self.labels = arr[1:-1]
        self.widget_entrs = []
        self.detail_function = eval(arr[len(arr)-1] )
        for label in self.labels:
            tk.Label(self,text=label , bg='#fff').pack(side=tk.TOP)
            en = tk.Entry(self)
            self.widget_entrs.append(en)
            en.pack(side=tk.TOP)


        self.btn = tk.Button(self, text='calc')
        self.btn.pack(side= tk.TOP)
        self.btn.bind('<Button-1>',self.func)

    def collect_calculable_args(self,arr):
        args = []
        for item in arr:
            args.append(int(item.get()))
        return args

    def func(self, event = None):
        args = self.collect_calculable_args(self.widget_entrs)
        print(self.detail_function(args))


class Details(tk.Tk):
    def __init__(self,arr):
        super().__init__()
        self.arr = arr
        for d in self.arr: 
            Detail(self,d).pack()


    def run(self): 
        self.mainloop()











if __name__ == "__main__":
    b = Details(shapes)
    b.mainloop()
# https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application
# class Navbar(tk.Frame): ...
# class Toolbar(tk.Frame): ...
# class Statusbar(tk.Frame): ...
# class Main(tk.Frame): ...

# class MainApplication(tk.Frame):
#     def __init__(self, parent, *args, **kwargs):
#         tk.Frame.__init__(self, parent, *args, **kwargs)
#         self.statusbar = Statusbar(self, ...)
#         self.toolbar = Toolbar(self, ...)
#         self.navbar = Navbar(self, ...)
#         self.main = Main(self, ...)

#         self.statusbar.pack(side="bottom", fill="x")
#         self.toolbar.pack(side="top", fill="x")
#         self.navbar.pack(side="left", fill="y")
#         self.main.pack(side="right", fill="both", expand=True)