import tkinter as tk 



class ScrollBtn(tk.Tk):
  def __init__(self): 
    super().__init__()
    self.geometry('200x200')

    for i in range(100):
      btn = tk.Button(self, text=f'hello btn {i}')
      btn.grid(row=i, column=0)



if __name__ == '__main__':

  btns = ScrollBtn()
  btns.mainloop()