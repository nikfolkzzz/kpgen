import tkinter as tk 

import tkinter.ttk as ttk


class DrawMeta(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.configure(bg='blue')
        self.labels = ['номер чертежа','металл за кг ₽','ткань м^2 ₽','болты шт. ₽',]
        self.default_values = ['21.16',700,25000,70]
        self.meta_label = []




        for idx , label in enumerate(self.labels): 
            meta_label = FormUnit(self,label,self.default_values[idx])
            meta_label.grid(row=0,column = idx)
            self.meta_label.append(meta_label)
        



    def meta_info(self):
        values = []




        for en in self.meta_label:

            values.append(en.en_val())

        draw_num, metall_price , fabric_price, bolt_price = values
        meta_info = {
                    'draw_num':draw_num,
                    'metall_price':metall_price,
                    'fabric_price':fabric_price,
                    'bolt_price':bolt_price
                    }

        print(meta_info)
        return meta_info


class FormUnit(tk.Frame):
    def __init__(self,parent,label_text ,default_value):
        super().__init__(parent)
        ttk.Label(self,text=label_text).grid(row=0,column=0)
        self.en =tk.Entry(self, width=10)


        self.en.bind('<Button-1>',self.on_click) 
        self.en.insert(0,default_value)
        self.en.grid(row=0,column=1)

    def en_val(self):

        return self.en.get()

    def on_click(self,parent,e): 
        self.en.delete(0,tk.END)
 


