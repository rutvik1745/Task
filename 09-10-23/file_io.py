# fileptr = open("file2.txt","w")

# fileptr.write('''Pytho is the modern day langauage. it makes things so simple.
# It is the fastest-growing programing language''')

# fileptr.close()


# fileptr = open("file2.txt","r")

# if fileptr:
#     print("file is opened successfully")

# fileptr.close()


# with open("file2.txt",'r') as f:
#     content= f.read();
#     print(content)


# fileptr = open("file2.txt","a")
# fileptr.write("java has an easy syntax and usesr-friendly interaction")
# fileptr.close()


# fileptr = open("file2.txt","r")
# content = fileptr.read(10)
# print(type(content))
# print(content)
# fileptr.close()


# fileptr = open("file2.txt","r");     
# #running a for loop     
# for i in fileptr:    
#     print(i) # i contains each line of the file  

# def square(number):
#     result = number**2
#     return result

# ip = []
# fileptr = open('accesslogs320mb.log','r')
# c = []
# for i ,id in enumerate(fileptr):
#     #  print(i.split(" - - "))
#     #  print(i)
#     if i == 0:
#         pass
#     else:
#         c.append(id.split(" "))
#         ip.append(c[0])
        
        

# print(c[0][0])
# print(len(c))
# for i in range(len(c)):
#     print(c[i][0])
#     if i >=10:
#         break