
#python Conditional Statements


# x = 10
# y = 5

# if x > y :
#     print("x is greater than y")
# else:
#     print("y is greater than or equal to x")

# x = 5
# y = 10

# if x > y :
#     print("x is greater than y")
# else:
#     print("y is greater than or equal to x")




#Python Loop

# fruits = ["apple","banana","cherry"]
# for x in fruits:
#     print(x)




#python While Loop
# i=1
# while i < 6:
#     print(i)
#     i+=1



#python Exceptions
# try:
#     x = int(input("Enter a number:"))
#     y = 10/x
#     print("Result",y)
# except ZeroDivisonError:
#     print("Error: Division by zero")
# except ValueError:
#     print("Error: invalid input")



# import csv

# with open('data1.csv','r')as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)




# import csv

# data = [["Name",'Age','Country'],
#     ['Alice','25','USA'],
#     ['Bob','30','Canada'],
#     ['Charlie','35','Australia']]

# with open('data1.csv','w')as file:
#     writer = csv.writer(file)
#     for row in data:
#         writer.writerow(row)


#python Magic Methods

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

def __str__(self):
    return f"{self.name}({self.age})"