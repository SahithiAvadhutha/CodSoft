from tkinter import *
root=Tk()
root.geometry("495x335+0+0")
root.resizable(0,0)
root.config(bg="white")
#title
frame1=Frame(root,width=500,height=90,bg="navyblue")
frame1.pack(side=TOP)
labeltitle=Label(frame1,text="CALUCLATOR",font=("Algerian",30,"bold"),fg="black",bg="red4",height=2,width=20)
labeltitle.grid(row=0,column=0)
#frames
calframe=Frame(root,width=515,height=100,bg='white')
calframe.pack(side=TOP)



operator=''
def buttonclick(numbers):
    global operator
    operator=operator+numbers
    calculatorfeild.delete(0,END)
    calculatorfeild.insert(END,operator)
def clear():
    global operator
    operator=''
    calculatorfeild.delete(0,END)
def ans():
    global operator
    result=str(eval(operator))
    calculatorfeild.delete(0,END)
    calculatorfeild.insert(0,result)
    operator=''

calculatorfeild=Entry(calframe,font=("aria",18,"bold"),width=39)
calculatorfeild.grid(row=0,column=0,columnspan=4)

button7=Button(calframe,font=("aria",18,"bold"),width=7,text='7',fg="black",bg="red4",bd=2,command=lambda:buttonclick('7'))
button7.grid(row=1,column=0)

button8=Button(calframe,font=("aria",18,"bold"),width=7,text='8',fg="black",bg="red4",bd=2,command=lambda:buttonclick('8'))
button8.grid(row=1,column=1)

button9=Button(calframe,font=("aria",18,"bold"),width=7,text='9',fg="black",bg="red4",bd=2,command=lambda:buttonclick('9'))
button9.grid(row=1,column=2)

buttonplus=Button(calframe,font=("aria",18,"bold"),width=7,text='+',fg="black",bg="red4",bd=2,command=lambda:buttonclick('+'))
buttonplus.grid(row=1,column=3)

button4=Button(calframe,font=("aria",18,"bold"),width=7,text='4',fg="black",bg="red4",bd=2,command=lambda:buttonclick('4'))
button4.grid(row=2,column=0)

button5=Button(calframe,font=("aria",18,"bold"),width=7,text='5',fg="black",bg="white",bd=2,command=lambda:buttonclick('5'))
button5.grid(row=2,column=1)

button6=Button(calframe,font=("aria",18,"bold"),width=7,text='6',fg="black",bg="white",bd=2,command=lambda:buttonclick('6'))
button6.grid(row=2,column=2)

buttonminus=Button(calframe,font=("aria",18,"bold"),width=7,text='-',fg="black",bg="red4",bd=2,command=lambda:buttonclick('-'))
buttonminus.grid(row=2,column=3)

button1=Button(calframe,font=("aria",18,"bold"),width=7,text='1',fg="black",bg="red4",bd=2,command=lambda:buttonclick('1'))
button1.grid(row=3,column=0)

button2=Button(calframe,font=("aria",18,"bold"),width=7,text='2',fg="black",bg="white",bd=2,command=lambda:buttonclick('2'))
button2.grid(row=3,column=1)

button3=Button(calframe,font=("aria",18,"bold"),width=7,text='3',fg="black",bg="white",bd=2,command=lambda:buttonclick('3'))
button3.grid(row=3,column=2)

buttonmul=Button(calframe,font=("aria",18,"bold"),width=7,text='*',fg="black",bg="red4",bd=2,command=lambda:buttonclick('*'))
buttonmul.grid(row=3,column=3)

buttonans=Button(calframe,font=("aria",18,"bold"),width=7,text='ANS',fg="black",bg="red4",bd=2,command=ans)
buttonans.grid(row=4,column=0)

buttonclear=Button(calframe,font=("aria",18,"bold"),width=7,text='CLEAR',fg="black",bg="red4",bd=2,command=clear)
buttonclear.grid(row=4,column=1)

button0=Button(calframe,font=("aria",18,"bold"),width=7,text='0',fg="black",bg="red4",bd=2,command=lambda:buttonclick('0'))
button0.grid(row=4,column=2)

buttondiv=Button(calframe,font=("aria",18,"bold"),width=7,text='/',fg="black",bg="red4",bd=2,command=lambda:buttonclick('/'))
buttondiv.grid(row=4,column=3)






root.mainloop()
