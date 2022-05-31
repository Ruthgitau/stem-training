#GUI with python
from tkinter import *
root = Tk()

#create a frame
My_Label = Label(root,text="Hello World")

#show it on screen
My_Label.pack()
root.mainloop()
from tkinter import *
root = Tk()

#create a frame
My_Label = Label(root,text="Hello World")

#show it on screen
My_Label.grid(row=0,column=0)
root.mainloop()
