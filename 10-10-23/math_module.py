import math
# print(math.sqrt(9))

# n = int(input("Enter the number"))
# print(math.factorial(n))


# num = int(input("enter the number"))
# exp = int(input("Enter the number"))
# res = math.pow(num,exp)
# print(res)

# #calculating the Gcd
# xp = math.gcd(num,exp)
# print(xp)

# print(dir(math))


#ceil() funcation return nearest integer value

# n = eval(input())
# res = math.ceil(n)
# print(res)


#floor(): always return the nearest interger value toward negative

# n = eval(input("Enter The number"))
# res = math.ceil(n)
# print(res)


# print(math.pi)

# a = int(input("Enter the number"))  
# b = int(input("Enter the number"))  
# res = a/b  
# print("Float Division" , res)  
# res = a//b  
# print("Integer Division" , res)  
# res = a % b  
# print("Reminder", res)  


print("The value of Euler's Number is :",math.e)

print("The value of Tau is :",math.tau)

print(math.inf)
print(-math.inf)

print(math.inf > 10e109)
print(-math.inf < -10e109)

r = 4
print("The value of the circle circumference:",2*math.pi*r)


x = 4.36
y = 4.57
z = 4.99
print(f"The ceiling value of x={x} y={y} z={z}",end=" ")
print((math.ceil(x)),(math.ceil(y)),math.ceil(z))


#returning the floor value of 4.346
print(f"The ceiling value of x={x} y={y} z={z}",end=" ")
print((math.floor(x)),(math.floor(y)),math.floor(z))


a = 6

# returning the factorial of 6  
print( "The factorial of 6 is : ", math.factorial(a) )  
  
# passing a non integral number  
try:  
    print( "The factorial of 6.5 in: ", math.factorial(6.5) )  
except:  
    print( "Cannot calculate factorial of a non-integral number" )  



# declaring some value  
num1 = 4  
num2 = -3
num3 = 0.00  
   
# passing above values to the exp() function  
print( f"The exponenetial value of {num1} is: ", math.exp(num1) )  
print( f"The exponenetial value of {num2} is: ", math.exp(num2) )  
print( f"The exponenetial value of {num3} is: ", math.exp(num3) )  


# returning x to the power of y.  
print( f"The value of {x} to the power of {y} is: ", math.pow(4,5) )  

angle= math.pi/4

#Returning the sine of pi/4
print("the sin of pi/4 is :",math.sin(angle))

#Returning the cosine of pi/4
print("the sin of pi/4 is :",math.cos(angle))

#Returning the tangent of pi/4
print("the sin of pi/4 is :",math.tan(angle))


print(dir(math))