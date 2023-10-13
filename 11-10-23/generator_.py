# def simple():
#     for i in range(10):
#         if(i%2 == 0):
#             yield i
    
# #Successive Function call using for  loop

# for i in simple():
#     print(i)

# def multiple_yield():
#     str1 = "First String"
#     yield str1

#     str2 = "Secound String"
#     yield str2

#     str3 = "Third String"
#     yield str3

# obj = multiple_yield()
# print(next(obj))
# print(next(obj))
# print(next(obj))

# list = [1,2,3,4,5,6,7]

# #list comprehension
# z = [x**3 for x in list]


# # Generator expression
# a = (x**3 for x in list)

# print(a)
# print(z)


# list = [1,2,3,4,5,6]
# z = (x**3 for x in list )

# print(next(z))
# print(next(z))
# print(next(z))
# print(next(z))
# print(next(z))

# def table(n):
#     for i in range(1,11):
#         yield n*i
#         i=i+1

# for i in table(15):
#     print(i)


# import sys
# # List comprehension
# nums_squared_list = [i * 2 for i in range(1000)]
# print(sys.getsizeof("Memory in Bytes:",nums_squared_list))


# #Generator Expression
# nums_squared_gc = (i ** 2 for i in range(1000))
# print(sys.getsizeof("Menory in Bytes:",nums_squared_gc))

# def infinite_sequence():  
#     num = 0  
#     while True:  
#         yield num  
#         num += 1  
  
# for i in infinite_sequence():  
#     print(i)  
