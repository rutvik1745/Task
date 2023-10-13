# x = ["Python","C","Android"]
# x.append("Java")
# x.append("C++")
# print(x)
# print(x.pop())
# print(x)
# print(x.pop())
# print(x)


import queue
#Queue is created as an object 'L'
L = queue.Queue(maxsize= 10)

#Data is inserted in 'L' at the end using put()
L.put(9)
L.put(6)

#get()takes data from
#from the head
#of the Queue

print(L.get())
print(L.get())

