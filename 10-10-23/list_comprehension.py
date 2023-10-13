person = ["Piyali","Hiya","Rudrashish","Badsha","Lipi"]
newlist = [x for x in person if "i" in x]
print(newlist)


#syntax
# newlist = [expression for item in iterable if condition == True]

#using for loop to iterate through item in list

number = [3,5,1,7,3,9]
num = []

for i in number:
    num.append(i**2)

print(num)


#using list comprehension to iterate through list items

number1 = [3,5,1,7,3,9,1]

x = [n**2 for n in number1]
print(x)

#import module to keep track of time
import time

#defining function to execute for loop
def for_loop(num):
    l = []
    for i in range(num):
        l.append(i+10)
    return l

#defining funcation to execute list comprehension
def list_comprehension(num):
    return [i + 10 for i in range(num)]


#Giving values to the funcation

#Calculating time taken by the loop

start = time.time()
for_loop(10000000)
end = time.time()

print("Time taken by the loop :",(end-start))


#Calculating time taken by list comprehension
start= time.time()
list_comprehension(10000000)
end =time.time()

print("Time taken by the loop:",(end - start))



x = "Javatpoint"
print([alpha for alpha in x])


letter = [alpha for alpha in 'javatpoint']
print(letter)


number_list = [num for num in range(30) if num %2 ==0]
print(number_list)


def Sum(n):
    dsum = 0
    for ele in str(n):
        dsum += int(ele)
    return dsum
list = [47,69,73,97,105,845,307]
newList = [Sum(i) for i in list if i & 1]  
print(newList)  


nested_list = []

for _ in range(3):
    #append an empty syblist inside the list
    nested_list.append([])

    for i in range(5):
        nested_list[_].append(i+_)
print(nested_list)

#Nested list comprehension
nested_list1 = [[_+i for _ in range(5)] for i in range(3)]
print(nested_list1)