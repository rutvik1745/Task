num = int(input("Enter The number : "))

for i in range(2,num//2):
    if num % i == 0:
        print("NO")
        break
else:
    print("YES")