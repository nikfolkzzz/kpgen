from tkinter import Tk, Label, Button

class Window: 
    def __init__(self, w, h , title, resizable = [False, False]):

        
        self.root = Tk()
        root = self.root
        root.title(title)
        root.geometry(f"{w}x{h}+200+200")
        root.resizable(resizable[0], resizable[1])

    def run(self):
        self.root.mainloop()





if __name__ == "__main__":
    window = Window(200,200, 'jojo',) 
    window.run()