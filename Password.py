from tkinter import *
from tkinter import messagebox
import random
import string
root=Tk()
root.geometry("495x335+0+0")
root.resizable(0,0)
root.config(bg="powderblue")
frame1=Frame(root,width=495,height=74,bg='black',border=2,borderwidth=2)
frame1.pack()
frame2=Frame(root,width=495,height=80,bg='black')
frame2.pack()
frame3=Frame(root,width=495,height=80,bg='yellow')
frame3.pack()
frame4=Frame(root,width=495,height=100,bg='white')
frame4.pack()


def generate_password():
    password_length = int(len_entry.get())

    # Ensure password length is at least 8 characters
    if password_length<4:
        messagebox.showerror("Error", "Password length should be at least 4 characters.")
        return

    characters =  string.ascii_lowercase+string.ascii_uppercase + string.digits
    password = ''.join(random.choice(characters) for i in range(password_length))

    diplay.config(text="Generated Password: " + password)

len_text=Label(frame2,text='length',font=('aria',19,'bold'),width=9,height=3,bg='black',foreground='white',border=2,borderwidth=3)
len_text.grid(row=3,column=0)
len_entry=Entry(frame2,width=20,font=('aria',25,'bold'),textvariable='len_entry')
len_entry.grid(row=3,column=2)


generate_but=Button(frame3, text="GENERATE", fg='white', bg='black', width=20, height=2, font=('aria',15,'bold'), command=generate_password)
generate_but.grid(row=0,column=3)

diplay = Label(frame4,bg='white',text="",width=100,height=100,font=('Algerian',19,'bold'))
diplay.pack()

title = Label(frame1,text="PASSWORD GENERATOR",font=('Algerian',32,'bold'),fg='black',borderwidth=10,border=2,bg='white')
title.pack()



root.mainloop()
