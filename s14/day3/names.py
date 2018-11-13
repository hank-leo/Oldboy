#！/usr/bin/env python
# Author:Hank

#names="jack jane tom hank"
names=["jack","jane","tom",["lucie","Luncy"],"hank"]

# names.append("leo")#追加
# names.insert(3,"Eric")#增加
# names[2]="canny" #修改
# names.remove("hank") #去除
# names.pop(2) #删除

# print(names.index("hank")) #位置
# print(names[names.index("hank")])

# print(names.count("hank")) #查个数

# print(names[0],names[2])

# #切片
# print(names[1:3])
# print(names[3])
# print(names[-2:])
# print(names[:3])

# names.clear() #清除

#names.reverse()
# names.sort() #排序

# print(names)
#
# names2=[1,2,3,4]
# names.extend(names2) #扩展列表
#
# del names2
# print(names,names2)

'''
#浅copy
names3=names.copy()

names[2]="leo"
names[3][0]="ray"
print(names)
print(names3)
'''

'''
#深入copy,完全独立复制
import copy

names4=copy.copy(names)

names[2]="leo"
print(names)
print(names4)
'''
print(names)

#布长
print(names[0:-1:2])

#for循环
for i in names:
    print(i)


