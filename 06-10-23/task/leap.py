x = int(input("Enter the Year : "))

if x % 400==0 :
    print("Yes")
elif x % 100==0:
    print("no")
elif x % 4==0:
    print("yes")
else:
    print("No")