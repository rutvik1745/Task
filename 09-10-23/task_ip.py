ip = []
fileptr = open('accesslogs320mb.log','r')
c = []
for i ,id in enumerate(fileptr):
    #  print(i.split(" - - "))
    #  print(i)
    if i == 0:
        pass
    else:
        c.append(id.split(" "))
        ip.append(c[0])
        
        

print(c[0][0])
print(len(c))
for i in range(len(c)):
    print(c[i][0])
    if i >=10:
        break