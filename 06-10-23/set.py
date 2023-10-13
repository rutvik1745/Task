# days = {"Monday","Tuesday","Wendesday","Thursday","Friday","Saturday","Sunday"}
# print(days)
# print(type(days))
# for i in days:
#     print(i)

# set1 = {1,2,3,"javatpoint",20.5}
# print(set1)

# set3 ={}
# print(type(set3))
# set4 = set()
# print(type(set4))

# set5={2,3,5,6,2,3,8,10,11,10,26,22}
# print(set5)
# set5.add(5000)
# print(set5)
# set5.update(["jully","june","march"])
# print(set5)


# set5.discard("january")
# set5.remove("june")
# print(set5)
# set5.pop()
# print(set5)

# s1 = {1,2,3}
# s2 = {2,3,4}
# s3 = {3,4,5}

# print(s1|s2)
# print(s2.union(s3))
# com = s1.union(s2,s3)
# print(com)

# print("intersection")
# print(s1.intersection(s2))
# k = s1.intersection(s2)
# print(k)

# print(s1-s2)
# print(s1^s2)

# days1 = {"Monday","Tuesday","Wednesday","Tusrday"}
# days2 = {"Monday","Tuesday"}
# day3= {"Monday","Tuesday","Friday"}

# print(days1>days2)
# print(days1<days2)
# print(days2 == day3)

# Frozenset = frozenset([1,2,3,4,5])
# print(type(Frozenset))
# for i in Frozenset:
#     print(i)

Dictionary = {"Name":"John","Country":"USA","ID":101}
print(type(Dictionary))
Frozenset = frozenset(Dictionary) #Frozenset will contain the keys of the dicionary
print(type(Frozenset))
for i in Frozenset:
    print(i)
