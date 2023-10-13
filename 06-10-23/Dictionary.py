# dict = {"Name":"Rutvik","Age":25}
# print(dict)

dict1 = {} #Creating an empty Dictionary
print("Empty Dictionary")
print(dict1)

# Creating a Dictionary
#With dict() mehod

dict2 = dict({1:'Hcl',2:'Wipro',3:'Facebook'})
print(dict2)
print("name",dict2[1])

#Adding elements to dictionary one at a time
dict2[4] = 'Ricky'
print(dict2)
dict2["Ram"] = [20,10,30,40]
dict2["Radhe"] = 10,20,30
print(dict2)
#Deleting a key
#using del mehod
del dict2[1]
print(dict2)
#Deleting a key
#using pop() method
dict2.pop(3)
print(dict2)

#for loop to print all the keys of dictionary

for x in dict2:
    print(x)

#for loop to print the vaalues of the dictionary by using values() method.
for x in dict2.values():
    print(x)

# for loop to print the items of the dictionary by using items() method
for x in dict2.items():
    print(x)

for x,y in dict2.items():
    print(x,y)

print(len(dict2))#printing len of dictionary

dict3 = {1:"Ayan",2:"Bunny",4:"Ram",3:"Bheem"}
any({'':'','':'','3':''})  
all({1:'',2:'','':''})  
print(all)
print(any)

print(sorted(dict3))


dict4 =dict3.copy()# copy() method 
print(dict4)
dict4.clear()# clear() method
print(dict4)

dict3.pop(1)# pop() method
print(dict3)

dict3.popitem()# popitem() method  
print(dict3)

print(dict3.keys()) # keys() method   

print(dict3.items())# items() method    

print(dict3.get(2))# get() method

dict3.update({3:"TCS"})# update() method 
print(dict3)

print(dict3.values())