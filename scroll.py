import tkinter as tk
from tkinter.constants import VERTICAL 



class ScrollBtn(tk.Tk):
  def __init__(self): 
    super().__init__()
    self.geometry('200x200')

    self.main_frame  = tk.Frame(self)
    self.main_frame.pack(fill= tk.BOTH  , expand = 1)

    self.my_canvas = tk.Canvas(self.main_frame)
    self.my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    self.scrollbar = tk.Scrollbar(self.my_canvas, orient=VERTICAL, command = self.my_canvas.yview)
    self.scrollbar.pack(side=tk.RIGHT, fill =tk.Y)

    self.my_canvas.configure(yscrollcommand=self.scrollbar.set)
    self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))


    self.second_frame = tk.Frame(self.my_canvas)

    self.my_canvas.create_window((0,0), window=self.second_frame, anchor='nw')




    for i in range(100):
      btn = tk.Button(self.second_frame, text=f'hello btn {i}')
      btn.grid(row=i, column=0)



if __name__ == '__main__':

  btns = ScrollBtn()
  btns.mainloop()