#！/usr/bin/env python
# Author:Hank

#装饰器---高阶函数
#
# 1.把一个函数名当做实参传给另一个函数
# (在不修改被装饰函数源代码情况下为其添加功能)
#
# 2.返回值中包含函数名(不修改函数的调用方式)
#
'''
import time
def bar():
    time.sleep(3)
    print('in the bar')

def test1(func):
    start_time=time.time()
    func()
    stop_time=time.time()
    print('the func run time is %s'%(stop_time-start_time))

test1(bar)
'''


import time
def bar():
    time.sleep(3)
    print('in the bar')

def test2(func):
    print(func)
    return func

# t=test2(bar)
# print(t)

# test2(bar())

bar=test2(bar)
bar()