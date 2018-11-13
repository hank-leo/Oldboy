#！/usr/bin/env python
# Author:Hank

def fib(max):
    n,a,b=0,0,1
    while n < max:
        #print(b)
        yield b #生成器
        a,b=b,a+b
        n=n+1
    return '-------done---------'

#f=fib(10)
g=fib(100)
while True:
    try:
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break

# print(f.__next__())
# print("=======")
# print(f.__next__())
# print("=======")
# print(f.__next__())
# print("=======")
# print(f.__next__())

# print("=====start loop=======")
# for i in f:
#     print(i)