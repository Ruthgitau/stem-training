#scientific calculator
type=input("which data type of unit you would like")
if type=="float":
    x=float("assign a value of x")
    y=float("assign a value of y")
if type =="int":
     x=int("assign a value of x")
     y=int("assign a value of y")

operation=input("enter an operation")
if operation=="additon":
    print(x+y)
if operation=="subtraction":
    print(x-y)
if operation=="division":
    print(x/y)
if operation=="multiplicaion":
    print(x*y)
solution=(x+y) or (x-y) or (x*y) or (x/y)
complex_solution=complex(solution)
