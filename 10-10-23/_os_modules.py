import os

# os.mkdir("d:\\new")

# print(os.getcwd())


# os.chdir("e:\\")
# print(os.getcwd())


# os.rmdir("d:\\new")
# os.chdir("..")
# os.rmdir("new")


# try:
#     #if file does not exist,
#     #then it throw an IOError
#     filename = "Python.txt"
#     f = open(filename,'r')
#     text = f.read()
#     f.close()

# #The Control jumps directly to here if 
# #any lines throws IOError.
# except IOError:

#     #Print(os.error) will <class'OSErro'>
#     print('Problem reading:'+filename)


# fd = "python.txt"

# file = open(fd,'w')
# file.write("This is awesome")
# file.close()
# file = open(fd,'r')
# text = file.read()
# print(text)


# file = os.popen(fd,'w')
# file.write("This is awesome ")


# fr = "pyhton.txt"
# file= open(fr,'r')
# text = file.read()
# print(text)
# os.close(file)

# fd = 'python.txt'
# os.rename(fd,"python1.txt")
# os.rename(fd,"Python1.txt")

import sys

path1 = os.access("python1.txt",os.F_OK)
print("Exist path:",path1)

# Checking access with os.R_OK     
path2 = os.access("Python.txt", os.R_OK)     
print("It access to read the file:", path2)     
      
# Checking access with os.W_OK     
path3 = os.access("Python.txt", os.W_OK)     
print("It access to write the file:", path3)     
      
# Checking access with os.X_OK     
path4 = os.access("Python.txt", os.X_OK)     
print("Check if path can be executed:", path4)    