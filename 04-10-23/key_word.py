#python program to demonstrate the application of iskeyword()
#importing keyword libray which has lists importing keyword library which has lists 
# import keyword 

# #displaying the complete list using "kwlist()".
# print("The set of keywords in this version is :")
# print(keyword.kwlist)

# help("keyword")



# Value keywords: True, False, None

# print(4==4)
# print(6>9)
# print(8<=28)
# print(6>9)
# print(True or False)
# print(True and False)


# print(None == 0)
# print(None == "")
# print(None == False)
# A = None
# B = None

# print(A == B)

# def no_return_funcation():
#     num1 = 20
#     num2 = 10
#     addition = num1 + num2
#     # return addition
# number = no_return_funcation()

# print(number)


# def with_return(num):
#     if num % 4 == 0:
#         return False

# number = with_return(40)
# print(number)    


# False and True
# False or True
# not True

# container = "javatpoint"
# print("p"in container)
# print("x"in container)
# l = [10,20,30,50,"Rutvik","python"]
# print("python" in l)


#the is keyword
# print(True is True)
# print(False is True)
# print(None is not None)
# print(10 is 10)
# # print((9+5) is (7*2))
# print("python" is "Python")

# print([]==[])
# print([] is [])
# print({}=={})
# print({} is {})
#   """a blank dictionary or list is the same as another blank one. However,
#       they aren't identical entities because theyare stored independently  
#       in memory. This is because both the lis and dictionary are changeable"""


# print( " == " )
# print( " is " )



#using nonlocal Keyword

# def the_outer_function():
#     var = 10
#     def the_inner_function():
#         nonlocal var
#         var = 14
#         print("The value inside the inner funcation :",var)
#     the_inner_function()
#     print("The value inside the outer funcation :",var)
# the_outer_function()

# def the_outer_function():
#     var = 20
#     def the_inner_funcation():
#         var = 24
#         print("The value inside the inner funcation: ",var)
#     the_inner_funcation()
#     print("The value inside the outer function: ",var)
# the_outer_function()



# for i in range(15):
#     print(i,end=" ")
#     if i == 9:
#         break
#     print()

#looping from 1 to 15

# i = 0
# while i<15:
#     if i == 9:
#         i +=5
#         continue
#     else:
#     #When i has valu 9, adding 2 and printing the value
#         print(i ,end=" ")
#     i +=1


# for i in range(15):
#     if i ==10:
#         continue
#     print(i)



#Exception Hadling keywords - try,except,raise,finally, and assert

#initializing the number
# var1 = 4
# var2 = 2


# #Exception raised in the try section
# try:
#     d = var1//var2#this will raise a "divide by zero" exception
#     print(d)
# except ZeroDivisionError:
#     print("We cannot divide by zero")
# finally:
#     # if exception is raised  or not, this block will be executed every time
#     print("This is inside finally block")
# #by using assert keyword we will check if var2 is 0
# print("The value of var1/var2 is :")
# assert var2!=0,"Divide by 0 error"
# print(var1/var2)


#The pass keyword

# def function_pass(arguments):
#     pass

# def func_with_return():
#     v = 13
#     return v

# def func_with_no_return():
#     v = 10
# print(func_with_return())
# print(func_with_no_return())



#The del keyword
# var1 = var2 =5
# del var1
# print(var2)
# print(var1)

# list= [1,2,3,5,'a','b','v']
# del list[5]
# print(list)
