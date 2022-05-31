#GUI WITH PYTHON
from tkinter import *
root=Tk()
#when DISABLED is added the button cannot be clicked
myButton = Button (root,text="click me",state=DISABLED)
myButton.pack()
root.mainloop()
