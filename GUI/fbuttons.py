#GUI with python
from tkinter import *
root=Tk()
def myclick():
    myLabel=Label(root,text="hey,you clicked")
    myLabel.pack()
MyB=Button(root,text="click me!",command=myclick)
MyB.pack()
root.mainloop()
