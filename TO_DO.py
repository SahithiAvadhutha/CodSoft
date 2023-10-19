from tkinter import *
from tkinter import messagebox, simpledialog
from PIL import ImageTk, Image


# Create an instance of tkinter window
win = Tk()
win.title("TO_DO_LIST")
win.geometry()
win.resizable(0,0)

# Define the geometry of the window

#FRAMES
#main
frame6=Frame(win,width=650,height=80,bg='black',borderwidth=9,border=3)
frame6.pack(side=TOP)
labeltitle=Label(frame6,text="TO DO LIST",font=("algerian",29,"bold"),width=29,height=1,fg='white',bg='black')
labeltitle.grid(row=0,column=0)
#left
frame1 = Frame(win, width=300, height=40)
frame1.pack(side=LEFT)
#right
frame2 = Frame(win, width=350, height=405)
frame2.pack(side=RIGHT)
#righttop
frame3=Frame(frame2,width=600,height=200,bg='white')
frame3.pack(side=TOP)
#rightbotton
frame4=Frame(frame2,width=428,height=213,bg='pink',border=3,highlightcolor='plum4')
frame4.pack(side=BOTTOM)
#righttopbottom
frame5=Frame(frame3,width=428,height=45,bg='white')
frame5.pack(side=BOTTOM)

#methods

def addtask():
    task = addtask.get()
    if task:
        # Read the existing tasks from the file
        tasks = []
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()
        except FileNotFoundError:
            pass

        # Calculate the new index
        new_index = len(tasks) + 1

        # Format the task with index and task name
        formatted_task = f"{new_index-1}: {task}\n"

        # Append the new task to the list
        tasks.append(formatted_task)

        # Write all tasks back to the file
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)

        addtask.delete(0, END)
# Function to delete the selected task
def removetask():
    task_to_remove = simpledialog.askstring("Remove Task", "Enter the task to remove:")

    if task_to_remove:
        updated_tasks = []
        found_task = False

        # Read the existing tasks from the file
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()
        except FileNotFoundError:
            tasks = []

        # Iterate through tasks to find and remove the task
        for task in tasks:
            parts = task.strip().split(": ", 1)
            if len(parts) == 2 and parts[1] == task_to_remove:
                found_task = True
            else:
                updated_tasks.append(task)

        # Update the tasks file without the specified task
        with open("tasks.txt", "w") as file:
            file.writelines(updated_tasks)

        if found_task:
            messagebox.showinfo("Task Removed", f'Task "{task_to_remove}" removed.')
            # Update the display with the updated tasks
            showtask()
        else:
            messagebox.showerror("Task Not Found", f'Task "{task_to_remove}" not found.')
 
# Function to display tasks
def showtask():
    display.delete(1.0, END)

    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                parts = task.strip().split(": ", 1)
                if len(parts) == 2:
                    display.insert(END, f"Index: {parts[0]}, Task: {parts[1]}\n")
                else:
                    display.insert(END, f"Task: {task}")

    except FileNotFoundError:
        display.insert(END, "No tasks found.")
def updatetask():
    display.delete(1.0, END)

    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                parts = task.strip().split(": ", 1)
                if len(parts) == 2:
                    index, task_name = parts
                    display.insert(END, f"Index: {index}, Task: {task_name}\n")
                else:
                    display.insert(END, f"Task: {task}")

    except FileNotFoundError:
        display.insert(END, "No tasks found.")

    # Prompt the user for the task to mark as completed
    task_to_complete = simpledialog.askstring("Mark Task as Completed", "Enter the task to mark as completed:")

    if task_to_complete:
        updated_tasks = []
        found_task = False

        # Iterate through tasks to find and mark the task as completed
        for task in tasks:
            parts = task.strip().split(": ", 1)
            if len(parts) == 2 and parts[1] == task_to_complete:
                index, task_name = parts
                updated_tasks.append(f"{index}: {task_name} (Completed)\n")
                found_task = True
            else:
                updated_tasks.append(task)

        # Update the tasks file with the completed task
        with open("tasks.txt", "w") as file:
            file.writelines(updated_tasks)

        if found_task:
            messagebox.showinfo("Task Updated", f'Task "{task_to_complete}" marked as completed.')
        else:
            messagebox.showerror("Task Not Found", f'Task "{task_to_complete}" not found.')


img = ImageTk.PhotoImage(Image.open("pic.jpg"))

#labels
# Create a Label Widget to display the text or Image
label = Label(frame1, image=img,width=304,height=500)
label.pack()
#buttons
addbutton=Button(frame3,text='ADD TASK',width=30,height=2,font="broadway",fg='black',bg='dark turquoise',command=addtask)
addbutton.pack(side=TOP)
delbutton=Button(frame3,text='REMOVE TASK',width=30,height=2,font="broadway",fg='black',bg='dark orange',command=removetask)
delbutton.pack(side=TOP)
updatebutton=Button(frame3,text='UPDATE TASK',width=30,height=2,font="broadway",fg='black',bg='dark slate gray',command=updatetask)
updatebutton.pack(side=TOP)
showbutton=Button(frame3,text='SHOW TASKS',width=30,height=2,font="broadway",fg='black',bg='palegreen4',command=showtask)
showbutton.pack(side=TOP)

display=Text(frame4,font=("aria",18),bd=3,width=33,height=8)
display.grid(row=0,column=0)

#entry
addtask=Entry(frame5,font=("cooper black",15,"bold"),bd=4,width=32,state=NORMAL)
addtask.grid(row=0,column=0)


win.mainloop()
