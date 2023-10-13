# def square(number):
#     result = number**2
#     return result
# import example_module
# result = example_module.square(  4  )    
# print("By using the module square of number is: ", result )    


# import math
# print("The value of euler's number is ",math.e)


# import math as mt #here, We are importing the math module as mt
# print("The value of euler's number is ",mt.e)


# from math import e,tau
# print("The value of tau constant is :",tau)
# print("The value of the euler's number is : ",e)

# from name_of_module import*


#Here,we are imorting the complete math module using*
from math import*
#Here, we are accessing funcation of math module without using the dot operator
print("Calculating square root: ",sqrt(25))
print("Calculating tangent of an angel:",tan(pi/6)
)
import sys 
print("Path of the sys module in the system is:",sys.path)

print("List of funcation:\n",dir(str),end=",")

number = 204
def addnumber():
    global number
    number = number +200
print("The number is :",number)
addnumber()
print("The number is :",number)
print(number)


# a = ["Python","Exceptions","try and except"]
# try:
#     for i in range(4):
#         print("The index and element from the array is :",i,a[i])
# except:
#     print("index out of range")


# num = [3,4,5,7]
# if len(num)>3:
#     raise Exception(f"length of the given list must be less than or equal to 3 but is {len(num)}")


# def square_root(number):
#     assert (number<0),"Give a positive integer"

#     return number**(1/2)

#     #Calling funcation and passing the values

# print(square_root(36))
# print(square_root(-36))


#Python program to show how to use else clause with try and except clauses

def reciprocal(num1):
    try:
        print("try")
        reci= 1/num1
    except ZeroDivisionError:
        print("except")
        print("We cannot divide by zero")
    else:
        print("else")
        print(reci)
reciprocal(4)
reciprocal(0)


#Python code to show the use of finally clause
#Raising an exception in try block
try:
    div = 4//0
    print(div)
except ZeroDivisionError:
    print("Atepting  to divide by zero")
finally:
    print("This is code of finally clause")


class EmptyError(RuntimeError):
    def __init__(self,argument):
        self.arguments = argument

var ="yugj"
try:
    raise EmptyError("The variable is empty")
except (EmptyError,var):
    print(var.arguments)