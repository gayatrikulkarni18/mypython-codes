import tkinter as tk 
win = tk.Tk() 
win.title("Practical 9A") 
def redClick():
    label.config(text="Helvetica Font")
    label.config(bg="red")
    label.config(font=("Helvetica", 16)) 
def greenClick( ):
    label.config(text= "Cambria Font")
    label.config(bg="green")
    label.config(font=("Cambria", 18)) 
def yellowClick():
    label.config(text="Arial Font")
    label.config(bg="yellow")
    label.config(font=("Calbari", 14)) 
label = tk.Label(win,text="Practical 9 A",bg='white') 
label.pack() 
B1=tk.Button(win, text = "RED Click", relief='raised',command=redClick) 
B1.pack(side ="left") 
B2=tk.Button(win, text ="Green Click", relief='raised',command=greenClick) 
B2.pack(side = "left") 
B3=tk.Button(win, text ="Yellow Click", relief='raised',command=yellowClick) 
B3.pack(side = "left") 
win.mainloop()
