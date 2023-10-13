# #a default funcation to take another function parameter

# def spell(text):
#     #making text in upper
#     return text.upper()
#     #Taking text as user input
# text = input("Enter a text to print it in uppercase and double: ")
# #spell functuion with text
# print(spell(text))
# #Assigning variable with the default function
# scream = spell#Scream with text variable
# print(scream(text))


#Default function for making text uppercase
# def scream(word):
#     return word.upper()
# #Default funcation for making tex lowercase
# def spell(word):
#     return word.lower()

# #A thrid function that work as a high order function
# def speak(funct):
#     #Storing the function in a variable in high order function
#     speaking = funct("Hello Python Developers! You are welcomed to JavaTpoint")
#     print(speaking)
# #Printing text in uppercase
# speak(scream)
# #printing text in lowercase
# speak(spell)


#A default function for addition
# def Adding(a):
#     #Nested funcation With secound number
#     def Addition(b):
#         return a+b #addition of two number
#     return Addition #Result

# #Taking both number variable as user input
# a= int(input("Enter first number : "))
# b = int(input("Enter secound number : "))

# #Assigning nested adding function to a variable
# addVariable = Adding(a)
# #using variable as high order function
# Result = addVariable(b)
# #printing reslut
# print("Sum of Two number given by you is : ",Result)



# Using default function as Python decorators  
def Python_Decorator(funct):  
       # Inner nested function  
       def inner():   
              print("This line of code will be printed before the execution of high order function")  
              funct()   
              print("This line of code will be printed after the execution of high order function")  
       return inner   
# A default function as decorator  
def JTP_Decorator():   
    print("This line of code will be printed inside the execution of high order function")  
JTP_Decorator = Python_Decorator(JTP_Decorator) # Python decorator as high order function   
# Python decorator calling out as high order function   
JTP_Decorator()  