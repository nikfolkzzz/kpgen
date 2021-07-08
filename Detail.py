import tkinter as tk
from typing import Sequence

def area():
    print("hello from func1")

square = ['size A','size B',area]



class Detail(tk.Tk):
    def __init__(self,unit):
        super().__init__()
        self.inputs = unit[:-1]
        self.func = unit[len(unit)-1]

        self.geometry("200x200")
        self.title("jojo")

        func_args =[]
        for item in self.inputs: 
            tk.Label(self, text=item).pack(side=tk.TOP, fill=tk.X)
            tk.Entry().pack(side=tk.TOP, fill=tk.X)



    def val_returner(self):
        return self.func()

    def run(self):
        self.mainloop()
        






if __name__ == "__main__":
    calculator = Detail(square)
    calculator.run()
    calculator.val_returner()

