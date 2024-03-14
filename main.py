from tkinter import *
import math

master = Tk()
master.geometry('600x300')
master.title('Calculation')

def one(v):
    if v.get()==1:
        r=Label(master, text="{}".format(int(x.get())%int(y.get())), font=('Calibri 12'))
        r.grid(row=6,column=2)
        r.after(3000, r.destroy)
    if v.get()==2:
        r=Label(master, text="{}".format(int(x.get())/int(y.get())), font=('Calibri 12'))
        r.grid(row=6,column=2)
        r.after(3000, r.destroy)
    if v.get()==3:
        r=Label(master, text="{}".format(math.sqrt(int(x.get()))), font=('Calibri 12'))
        r.grid(row=6,column=2)
        r.after(3000, r.destroy)
    if v.get()==4:
        r=Label(master, text="{}".format((int(y.get()))**2), font=('Calibri 12'))
        r.grid(row=6,column=2)
        r.after(3000, r.destroy)



master.rowconfigure(1,weight=1)
master.rowconfigure(2,weight=1)
master.rowconfigure(3,weight=1)
master.rowconfigure(4,weight=1)
master.rowconfigure(5,weight=2)
master.rowconfigure(6,weight=3)

l1=Label(master, text='X ').grid(row=1,column=0)
l2=Label(master, text='Y ').grid(row=1,column=2)
x = Entry(master)
y = Entry(master)
x.grid(row=1, column=1)
y.grid(row=1, column=3)

#v = StringVar(master, "2") 
var = IntVar()

Label(master, text='Operation').grid(row=3,column=0)

R1 = Radiobutton(master, text="%", variable=var, value=1)
R1.grid(row=4, column=0)
R2 = Radiobutton(master, text="/", variable=var, value=2)
R2.grid(row=4, column=1)
R3 = Radiobutton(master, text="√x", variable=var, value=3)
R3.grid(row=4, column=2)
R4 = Radiobutton(master, text="y^2", variable=var, value=4)
R4.grid(row=4, column=3)
button = Button(master, text='=', width=25, command= lambda:one(var), cursor="hand2",background="white",fg="black")
button.bind("<Enter>", func=lambda e:button.config(fg='white',background='black'))

#button.bind("<Enter>", func=lambda e:master.config(background="#"))
button.bind("<Leave>", func=lambda e: button.config(fg='black',background='white'))
#button.bind("<Enter>", func=lambda e:master.config(background="white"))
button.grid(column=2)

mainloop()


