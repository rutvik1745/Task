#python program demonstrate
#abstract base class work

# from abc import ABC  

# class Car(ABC):
#     def mileage(self):
#         pass


# class Tesla(Car):
#     def mileage(self):
#         print("The mileage is 30kmph")
    
# class Suzuki(Car):
#     def mileage(self):
#         print("The mileage is 25kmph")

# class Duster(Car):
#     def mileage(self):
#         print("The mileage is 24kmph")

# class Renault(Car):
#     def mileage(self):
#         print("The mileage is 27kmph")


# #Driver code
# t = Tesla()
# t.mileage()

# r = Renault()
# r.mileage()

# d = Duster()
# d.mileage()

# s = Suzuki()
# s.mileage()


from abc import ABC
class Polygon(ABC):
    #abstract method
    def sides(self):
        pass

class Triangle(Polygon):
    def sides(self):
        print("Triangle has 3 sides")

class Pentagon(Polygon):
    def sides(self):
        print("Pentagon has 5 sides")

class Hexagon(Polygon):
    def sides(self):
        print("Hexagon has 6 sides")

class square(Polygon):
    def sides(self):
        print("I have  4 sides")

t = Triangle()
t.sides()

s= square()
s.sides()

p = Pentagon()
p.sides()

k = Hexagon()
k.sides()
