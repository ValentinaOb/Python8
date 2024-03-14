from tkinter import *
import math

master = Tk()
master.geometry('600x300')
master.title('Text')

def one(t):
    txt1=str(t.get("1.0", "end-1c"))
    txt= list(txt1.split(" "))
    count=[]
    pos=[]
    res=[]
    n=0
    n1=100

    for i in txt:
        for j in i:
            n+=1
        count.append(n)
        n=0
        
    for i in count:
        if i<n1:
            n1=i
    
    l=0
    for i in count:
        if i ==n1: pos.append(l)
        l+=1

    l=0
    for i in txt:
        for j in pos:
            if l==j:
                res.append(i)
        l+=1

    sr = ' '.join(map(str, res))
    r=Label(master, text="{}".format(sr, font=('Calibri 24')))
    r.grid(row=3,column=2)
    r.after(5000, r.destroy)



master.rowconfigure(1,weight=1)
master.rowconfigure(2,weight=1)
master.rowconfigure(3,weight=2)

l1=Label(master, text='   Input text ').grid(row=1,column=0)
t = Text(master, height = 5, width = 55) 
t.grid(row=2,column=1)


button = Button(master, text='Min', width=25, command= lambda:one(t), cursor="hand2",background="white",fg="black")
button.grid(row=3,column=1)

mainloop()


