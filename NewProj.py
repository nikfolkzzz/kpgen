import tkinter as tk
import os 
from tkinter import ttk
from tkinter.constants import Y
from typing import Text 

from datetime import datetime


# import earthpy as et



class NewProj(tk.Toplevel): 
    def __init__(self,parent): 
        super().__init__(parent)
        
        self.geometry('300x300')
        self.title('Новый проект')
        self.lbs = ['номер проекта', 'заказчик']

        self.btn  = ttk.Button(self, text = 'создать нову папку и карточку' ,command=self.create_proj) 
        self.ens = []


        for index , item in enumerate(self.lbs): 
            frame = tk.Frame(self ,padx=10, pady=10)
            en = tk.Entry(frame, width=20)
            lb = tk.Label(frame, text = item)

            lb.grid(row=index , column=0)
            en.grid(row=index+1, column=0 )
            frame.grid(row=0, column=index)
            self.ens.append(en)

        self.btn.grid(row = 1)

    def create_proj(self):
        project_num , customer  = [f.get() for f in self.ens]
        now = datetime.now()
        timestring = now.strftime("%Y%m%d%H%M")
        card_text = f'''# {timestring} {customer} {project_num} 
tags: #вработе # # # # # # # #

## описание проекта 

## статус проекта 
        '''
        ZK_FOLDER = r"C://Users//Администратор//YandexDisk//zettelkasten"
        PROJS_FOLDER = ''
        FILE_PATH = os.path.join(ZK_FOLDER, f'{timestring} {customer} {project_num}.md ')

        with open (FILE_PATH, 'w',encoding='utf-8') as file :
            file.write(card_text)
        
        


