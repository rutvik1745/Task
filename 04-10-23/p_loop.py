#Python program to show how the for loop works

# numbers = [4,2,6,7,8,9,10,6,9,2,10]

# square = 0
# squares = []

# for value in numbers:
#     square = value **2 
#     squares.append(square)
# print(squares)

#Python program to show how if-else statments work

# string = "Python Loop"

#Initiating a loop
# for s in string:
    # if s=='o':
    #     print("If block")
    # else:
    #     print(s)

#secoud method
# for i in range(len(string)):
#     if string[i]=='o':
#         print("If block")
#     else:
#         print(string[i])



# tuple_ = (3,4,6,8,9,2,3,8,9,7)

# for value in tuple_:
#     if value %2 !=0:
#         print(value)
# else:
#     print("These are the odd numbers present in the tuple")


# for i in range(len(tuple_)):
#     if tuple_[i] %2 == 0:
#         print(tuple_[i])
# else:
#     print("This are the even number present in the tuple")


# print(range(10))
# print(list(range(10)))
# print(list(range(4,9)))



#while loop
c = 0
# while c<10:
#     c = c+3
#     print("python loops",c)
# else:
#     print("Code block inside the else statement")


#Continue Statement

# for string in "Python Loops":
#     if string =='o' or string == 'p' or string=='t':
#         continue
#     print("Current Latter:",string)

#Break Statement

# for string in "Python Loops":
#     if string == 'L':
#         break
#     print("Current Letter:",string)

#Pass  Statement

# for string in "Python Loops":
#     pass 
# print("Last Latter",string)