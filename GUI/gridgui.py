#GUI with python
from tkinter import *
root = Tk()

#create a frame
My_Label1 = Label(root,text="Hello World")
My_label2 = Label(root,text="Hello World")

#show it on screen
My_Label1.grid(row=0,column=0)
My_label2.grid(row=1,column=2)
root.mainloop()


