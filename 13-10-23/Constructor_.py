# class Employee:
#     def __init__(self,name,id):
#         self.id = id
#         self.name = name

    
#     def display(self):
#         print("Id : %d\nName : %s"%(self.id,self.name))


# emp1 = Employee("John",101)
# emp2 = Employee("David",102)

# # Accessing display() method to print employee 1 information
# emp1.display()


# # Accessing display() method to print employee 2 information

# emp2.display()



# class Student:
#     count= 0
#     def __init__(self):
#         Student.count = Student.count+1


# s1 = Student()

# s2 = Student()


# s3 = Student()
# print("The number of student : ",Student.count)




# class Student:
#     #Construtor -non parameterized
#     def __init__(self):
#         print("This is non parametrized constructor")
#     def show(self,name):
#         print("Hello",name)
# student = Student()
# student.show("John")
# student1 = Student()
# student.show("Ravi")



# class Student:
#     #Constructor - parameterized
#     def __init__(self,name):
#         print("This is Parametrized constructor")
#         self.name = name
#     def show(self):
#         print("Hello",self.name)

# student = Student("John")
# student.show()


# class Student:
#     roll_num = 101
#     name = "Joseph"

#     def display(self):
#         print(self.roll_num,self.name)

# st = Student()
# st.display()


# class Student:
#     def __init__(self):
#         print("The First Constructor")
#     def __init__(self):
#         print("The Secound constructor")

# st = Student()



# class Student:
#     def __init__(self,name,id,age):
#         self.name = name
#         self.id = id
#         self.age = age

#         #creates the object of the class student
# s= Student("John",101,22)
# print(s)

# #prints the attribute name of the objects
# print(getattr(s,"name"))

# #reset the value of attribute age to 23
# setattr(s,"age",23)

# #print the modified value of age
# print(getattr(s,'age'))

# #print true if the student contains the attribute with name id
# print(hasattr(s,'id'))
# delattr(s,'age')

# #this will give an error since the attribute age has been deleted
# print(s.age)


# class Student:
#     def __init__(self,name,id,age):
#         self.name = name
#         self.id = id
#         self.age = age
#     def display_details(self):
#         print("Name : %s, ID : %d , age : %d"%(self.name,self.id))
# s = Student("John",101,22)
# print(s.__doc__)
# print(s.__dict__)
# print(s.__module__)

