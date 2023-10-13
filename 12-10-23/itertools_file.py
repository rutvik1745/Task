# import itertools
# a = [1,2,3]
# b = ['a','b','c']
# c = zip(a,b)
# print(c)

# a = iter('Hello')
# print(a)


# import itertools

# for i in itertools.count(10,5):
#     if i == 50:
#         break
#     else:
#         print(i,end=" ")

# import itertools
# temp = 0
# for i in itertools.cycle("123"):
#     if temp > 7:
#         break
#     else:
#         # print(temp)
#         print(i,end=" ")
#         temp = temp+1

# import itertools

# val = ['java','t','point']

# iter = itertools.cycle(val)

# for i in range(6):
#     #using next function
#     print(next(iter),end=" ")

# import itertools
# print("Printing the number repeadtly:")
# print(list(itertools.repeat(40,15)))

# from itertools import product

# print("We ate computing cartesian product using repeat keyword Argument:")
# print(list(product([1,2],repeat = 2)))

# print()

# print("Weare computing cartesian product of the containers:")
# print(list(product(["Java","T","Point"],"5")))
# print()

# print("We are computing product of the containers:")
# print(list(product("CD",[4,5])))

# from itertools import permutations

# print("Computing all permutation of the following list")
# print(list(permutations([3,"Python"],2)))
# # print()

# print("Permutations of following string")
# print(list(permutations('AB')))
# # print()

# print("Permutation of the given container is :")
# print(permutations(range(4),2))
# print()

# from itertools import combinations
# print("Combination of list in sorted order(Witout replacement)",list(combinations(['b',3],1)))

# print("Combination of string in sorted order ",list(combinations("zx",2)))

# print("Combination of list in sorted order",list(combinations(range(20),1)))

# from itertools import combinations_with_replacement

# print("Combination of string in sorted order (with replacement) is :")
# print(list(combinations_with_replacement("XY",3)))

# print("Combination of string in sorted order (with replacement) is :")
# print(list(combinations_with_replacement([4,2],3)))

# print("Combination of string in sorted order (with replacement) is :")
# print(list(combinations_with_replacement(range(3),2)))

# import itertools
# import operator

# #initalizing list1
# list1 = [1,4,5,7,9,11]

# #using accumulate() that will pass prints the summation of elements
# print("The sum is :",end=" ")
# print(list(itertools.accumulate(list1)))

# #using accumulate() that will pass prints the multiplication of elements
# print("The sum is :",end=" ")
# print(list(itertools.accumulate(list1,operator.mul)))


# import itertools

# #Declaring list 1
# list1 = [1,2,3,4]

# #Declaring list 2
# list2 = [1,5,6,8]

# #Declaring list 3
# list3 = [9,10,11,12]

# #using chain() function that will to print all elements of lists
# print("The output is : ",end=" ")
# print(list(itertools.chain(list1,list2,list3)))


# import itertools
# #initializing list

# list1 = [2,4,5,7,8]

# #using dropwhile() iteator that will print displaying after condition is false
# print("The output is :",end=" ")
# print(list(itertools.dropwhile(lambda x:x%2 == 0,list1)))
# print(list)


# import itertools

# #Using filterfalse()iterator that will print false value
# print("The output is :",end=" ")
# print(list(itertools.filterfalse(lambda x:x%2 == 0,list1)))


# import itertools

# list1 = [12,34,65,73,80,19,20]

# #using islice() iterator  that will slice the list acc.to given argument
# #starts priting from  3nd index till 8th skipping 2
# print("The sliced list values are :",end="")
# print(list(itertools.islice(list1,2,8,2)))


# import  itertools

# #Declaring list that contain tuple as element
# list1 = [(10,20,15),(18,40,19),(53,42,90),(16,12,27)]

# #using starmap() iterator for selection value acc.to function
# #select max of all tuple value

# print("The value acc.to function are : ",end="")
# print(list(itertools.starmap(max,list1)))


# import itertools
# #initializing list

# list1 = [20,42,64,77,8,10,20]

# #using takewhile() iteator is used to print values till condition return false
# print("The output is :",end=" ")
# print(list(itertools.takewhile(lambda x:x%2 == 0,list1)))
# print(list)

# import itertools

# #Declaring list
# li = [1,2,3,4,5,6,7]

# #storing list in itertor
# iti = iter(li)

# #using tee() iterator to create a list of iterators
# #Creating list of 3 iterators having similar values
# it = itertools.tee(iti,3)
# #it will print object of iterator

# print(it)
# print("the iterators are : ")
# for i in range(0,2):
#     print(list(it[i]))

import itertools
print("The combined value of iterrables is :")
print(*(itertools.zip_longest('Java','Tpoint',fillvalue='_')))