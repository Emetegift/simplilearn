## Threading in Python

'''
A PROCESS is an executable instance of a computer program.
THREAD is a sequence of instructions in aprogram that can be executed independently of the remaining program. 
This simply means that a thread exist within a pocess.
The the threading function can be written in different ways as shown below:
'''
# # a. Most Basic

# from threading import *

# def show():
#     print("This a chld thread")
# t = Thread(target=show())
# t.start() #This will start the target function, i.e the "show" above
# print("This is the parent thread")


# # b. This is done by importing a class;

# from threading import *
# class MyThread(Thread):
#     def run(self):
#         for i in range(5):
#             print("This is a child thread")
# t = MyThread()
# t.start()
# for i in range(5):
#     print("This is the parent thread")
    
    
# # c. In this, the tread class is not imported;
# from threading import *
# class Demo:
#     def show (self):
#         for i in range(5):
#             print("This is a child thread")
# obj = Demo()
# t =Thread(target=obj.show)
# t.start()
# for i in range(5):
#     print("This is the parent thread")


"""
Multithreading: This is model in which multiple threads within a process is executed independently,
while sharing the same resources. 
    
"""
from threading import *
import time
class Demo:
    def num(self):
        for i in range(6) :
            print("The number is:", i) ## This will print the single numbers between the range of 6
            time.sleep(2) ## This will allow  each thread to execute properly before another thead gets executed
            
    def double(self):
        for i in range(1,6) :
            print("The double of the number is:", 2*i) ## This will print the double of the numbers in this range
            time.sleep(1)
            
    def square(self):
        for i in range(1,6) :
            print("The sqaure root of the number is:", 1*i) ## This will print the square root of the numbers in this range
            time.sleep(1)
obj = Demo()
t1 = Thread(target=obj.num)
t2 = Thread(target = obj.double)
t3 = Thread(target =obj.square)
t1.start()
time.sleep(0.5)
t2.start()
time.sleep(0.5)
t3.start()

# To make sure each function is executed separately and orderly;
t1.join()
t2.join()
t3.join()