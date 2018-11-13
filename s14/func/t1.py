#！/usr/bin/env python
# Author:Hank
'''
def func_name(arg1,arg2,arg3,*args,**kwargs):
    print(arg1,arg2,arg3)
    print(args)
    print(kwargs)

func_name(5,2,43,99,33,11,name='hank')
'''

age=22
def change_age():
    age = 24
    print(age)

print(age)


'''
1.明确的结束条件

2.问题规模每递归一次都应该比上一次的问题规模有所减少

3.效率低
'''

