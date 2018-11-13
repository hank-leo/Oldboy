#！/usr/bin/env python
# Author:Hank

'''
count=0
while True:
    print("count:",count)
    count=count+1
    if count==10:
        break
'''


# for i in range(0,10,2):
#     print("loop",i)

#
# for i in range(0,10):
#     if i<3:
#         print("loop",i)
#     else:
#         continue
#     print("hehe..")

for i in range(10):
    print('----------------',i)
    for j in range(10):
        print(j)
        if j >= 3:
            break
