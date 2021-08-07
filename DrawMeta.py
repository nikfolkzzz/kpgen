import tkinter as tk 


class DrawMeta(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.configure(bg='blue')
        # DRAW NUMB
        self.draw_num_label = tk.Label(self, text = 'Номер чертежа компенсатора', bg='pink' )
        self.draw_num_label.grid(row=0 , column=0 , sticky='e')

        self.draw_num_entry = tk.Entry(self,)
        self.draw_num_entry.grid(row=0 , column=1,sticky='w' )

        # FABRIC PRICE 
        tk.Label(self,text='цена за кв м ткани', ).grid(row=1,column=0 ,sticky='w')

        self.fabric_price_entry = tk.Entry(self, textvariable='25000')
        self.fabric_price_entry.grid(row=1,column=1)
        # METALL PRICE 

        tk.Label(self,text='цена 1 кг метала',anchor='w').grid(row=2,column=0,sticky='w')
        self.metall_price_entry = tk.Entry(self, textvariable='25000').grid(row=2, column=1)

        tk.Label(self,text='цена за одим болт',anchor='w').grid(row=3,column=0,sticky='w')
        self.bolt_price = tk.Entry(self, textvariable='25000').grid(row=3, column=1)

        # SCREW PRICE


    def meta_info(self):
        info = {'fabric_price': self.fabric_price_entry.get(),
                'draw_number':self.draw_num_entry.get(),
                'bolt_price': self.bolt_price_entry,
                'metall_price': self.metall_price_entry,
        }    


        return info