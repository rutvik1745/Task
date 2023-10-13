# number = [3,5,8,3,6,10,11,2,3,5,6]

# sum = 0
# for num in number:
#     sum = sum + num**2
# print("The sum of squares is :",sum)



# list = [3,5,6,7,8,9,10]
# for i in range(len(list)):
#     list.append(list[i]+2)
# print(list)

# student_name_1 = 'Itika'
# student_name_2 = 'Paraker'


# records = {'Itika':90,'Arshia':92,'Peter':46}
# def marks(student_name):
#     for a in records:
#         if a == student_name:
#             return records[a]
#             break
#         else:
#             return f'There is no student of name {student_name} in the records'

# print(f"Marks of {student_name_1} are:",marks(student_name_1))
# print(f"Marks of {student_name_2} are:",marks(student_name_2))


import random
number = []
for val in range(0,11):
    number.append(random.randint(0,11))
print(number)
for num in range(0,11):
    for  i in number:
        if num == i:
            print(num,end=' ')
        