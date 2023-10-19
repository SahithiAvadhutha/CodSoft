import tkinter as tk
from tkinter import *

import random


def determine_winner(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    win1='you'
    win2='computer'

    if user_choice == computer_choice:
        return f"It's a tie! You both chose {user_choice}."

    if (user_choice == 'Rock' and computer_choice == 'Scissors') or \
       (user_choice == 'Paper' and computer_choice == 'Rock') or \
       (user_choice == 'Scissors' and computer_choice == 'Paper'):

        return f"You win! Computer chose {computer_choice}."

    return f"You lose! Computer chose {computer_choice}."


def button_click(choice):
    result = determine_winner(choice)
    diplay.config(text=''+result)



root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("495x335+0+0")
root.resizable(0,0)
root.config(bg="white")


frame1 = Frame(root,width=50,height=40,bg='black')
frame1.pack(side=TOP)
frame3=Frame(root,width=495,height=50,bg='white')
frame3.pack(side=TOP)
frame2=Frame(root,width=495,height=80,bg='olive')
frame2.pack(side=TOP)
displayframe=Frame(root,width=495,bg='firebrick',height=110)
displayframe.pack(side=TOP)
bframe=Frame(root,width=495,bg='DarkOrange4',height=45)
bframe.pack(side=TOP)
b1=Frame(bframe,width=247,bg='Darkorange4',height=47)
b1.pack(side=LEFT)
b2=Frame(bframe,width=247,bg='DarkOrange4',height=47)
b2.pack(side=LEFT)



rock_button=Button(frame2,text='ROCK',width=25,fg='white',bg='DarkOrange4',height=3,border=2,command=lambda:button_click('Rock'))
rock_button.pack(side=LEFT)
paper_button=Button(frame2,text='PAPER',width=25,fg='white',bg='DarkOrange4',height=3,border=2,command=lambda:button_click('Paper'))
paper_button.pack(side=LEFT)
scissors_button=Button(frame2,text='SCISSORS',width=25,fg='white',bg='DarkOrange4',height=3,border=2,command=lambda:button_click('Scissors'))
scissors_button.pack(side=LEFT)



title = Label(frame1,text='ROCK PAPER AND SCISSORS',fg='white',font=('Algerian',20,'bold'),bg="DarkOrange4",width='30',height=2)
title.pack()
text2=Label(frame3,text="LET'S START THE GAME!!",fg='black',bg='white',font=('Algerian',19,'bold'),width='30',height=2,border=2)
text2.pack()

diplay = Label(displayframe,bg='white',text="",width=30,height=4,font=('aria',16,'bold'))
diplay.pack()

root.mainloop()
