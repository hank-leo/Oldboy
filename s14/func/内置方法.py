#！/usr/bin/env python
# Author:Hank

#all()函数
# print(all([0,-1,3]))
# print(all([1,-1,3]))

#any()函数
# print(any([]))

#ascii()函数
# a=ascii([1,2,"哈哈哈"])
# print(a)

#bin()函数 二进制
# print(bin(6))
# print(bin(255))

#bool()函数
# print(bool([]))
# print(bool([1]))

#bytes()
# a=bytes("abcde",encoding="utf-8")
# b=bytearray("abcde",encoding="utf-8")
# print(b[1])
#
# b[1]=200
# print(b)
# print(a.capitalize(),a)

# def sayhi():pass
# print(callable([]))

#chr() 位置
# print(chr(87))
# print(chr(89))
# print(chr(81))

# def fib(max):
#     n,a,b=0,0,1
#     while n < max:
#         yield a,b == b, a + b
#         #a=b a=1,b=2,a=b,a=2,b=a+b b=2+2=4
#         n=n+1
#     return '---done---'
# f=fib(3)
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())

# g=fib(6)
# while True:
#     try:
#         x = next(g)
#         print('g:',x)
#     except StopIteration as e:
#         print('Generator return value:',e.value)
#         break

# def sayhi(n):
#     print(n)
#     for i in range(n):
#         print(i)
# sayhi(3)

# a=lambda n:print(n)
# a(5)
# a(10)

# calc = lambda n:3 if n<4 else n
# print(calc(5))

# res = filter(lambda n:n>5,range(10))
# res = map(lambda n:n*2,range(10))


# import functools
# res = functools.reduce(lambda  x,y:x*y,range(1,10))
# print(res)

# a=frozenset([1,2,44,55,6,778,9,2])
# print(a)

# def test():
#     local_var = 333
#     print(locals())

# test()
# print(globals())
# print(globals().get('local_var'))

# a={6:2,8:0,1:4,-5:6}
# print(sorted(a.items())) #按升顺排列
# print(sorted(a.items(),key=lambda x:x[1])) #按降序排列
# print(a)

# a=[1,2,3,4,5,6]
# b=['a','b','c','d']
# for i in zip(a,b):
#     print(i)


# import decorator
__import__('decorator')