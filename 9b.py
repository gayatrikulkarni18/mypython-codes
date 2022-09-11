from tkinter import* 
def swap():
    if v.get():
        e.pack_forget()
        mb.pack(anchor="w", side="right")
        l2.config(text="Use Menu Below.")
        l2.config(bg="yellow")
        l2.config(font=("Helvetica",16,"italic"))
    else:
        mb.pack_forget()
        e.pack(anchor="w",side="left")
        l2.config(text="Use Entry Box Below.")
        l2.config(bg="green")
        l2.config(font=("Cambria",16,"bold"))
        e.focus() 
t= Tk() 
v= IntVar(t) 
c=Checkbutton(t,command=swap,text="Select to use menu.",variable=v) 
c.pack(anchor="w") 
f1=Frame(t) 
l1=Label(f1,text="Select the Menu item of your choice:") 
l1.pack(side="left") 
l2=Label(f1,text="Use Entry Box Below.",bg="green",font=("Cambria",16,"bold")) 
l2.pack(side="top") 
f=Frame(f1) 
f.pack(side= "left") 
e=Entry(f,width=35) 
mb=Menubutton(f,width=25,text="Veg",indicatoron=1,relief="sunken",anchor="w")
m=Menu(mb,tearoff=0);mb.configure(menu=m)
for s in "Veg nonVeg Chinese French".split():
    m.add_command(label=s,command=lambda s=s:mb.configure(text=s)) 
f.pack() 
f1.pack() 
swap() 
b=Button(t,text="Place order",relief="raised",fg="red",command=t.destroy); 
b.pack(side="top") 
f.mainloop()