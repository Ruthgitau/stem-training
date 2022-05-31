#GUI WITH PYTHON
from tkinter import *
root=Tk()
#when DISABLED is added the button cannot be clicked
myButton = Button (root,text="click me",state=DISABLED,padx=50,pady=50)
myButton.grid(row=1,column=5)
root.mainloop()
