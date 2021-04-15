# Simple To-Do List App

import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do List by @SatyaSampreeth")

def add_task():
    task = entry_task.get()
    if task != '':
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title='Warning!', message='You must enter a task.')

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title='Warning!', message='You must select a task.')

def load_task():
    try:
        tasks = pickle.load(open('projects/tasks.dat', 'rb'))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title='Warning', message='Cannot find tasks.dat.')

def save_task():
    tasks =listbox_tasks.get(0, listbox_tasks.size())
    # print(tasks)
    pickle.dump(tasks, open('projects/tasks.dat','wb'))
    listbox_tasks.delete(0, tkinter.END)



# Create GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height  = 5, width = 60)
listbox_tasks.pack(side= tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand = scrollbar_tasks.set)
scrollbar_tasks.config(command= listbox_tasks.yview)

entry_task = tkinter.Entry(root, width = 60)
entry_task.pack()

button_add_task = tkinter.Button(root, text = 'Add Task', width = 50, command = add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text = 'Delete Task', width = 50, command = delete_task)
button_delete_task.pack()

button_load_task = tkinter.Button(root, text = 'Load Task', width = 50, command = load_task)
button_load_task.pack()

button_save_task = tkinter.Button(root, text = 'Save Task', width = 50, command = save_task)
button_save_task.pack()

root.mainloop()