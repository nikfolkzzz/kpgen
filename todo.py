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
        self.tasks_canvas.pack(side= tk.TOP, fill = tk.BOTH, expand = 1)

        self.tasks_frame = tk.Frame(self.tasks_canvas)

        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)


        self.text_frame = tk.Frame(self)
        
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)



        self.task_create = tk.Text(self.text_frame, height=3, bg='#fff', fg='black') 


        self.scrollbar.pack(side=tk.RIGHT, fill = tk.Y)

        self.canvas_frame = self.tasks_canvas.create_window((0,0), window= self.tasks_frame, anchor = 'n')

        self.task_create.pack(side=tk.BOTTOM,fill = tk.X)

        self.text_frame.pack(side = tk.BOTTOM, fill =tk.X)
        self.task_create.focus_set()

        todo1 = tk.Label(self.tasks_frame, text="--- add items here---", bg='lightgrey',fg="black",pady=10)

        todo1.bind("<Button-1>",self.remove_task)


        self.tasks.append(todo1)

        for task in self.tasks: 
            task.pack(side=tk.TOP,fill=tk.X)








        self.bind("<Return>",self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)



        self.colour_schemes = [{"bg":"grey","fg": "white"},{"bg":"lightgrey", "fg":"black"}]
        
        

    def add_task(self, event=None):
        # put in variable inner text from text area (tk.Text())
        task_text = self.task_create.get(1.0,tk.END).strip()
        if len(task_text) > 0: 
            new_task = tk.Label(self.tasks_frame, text = task_text,pady=10)
            self.set_task_colour(len(self.tasks),new_task)
            new_task.bind("<Button-1>",self.remove_task)
            new_task.pack(side=tk.TOP,fill=tk.X)
            self.tasks.append(new_task)
        
        self.task_create.delete(1.0 , tk.END)


    def remove_task(self, event): 
        task = event.widget
        # widget.bind(event,handler)
        # event.widget достали виджет из хэндлера 

        if msg.askyesno("really delet?"):
            self.tasks.remove(event.widget)
            event.widget.destroy()
            self.recolour_tasks()
    
    def recolour_tasks(self): 
        for index , task in enumerate(self.tasks): 
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task): 
        _, task_style_choose = divmod(position,2)

        my_scheme_choice = self.colour_schemes[task_style_choose]

        task.configure(bg=my_scheme_choice['bg'])
        task.configure(fg=my_scheme_choice['fg'])

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))
    
    def task_width(self,event): 
        canvas_width = event.width 
        self.tasks_canvas.itemconfig(self.canvas_frame, width = canvas_width)


    def mouse_scroll(self, event): 
        if event.delta: 
            self.tasks_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        # если есть изменения в значении скрола, то в метод изменения скролинга передаем цифры 

        else: 
            if event.num == 5: 
                move = 1

            else:
                 move = -1 

            self.tasks_canvas.yview_scroll(move,"units")

    def run(self):
        self.mainloop()



if __name__ == "__main__":

    todo = Todo()
    todo.run()