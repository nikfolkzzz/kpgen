import tkinter as tk
from tkinter.constants import VERTICAL 



class ScrollBtn(tk.Tk):
  def __init__(self): 
    super().__init__()
    self.geometry('200x200')
    self.title('when it is over ??? ')

    self.my_canvas = tk.Canvas(self ,bg='pink')
    self.my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    self.main_frame  = tk.Frame(self.my_canvas ,bg='lightblue')
    # self.main_frame.pack(fill= tk.BOTH  , expand = 1)


    self.scrollbar = tk.Scrollbar(self.my_canvas, orient=VERTICAL, command = self.my_canvas.yview)
    self.my_canvas.configure(yscrollcommand=self.scrollbar.set)
    self.scrollbar.pack(side=tk.RIGHT, fill =tk.Y)

    self.my_canvas.bind('<Configure>', self.task_width)
    self.canvas_frame = self.my_canvas.create_window((0,0), window=self.main_frame, anchor='n')

    self.bind("<Configure>", self.on_frame_configure)

    self.bind_all("<MouseWheel>", self.mouse_scroll)

    for i in range(100):
      btn = tk.Button(self.main_frame, text=f'hello btn {i}')
      # btn.grid(row=i, column=0)
      btn.pack(fill=tk.X)


  def task_width(self,e): 
    # canvas_width = e.width
    self.my_canvas.itemconfig(self.canvas_frame, width = e.width)

  def mouse_scroll(self, event): 
        if event.delta: 
            self.my_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        # если есть изменения в значении скрола, то в метод изменения скролинга передаем цифры 

        else: 
            if event.num == 5: 
                move = 1

            else:
                 move = -1 

            self.my_canvas.yview_scroll(move,"units")

  def on_frame_configure(self, event=None):
      self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all"))

if __name__ == '__main__':

  btns = ScrollBtn()
  btns.mainloop()