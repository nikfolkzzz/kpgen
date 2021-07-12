import tkinter as tk 

class TestWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('200x200+500+500')
        self.title('jojo ni')
        




    def run(self):
        self.mainloop()



if __name__ == '__main__':
    win = TestWindow()
    win.run()