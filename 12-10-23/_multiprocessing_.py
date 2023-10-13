# from multiprocessing import Process  
# def disp():  
#    print ('Hello !! Welcome to Python Tutorial')  
# if __name__ == '__main__':  
#      p = Process(target=disp)  
#      p.start()  
#      p.join()  



# Python multiprocessing example
# importing the multiprocessing module


# import multiprocessing
# def cube(n):
#    #This function will print the cube of the given number
#    print("The Cube is : {}".format(n*n*n))

# def square(n):
#    #This function will print the square of the given number
#    print("the Cube is {}".format(n*n))


# if __name__=="__main__":
#    # creating two processes
#    process1 = multiprocessing.Process(target = square,args=(5,))
#    process2 = multiprocessing.Process(target=cube,args=(5,))

# #Here we start the process 1
#    process1.start()
#    #Here we start process 2
#    process2.start()

#    #The join() mehod is used to wait for process 1 to complete
#    process1.join()
#    #it is used to wait for process 1 complete
#    process2.join()

#    #print if both processes are completed
#    print("both processes are finished")


# import multiprocessing
# print("the number of CPU currently working in system : ",multiprocessing.cpu_count())


#importing Queue class

# from multiprocessing import Queue

# fruit  = ['Apple','Orange','Guava','Papaya','Banana']
# count = 1
# #Creating queue objeect
# queue = Queue()

# print("Pushing items to the queue : ")
# for fr in fruit:
#    print('item no:',count,fr)
#    queue.put(fr)
#    count +=1

# print("\npoping items from the queue : ")
# count = 0
# while not queue.empty():
#    print('item no :',count,queue.get())
#    count +=1

# from multiprocessing import Lock, Process, Queue,current_process
# import time
# import queue

# def jobTodo(tasks_to_perform,complete_tasks):
#    while True:
#       try:
#          #The try block to catch task from the queue.
#          #The get_nowait() function is used to 
#          #raise queue.Empty exception if the queue is empty

#          task = tasks_to_perform.get_nowait()
#       except queue.Empty:
#          break
#       else:

#          #if no exception has been raised, the else block will execute
#          #add the task completion

#          print(task)
#          complete_tasks.put(task + " is done by" + current_process().name)
#          time.sleep(.5)
#       return True

# def main():
#    total_task = 8
#    total_number_of_processes = 3
#    tasks_to_perform = Queue()
#    complete_tasks = Queue()
#    number_of_processes = []

#    for i in range(total_task):
#       tasks_to_perform.put("Task no : " + str(i))

#    #defining number of processes
#    for w in range(total_number_of_processes):
#       p = Process(target=jobTodo,args=(tasks_to_perform,complete_tasks))
#       number_of_processes.append(p)
#       p.start()

#    #completing process
#    for p in number_of_processes:
#       p.join()

#    #print the outut
#    while not complete_tasks.empty():
#       print(complete_tasks.get())
#    return True

# if __name__=='__main__':
#    main()

# from multiprocessing import Pool  
# import time  
  
# w = (["V", 5], ["X", 2], ["Y", 1], ["Z", 3])  
  
  
# def work_log(data_for_work):  
#     print(" Process name is %s waiting time is %s seconds" % (data_for_work[0], data_for_work[1]))  
#     time.sleep(int(data_for_work[1]))  
#     print(" Process %s Executed." % data_for_work[0])  
  
  
# def handler():  
#     p = Pool(2)  
#     p.map(work_log, w)  
  
# if __name__ == '__main__':  
#     handler()  


# from multiprocessing import Pool  
# def fun(x):  
#     return x*x*x  
  
# if __name__ == '__main__':  
#     with Pool(5) as p:  
#         print(p.map(fun, [1, 2, 3]))  

# from multiprocessing import Manager
# def Manager():
#    print("this")

# manager = Manager()
# l = manager.list([i*i for i in range(10)])
# print(l)
# print(repr(l))
# print(l[4])
# print(l[2:5])