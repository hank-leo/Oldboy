#！/usr/bin/env python
# Author:Hank
import getpass

#密码匿文输入
# username=input("username:")
# password=getpass.getpass("password:")
#
# print(username,password)



#if，elif判断
_username="hank"
_password="abc123"
username=input("username:")
password=input("password:")

if _username==username and _password==password:
    print("Welcome user {name} login...".format(name=username))
else:
    print("Invalid username or password!")


