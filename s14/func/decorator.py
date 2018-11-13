#！/usr/bin/env python
# Author:Hank
'''
装饰器原则：
1.不修改被装饰的函数的源代码

2.不修改被装饰的函数的调用方式
'''

import time

def timmer(func):
    def warpper(*args,**kwargs):
        start_time=time.time()
        func()
        stop_time=time.time()
        print('the func run time is %s' %(stop_time-start_time))
    return warpper()

@timmer
def test1():
    time.sleep(3)
    print('in the test1')

