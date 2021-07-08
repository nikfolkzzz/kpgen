import tkinter as tk 
from child_window import ChildWindow


class Window(tk.Tk): 
    def __init__(self, w, h , title, resizable = [False, False]):
        super().__init__()

     
        self.title(title)
        self.geometry(f"{w}x{h}+200+200")
        self.resizable(resizable[0], resizable[1])
        
    def create_child(self,w,h,title='child',resizeble=[False,False]):
        ChildWindow(self,w,h,title,resizeble)

    def run(self):
        self.mainloop()







if __name__ == "__main__":
    window = Window(200,200, 'jojo',) 
    window.create_child(550,550)
    window.run()