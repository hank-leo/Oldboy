#！/usr/bin/env python
# Author:Hank

hank_age=24

#while循环
# count=0
# while count<3:
#     guess_age = int(input("输入猜测年龄："))
#     if guess_age==hank_age:
#         print("yes")
#         break
#     elif guess_age<hank_age:
#         print("think bigger...")
#     else:
#         print("think small...")
#     count+=1
# else:
#     print("you have tried too many times...fuck off")


#for循环
for i in range(3):
    guess_age = int(input("输入猜测年龄："))
    if guess_age==hank_age:
        print("yes")
        break
    elif guess_age<hank_age:
        print("think bigger...")
    else:
        print("think small...")
else:
    print("you have tried too many times...fuck off")