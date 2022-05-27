#impriving the advanced calculator so that it detects errors
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

#detecting an error and indicating that it is an error when a number is divided by zero
#try,accept in python to catch errors
try:
    div=10/0
    value =int(input ("enter a number"))
    print(value)
except:
    print("invalid number entered")

except ValueError:
    print("invalid number entered")
except ZeroDivisionError:
    print("Divided by zero")
    
try:
    div=100/0
    value=int(input("enter a number"))
    print(value)
except:
    print("invalid number entered")

    