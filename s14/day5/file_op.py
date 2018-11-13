#！/usr/bin/env python
# Author:Hank

# data=open("./yesterday",encoding="utf-8").read()
# f=open("./yesterday",encoding="utf-8")
# data=f.read()
# data2=f.read()
# print(data)
# print('----------data2----------%s---' %data2)

#写入
# f=open("./yesterday2",'w',encoding="utf-8")
# f.write("打死你个龟孙,\n")
# f.write("顶你个肺")


#追加
# f=open("./yesterday2",'a',encoding="utf-8")
# f.write("脑子瓦特了你。。。\n")
# f.write("顶你个肺")

# f=open("./yesterday2",'a',encoding="utf-8")

# f.write("\n when i was young i listen to the radio \n")
# data=f.read()
# print('----read',data)


# f=open("./yesterday",'r',encoding="utf-8")

#正常打印
# print(f.readline())
# print(f.readline())

#范围读取
# for i in range(3):
#     print(f.readline())

#使用readlines循环读取
# for index,line in enumerate(f.readlines()):
#     if index ==5:
#         print('-----------------分割线-----------------')
#         continue
#     print(line.strip())


#单行读取
# print(f.readline())


#逐行读取
# for line in f:
#     print(line)

#循环读取
# count = 0
# for line in f:
#     if count == 9:
#         print('------华丽的分割线-----------')
#         count += 1
#         continue
#     print(line)
#     count += 1


# print(f.tell()) #下标

# print(f.readline()) #单行读取
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.tell()) #读取下标
# f.seek(10)
# print(f.readline())

# print(f.flush()) #清除内存

# print(f.encoding) #文本的编码

# print(dir(f.buffer))

# print(f.fileno())

# f=open("yesterday2",'w',encoding='utf-8')

# f.write("hello 1\n")
# f.write("hello 2\n")
# f.write("hello 3\n")


#截断
# f=open("yesterday2",'a',encoding='utf-8')
# f.seek(10)
# f.truncate(20)

#读写
# f=open("yesterday2",'r+',encoding='utf-8')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.tell())
# f.seek(10)
# f.write("should be at the begining of the second")
# print(f.readline())



#写读
# f=open("yesterday2",'w+',encoding='utf-8')
# f.write("------------diao-----------\n")
# f.write("------------diao-----------\n")
# f.write("------------diao-----------\n")
# f.write("------------diao-----------\n")
# print(f.tell())
# f.seek(10)
# f.write("should be at the begining of the second")
# print(f.readline())

f=open("yesterday",encoding='utf-8')
first_line=f.readline()
print('first line:',first_line)

print('分隔线'.center(50,'-'))

data=f.read()
print(data)



f.close()

