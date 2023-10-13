number = [12,75,150,180,145,525,50]

for i in number:
    if (i % 5 == 0) and i <= 150:
        print(i)
    elif i > 500:
        break
        
    