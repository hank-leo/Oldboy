#！/usr/bin/env python
# Author:Hank

#装饰器之案例剖析1

# import time
# def timer(func): #timer(test1) func=test1
#     def deco():
#         start_time=time.time()
#         func()
#         stop_time=time.time()
#         print('the func run time is %s' %(stop_time-start_time))
#     return deco
#
# @timer
# def test1():
#     time.sleep(3)
#     print('in the test1')
#
# @timer
# def test2():
#     time.sleep(3)
#     print('in the test2')
#
# #deco(test1)
# test1()
# test2()


#装饰器通用
import time
def timer(func): #timer(test1) func=test1
    def deco(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        stop_time=time.time()
        print('the func run time is %s' %(stop_time-start_time))
    return deco

@timer
def test1():
    time.sleep(1)
    print('in the test1')

@timer
def test2(name,age):
    print('test2:',name,age)

#deco(test1)
test1()
test2('hank',22)