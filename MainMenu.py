import tkinter as tk 

class MainMenu(tk.Menu):
  def __init__(self,mainwindow):
    super().__init__(mainwindow)
    
    file_menu = tk.Menu(self)
    type_menu = tk.Menu(self)
    help_menu = tk.Menu(self)



    self.add_cascade(label='Файл', menu = file_menu)
    self.add_cascade(label='Форма компенсатор' , menu = type_menu)
    self.add_cascade(label='Справка', menu = help_menu)

    file_menu.add_command(label="Обновить")
    file_menu.add_separator()
    file_menu.add_command(label="Сохранить")
    file_menu.add_command(label="Выход",command=mainwindow.quit)

    type_menu.add_command(label="Круглый компенсатор",command= lambda : mainwindow.refresh('circ'))
    file_menu.add_separator()
    type_menu.add_command(label="Прямоугольный компенсатор",command= lambda : mainwindow.refresh('rect'))
    file_menu.add_separator()
    type_menu.add_command(label="Произвольный компенсатор")

    help_menu.add_command(label="FAQ")

