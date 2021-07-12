import tkinter as tk 
import tkinter.messagebox as msg 

class Todo(tk.Tk): 
    def __init__(self,tasks = None):
        super().__init__()

        if not tasks: 
            self.tasks = []
        else: 
            self.tasks = tasks

        self.title("Todo app v2")
        self.geometry("300x400")
        
        self.tasks_canvas = tk.Canvas(self)
        self.task_frame = tk.Frame(self.tasks_canvas)
        self.task_text = tk.Frame(self)
        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)




        todo1 = tk.Label(self,text="--- add items here---", bg='lightgray',fg="black",pady=10)
        todo1.bind("<Button-1>",self.remove_task)


        self.tasks.append(todo1)

        for task in self.tasks: 
            task.pack(side=tk.TOP,fill=tk.X)

        self.task_create = tk.Text(self, height=5, bg='#fff', fg='black') 
        self.task_create.pack(side=tk.BOTTOM,fill = tk.X)

        self.tasks_canvas.pack(side= tk.TOP, fill = tk.BOTH, expand = 1)
        self.scrollbar.pack(side=tk.RIGHT, fill = tk.Y)

        self.canvas_frame = self.tasks_canvas.create_window((0,0), window= self.task_frame, anchor = 'n')
        self.task_frame.pack(side = tk.BOTTOM, fill =tk.X)
        self.task_create.focus_set()





        self.bind("<Return>",self.add_task)
        self.colour_schemes = [{"bg":"lightgray", "fg":"black"}, {"bg":"grey", "fg":"white"}]
        
        

    def add_task(self, event=None):
        # put in variable inner text from text area (tk.Text())
        task_text = self.task_create.get(1.0,tk.END).strip()
        if len(task_text) > 0: 
            new_task = tk.Label(self, text = task_text,pady=10)
            # создаем массив в () чтобы по разному поочередно окрашивать задачи в тудушке

            # подчеркиванием игнорируется первое значение в divmod и переменной присваивается 0 или 1 чтобы окрашивать таску
            _, task_style_choice = divmod(len(self.tasks),2)
            # как я понял красим четные не четные 
            my_scheme_choice = self.colour_schemes[task_style_choice]
            new_task.configure(my_scheme_choice['bg'])
            new_task.configure(my_scheme_choice['fg'])
            new_task.pack(side=tk.TOP,fill=tk.X)
            self.tasks.append(new_task)

    def run(self):
        self.mainloop()



if __name__ == "__main__":

    todo = Todo()
    todo.run()