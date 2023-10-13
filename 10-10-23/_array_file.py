import array as arr

a= arr.array('i',[2,4,5,6])
print(type(a))


print("First element is:", a[0])    
print("Second element is:", a[1])   
print("Third element is:", a[2])  
print("Forth element is:", a[3])  
print("last element is:", a[-1])    
print("Second last element is:", a[-2])    
print("Third last element is:", a[-3])    
print("Forth last element is:", a[-4])    
print(a[0], a[1], a[2], a[3], a[-1],a[-2],a[-3],a[-4])  


number = arr.array('i',[0,2,3,5,7,10,])

#changing first element 1 by the value 0
number[0] = 0
print(number)

number[5] = 8
print(number)

#reolace the calue of 3rd to 5 th element by 4,6 and 8
number[2:5] = arr.array('i',[4,6,8])
print(number)

del number[0]
print(number)
print(len(number))


a = arr.array('d',[1.1,2.1,3.1,2.6,7.8])
b = arr.array('d',[3.7,8.6])
c = arr.array('d')
c=a+b
print("array c",c)
print(type(a))
print(type(b))