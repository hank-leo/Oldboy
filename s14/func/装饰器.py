#！/usr/bin/env python
# Author:Hank

'''
def foo():
    print('foo')

# foo #表示函数
foo() #表示执行foo函数
'''

'''
def foo():
    print('foo')

foo1 = lambda x:x+1

foo(2)
'''


'''
def w1(func):
    def inner():
        print('已验证')
        return func()
    return inner

@w1
def f1():
    print('f1')
'''

'''
#被装饰的函数如果有参数呢？
def w1(func):
    def inner(arg):
        # 验证1
        # 验证2
        # 验证3
        return func(arg)
    return inner

@w1
def f1(arg):
    print ('f1')
'''


'''
初创公司有N个业务部门，1个基础平台部门，基础平台负责提供底层的功能，如：数据库操作、redis调用、监控API等功能。
业务部门使用基础功能时，只需调用基础平台提供的功能即可。如下：
'''

'''
def f1():
    print('f1')


def f2():
    print('f2')

def f3():
    print('f3')

def f4():
    print('f4')

f1()
f2()
f3()
f4()
'''

#只对基础平台的代码进行重构，其他业务部门无需做任何修改
'''
def check_login():
    pass

def f1():
    check_login()
    print('f1')


def f2():
    check_login()
    print('f2')

def f3():
    check_login()
    print('f3')

def f4():
    check_login()
    print('f4')

f1()
f2()
f3()
f4()
'''


'''
写代码要遵循开发封闭原则，虽然在这个原则是用的面向对象开发，但是也适用于函数式编程，简单来说，它规定已经实现的功能代码不允许被修改，但可以被扩展，即：

封闭：已实现的功能代码块
开放：对扩展开发

如果将开放封闭原则应用在上述需求中，那么就不允许在函数 f1 、f2、f3、f4的内部进行修改代码
'''
'''
def w1(func):
    def inner():
        # 验证1
        # 验证2
        # 验证3
        return func()

    return inner

@w1
def f1():
    print('f1')

@w1
def f2():
    print('f2')

@w1
def f3():
    print('f3')

@w1
def f4():
    print('f4')
'''

#一个函数可以被多个装饰器装饰吗？
'''
import time
def w1(func): #timer(test1) func=test1
    def deco(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        stop_time=time.time()
        print('the w1 run time is %s' %(stop_time-start_time))
    return deco

def w2(func): #timer(test1) func=test1
    def deco(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        stop_time=time.time()
        print('the w2 run time is %s' %(stop_time-start_time))
    return deco

@w1
@w2
def f1(name,age):
    time.sleep(1)
    print('f1:',name,age)

f1('hank',22)
'''

#还有什么更吊的装饰器吗？

def Before(request,kargs):
    print('before')

def After(request,kargs):
    print('after')

def Filter(before_func,after_func):
    def outer(main_func):
        def wrapper(request,kargs):

            before_result=before_func(request,kargs)
            if(before_result!=None):
                return before_result

            main_result=main_func(request,kargs)
            if(main_result!=None):
                return main_result

            after_result=after_func(request,kargs)
            if(after_result!=None):
                return after_result

        return wrapper
    return outer

@Filter(Before,After)
def Index(request,kwargs):
    print('index')

Index('hank','leo') #运行函数