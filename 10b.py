
from tkinter import*
from tkinter import messagebox
import sqlite3

connection = sqlite3.connect("Student.db")
print(connection.total_changes)


def showStudent_Id():
    c= conn.cursor()
    conn= sqlite3.connect("Student.db")
    cursor = conn.cursor()
    cursor.executer("USE Library")
    sql ="SELECT * FROM StudentId where "+var.get()+"like '%"+stext.get()+"%"
    cursor.execute( sqlite3)
    results = cursor.fetchaiiO
    if not results:
        messagebox.showtnfo(title='Sorry', message="No Record Found!")

win = Tk()
win.title("Students Details")
var = StringVar()
var.set("Student_Id")

Label(win,text="Select the Attribute to Search:").grid(row=0)

r1=Radiobutton(win,text="Search by Title",width=50, justify="center",variable="var",value="title",anchor="w")
r1.grid(row=1,columnspan=2)
r2=Radiobutton(win,text="Search by student_ID",width=50, justify="center",variable="var",value="title",anchor="w")
r2.grid(row=2,columnspan=2)

L1=Label(win,text="Enter the text string to Search:").grid(row=5,column=0)
stext = Entry(win, width=20).grid(row=5,column=1)

b1=Button(win, text="StudentId",command=showStudent_Id).grid(row=6,columnspan=2)
mainloop()
