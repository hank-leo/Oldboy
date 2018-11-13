#！/usr/bin/env python
# Author:Hank

import sys

f=open("yesterday2","r",encoding="utf-8")
f_new=open("yesterday2.bak","w",encoding="utf-8")

# for line in f:
#     if "肆意的快乐等我享受" in line:
#         line=line.replace("肆意的快乐等我享受","肆意的快乐等hank享受")
#     f_new.write((line))
# f.close()
# f_new.close()
#

#使用argv替换
# find_str=sys.argv[1]
# repalce_str=sys.argv[1]
#
# for line in f:
#     if find_str in line:
#         line=line.replace((find_str,repalce_str))
#     f_new.write(line)
# f.close()
# f_new.close()

# 自动关闭文件
# with open("yesterday2","r",encoding="utf-8") as f:
#     for line in f:
#         print(line)

with open("yesterday2","r",encoding="utf-8") as f:
    for line in f:
        print(line)

