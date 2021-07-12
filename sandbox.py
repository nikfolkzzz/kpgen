import tkinter as tk 

root = tk.Tk()
label = tk.Label(root, text = '# hello world')
label.pack(padx = 50, pady = 50)


root.mainloop()



def hello_returner(r): 
    area = 3.14*r**2/2 
    return 'radius = {}'.format(area) 

shapes = [
    {
        'name': 'rektangle',
        'inputs': ['a','b']
    },
    {
        'name': 'circle',
        'inputs': ['r'],
        'func': hello_returner
    }
]

    

class Shape: 
    def __init__(self,dict): 
        self.name = dict['name']
        self.inputs = dict['inputs']
        self.hello_returner = dict['func']

    def data_returner(self): 
      return self.hello_returner(4)

circle = Shape(shapes[1])
print(circle.name, circle.inputs, circle.data_returner())




