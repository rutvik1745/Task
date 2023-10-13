#Python profram to show how  __init__ method works

#Creating a Class

class methods():
    def __init__(self,*args):
        print("Now called __init__ magic method, agter the initialised parameters")
        self.name = args[0]
        self.std = args[1]
        self.marks = args[2]


student = methods("ltika",11,98)
student1 = methods("Rutvik",12,45)
print(student)
print(f"Name,standard,and marks of the student is : \n",student.name,"\n",student.std,'\n',student.marks)



#Python program to show How __new__method works

#Creting a class
class Method(object):
    def __new__(cls):
        print("Creating instance by __new__ method")
        return super(Method,cls).__new__(cls)
    #Calling the init method
    def __init__(self):
        print("init method is called here")

Method()
s= Method()



#python program to show how to add two attributes

#Creating a second class
class method:
    def __init__(self,argument):
        self.attributes = argument

#Creating a second clss
class method2:
    def __init__(self,argument):
        self.attributes = argument

#Creating The instances
instance_1 = method("Attribute")
print(instance_1.attributes)

instance_2 = method2("27")
print(instance_2.attributes)

#Adding two attributes of the instance
print(instance_1.attributes + instance_2.attributes)
print(instance_2.attributes + instance_1.attributes)



#Python program to show how __add__methods works

#Creating a class
class method_1:
    def __init__(self,argument):
        self.attributes = argument
    def __add__(self,object1):
        return self.attributes + object1.attributes

#creating a secound class
class method_2:
    def __init__(self,argument):
        self.attributes = argument
    def __add__(self,object1):
        return self.attributes + object1.attributes
    
instance1 = method_1("Attribute")
print(instance1)
instance2 = method_2("25")
print(instance2)
print(instance2 + instance1)



#Python program to show how __repr__ magic method works


#Creating class
class method_3:
    #Calling __init__method and initializing the attributes of the class
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        #Calling the __repr__ method and providing the string to be printed each time instance is prime
    
    def __repr__(self):
        return f"Following are the values of the attributes of the class Method:\nx = {self.x}\ny = {self.y}\nz = {self.z}"

i= method_3(4,5,3)
print(i)


#Python code to show how the __contains__ magic method works

#Creating a class

class method_4:
    #Calling the __init__ method and initializing the attributes
    def __init__(self,attribute):
        self.attribute = attribute

    #Calling the __contains__ method
    def __contains__(self,attribute):
        return attribute in self.attribute
    
#Creating an instance of the class
instance = method_4([4,6,8,9,1,6])

#Checking if a value is present in the container attribute
print(" 4 is contained in ""attrobute"":",4 in instance)
print(" 5 is contained in ""attrobute"":",5 in instance)
print(instance)


#python program to show how the __call__ magic method works


#Creating a class
class method5:
    #Calling the __init__ method and initalizing the attributes
    def __init__(self,a):
        self.a = a
    #Calling the __call__ method to multipy a number to the attribute value
    def __call__(self,number):
        return self.a*number

#Creating instance and proving the value to the attribute a
instance = method5(7)
print(instance.a)#Printing the value of the attribute a
#Calling the instance while passing a value which will call the  __call_ method
print(instance(5))
print(instance)




#ython program to show how the __iter___method works

#Creating a class
class method6:
    def __init__(self,start_value,stop_value):
        self.start = start_value
        self.stop  = stop_value
    def __iter__(self):
        for num in range (self.start,self.stop+1):
            yield num **2
    
    #Creating an instance
instance = iter(method6(3,8))
print(next(instance))
print(next(instance))
print(next(instance))
print(next(instance))
print(next(instance))
print(next(instance))
print(instance)