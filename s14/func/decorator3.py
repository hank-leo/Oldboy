#！/usr/bin/env python
# Author:Hank

#装饰器---嵌套函数

'''
def foo():
    print('in the foo')
    def bar():
        print('in the bar')

    bar()

foo()
'''


#局部作用域和全局作用域的访问顺序
x=0
def grandpa():
    x=1
    def dad():
        x=2
        def son():
            x=3
            print(x)
        son()
    dad()
grandpa()