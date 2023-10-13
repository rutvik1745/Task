def square(num):

    return num**2
o = square(6)
print(square(6))

def a_function(string):
    return len(string)

print("length of the string Function is ",a_function("Function"))
print("length of the string Python is ",a_function("Python"))

def squ(item_list):
    sque = []
    for i in item_list:
        sque.append(i**2)
    return sque

my_list = [2,3,4,6]
result = squ(my_list)
print(result)


#python code to demonstrate the use of default arguments
#defining a Function
def function(n1,n2=20):
    print("number 1 is",n1)
    print("number 2 is",n2)

#Calling the function and passing onlu one argument
print("passing onlu one argument")
function(30)

#Now giving two arguments to the function
print("Passing two argument")
function(50,30)


#Python code to demonstrate the use of keyword arguments

def function1(n1,n2):
    print("number 1 is :" ,n1)
    print("number 2 is :",n2)

#Calling function and passing argument without using keyword
print("without suing keyword")
function(50,30)


#Calling function and passing arguments using keyword
print("With using keyword")
function(n2 = 50,n1 =30)


#Python code to demonstrate the use of default arguments

def function2(n1,n2):
    print("number 1 is :",n1)
    print("number 2 is :",n2)

#Calling function and passing two arguments out of order, We need num 1 to be 20 and num2 to be 30
print("Passing only one argument")
function(30,20)

#Calling function and passing only one argument
print("Passing only one argument")
try:
    function(30)

except:
    print("Function needs two positional arguments")


#Python code to demonstrate the se of variable-length arguments
def function3(*args_list):
    ans = []
    for l in args_list:
        ans.append(l.upper())
    return ans

#Passing args arguments
object = function3("Python","Functions","tutorial")
print(object)

def function4(**kargs_list):
    ans = []
    for key,values in kargs_list.items():
        ans.append([key,values])
    return ans

object1 = function4(First="Python",Secound="Function",Third="Tutorial")
print(object1)

#Python code to demonstrate the use of return statements

#Defining a function with return statement

def square(num):
    return num**2

    #Calling Function and passing argument
print("With return statement")
print(square(52))

#Defining a function without return statement
def square(num):
    num**2
    
#Calling function and passing arguments
print("Without return statement")
print(square(52))

