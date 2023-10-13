# def fun1(msg): #here, we are creating a funcation and passing the pratameter
#     print(msg)
# fun1("Hii, wekcome to function") # Here, We are printing the data of funcation 1
# fun2 = fun1 #Here, Wr are copying the function 1 data to function 2
# fun2("Hii, welcome to function") #Here,we are printing the data of function 2


# def func(): #here, we are creating a function and passing the parameter
#     print("We are in first funcaion") #Here, We are printing the data parameter
#     def func1(): #here, we are creating a function and passing the parameter
#         print("This is first chid function")
#     def func2(): #here, we are creating a function and passing the parameter
#         print("this is secound chid function")
#     func2()
#     func1()
#     func2()

# func()


# def add(x): #here, we are creating a function and passing the parameter
#     return x + 1  #here, We are returning the passed calue by adding 1
# def sub(x):#here, we are creating a function and passing the parameter
#     return x - 1
# def operator(func,x): #here, we are creating a function and passing the parameter
#     temp = func(x)
#     return temp


# print(operator(sub,10))#Here, we are printing the operation substraction with 10
# print(operator(add,20))#here, We are printing the operation adddition with 20


# def hello(): #here, we are creating a function named hello
#     def hi():  # here, we are creating a function named hi  
#         print("Hello")  #here, we are printing the output of the function  
#     return hi

# new = hello()
# new()



# def divide(x,y): #here, we are creating a funcation and passing the paramater
#     print(x/y) # Here, we are printing the result of the expression  
# def outer_div(func):  # Here, we are printing the result of the expression  
#     def inner(x,y):  # Here, we are printing the result of the expression  
#         if (x<y):
#             x,y = y,x
#         return func(x,y)
#     #Here we are returning a function with some passed parameters
#     return inner

# divide1 = outer_div(divide)
# divide1(2,4)


#Syntactic Decorator

# def outer_div(func):  # Here, we are printing the result of the expression  
#     def inner(x,y):  # Here, we are printing the result of the expression  
#         if (x<y):
#             x,y = y,x
#         return func(x,y)
#     #Here we are returning a function with some passed parameters
#     return inner


# @outer_div
# def divide(x,y): #here, we are creating a funcation and passing the paramater
#     print(x/y)

# divide(2,4)


#We can import mod_decorator.py in another file.
# from mod_decorator import do_twice

# @do_twice
# def say_hello():
#     print("Hello There")

# say_hello()


# from mod_decorator import do_twice
# @do_twice
# def display(name):
#     print(f"Hello {name}")
# display("Rutvik")


# from mod_decorator import do_twice
# @do_twice

# def return_greeting(name):
#     print("We are created greeting")
#     return f"hi {name}"
# hi_adam = return_greeting("Adam")


# class Student: #here, We are creating a xlas with the  name Studnet
#     def __init__(self,name,grade):
#         self.name = name
#         self.grade = grade

#     @property
#     def display(self):
#         return self.name + "got grade " + self.grade
# stu = Student("Johan","B")
# print("Name of the Sudent:",stu.name)
# print("Grade of the student:",stu.grade)
# print(stu.display)


# class Person:
#     @staticmethod
#     def hello():
#         print("Hello Peter")

# per = Person()
# per.hello()
# Person.hello()
# Person()

# import functools #here, we are importing the functools into our program
# def repat(num):
#     # Here, we are creating and returing  a wrapper funcation
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def werapper(*args,**kwargs):
#             for _ in range(num): #here, we are initializing a for loop and iterating till num
#                 value = func(*args,**kwargs)
#             return value #Here, we are returning the value
#         return wrapper # here, we are returning the wrapper class
#     return decorator_repeat
#     # Here we are passing num as an argument which repeats the print function
#     @repeat(num=5)
#     def function1(name):
#         print(f"{name}")
#     a = function1("Rutvik")
#     print(a)


# import functools # here, we are importing the functools into our program
# def count_function(func):
#     # here , we are defining a function and passing the parameter func
#     @functools.wraps(func)
#     def wrapper_count_calls(*args,**kwargs):
#         wrapper_count_calls.num_calls +=1
#         print(f"Call {wrapper_count_calls.num_calls}of{func.__name__!r}")
#         return func(*args,**kwargs)
#     wrapper_count_calls.num_calls= 0
#     return wrapper_count_calls
# @count_function
# def say_hello():
#     print("Say Hello")
# say_hello()
# say_hello()
  
import functools 
class Count_Calls:
    def __init__(self,func):
        functools.update_wrapper(self,func)
        self.func = func
        self.num_calls = 0
    def __call__(self,*args,**kwargs):
        self.num_calls +=1
        print(f"call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args,**kwargs)

@Count_Calls
def say_hello():
    print("say Hello")
say_hello()
say_hello()
say_hello()
