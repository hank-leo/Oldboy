#！/usr/bin/env python
# Author:Hank
'''
编写登陆接口

输入用户名密码
认证成功后显示欢迎信息
输错三次后锁定
'''

_username="hank"
_password="123456"

count=0
while count<3:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if _username==username and _password==password:
        print("认证成功！")
        break
    else:
        print("用户名或密码输入错误！")
    count +=1
else:
    print("已输错三次,锁定！")


'''
：多级菜单

三级菜单
可依次选择进入各子菜单
所需新知识点：列表、字典
'''
