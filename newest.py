def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
       return "error number cannot be divided by Zero"
    return a/b
print("a simple calculator")
num1=float(input("enter 1st number"))
num2=float(input("enter 2nd number"))
op=input("enter any operator from(+,-,*,/)")
if op=="+" :print("answer:",add(num1,num2))
elif op=="-":print("answer",sub(num1,num2))
elif op=="*":print("answer",mul(num1,num2))
elif op=="/":print("answer",div(num1,num2))
else:
    print("invalid operator.please select again")
