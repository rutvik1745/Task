# class Animal:
#     def speak(self):
#         print("Animal Speaking")
#     #Child class Dog inherits the base class Animal
# class Dog(Animal):
#     def bark(self):
#         print("dog barking")

# d = Dog()
# d.bark()
# d.speak()


# class Animal:
#     def speak(self):
#         print("Animal Speaking")

#     # The child class Dog inherits the base class Animal
# class Dog(Animal):
#     def bark(self):
#         print("dog barking")
#     #the child class Dogchild inherits another child class Dog

# class DogChild(Dog):
#     def eat(self):
#         print("Eating bread...")

# d  = DogChild()
# d.bark()
# d.speak()
# d.eat()


# class Calculation1:
#     def Summation(self,a,b):
#         return a+b
# class Calculation2:
#     def MUltiplication(self,a,b):
#         return a*b
# class Deriverd(Calculation1,Calculation2):
#     def Divide(self,a,b):
#         return a/b

# d = Deriverd()
# print(d.Summation(10,20))
# print(d.MUltiplication(10,20))
# print(d.Divide(10,20))


# class Calculation1:
#     def Summation(self,a,b):
#         return a + b
# class Calculation2:
#     def MUltiplication(self,a,b):
#         return a*b
# class Deriverd(Calculation1,Calculation2):
#     def Divide(self,a,b):
#         return a/b

# d = Deriverd()
# print(issubclass(Deriverd,Calculation2))
# print(issubclass(Calculation1,Calculation2))
# print(issubclass(Deriverd,Calculation1))
# print(issubclass(Calculation1,Deriverd))


# class Calculation1:
#     def Summation(self,a,b):
#         return a+b

# class Calculation2:
#     def MUltiplication(self,a,b):
#         return a*b

# class Divided(Calculation1,Calculation2):
#     def Divide(self,a,b):
#         return a/b

# d = Divided()
# print(isinstance(d,Divided))

# class Animal:
#     def speak(self):
#         print("speaking")
# class Dog(Animal):
#     def speak(self):
#         print("barking")

# d = Dog()
# d.speak()


# class Bank:
#     def getroi(self):
#         return 10
# class SBI(Bank):
#     def getroi(self):
#         return 7
# class ICICI(Bank):
#     def getroi(self):
#         return 8
# b1 = Bank()
# b2 = SBI()
# b3 = ICICI()
# print("Bank rate of insterest : ",b1.getroi())
# print("SBI rate of insterest : ",b2.getroi())
# print("ICICI rate of insterest : ",b3.getroi())

# class Employee:
#     __count = 0
#     def __init__(self):
#         Employee.__count = Employee.__count+1
#     def Display(self):
#         print("The number of employees",Employee.__count)

# emp = Employee()
# emp = Employee()
# try:
#     print(emp.__count)
# finally:
#     emp.Display()


