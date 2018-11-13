#！/usr/bin/env python
# Author:Hank
'''
请闭眼写出以下程序。

程序：购物车程序

需求:

启动程序后，让用户输入工资，然后打印商品列表
允许用户根据商品编号购买商品
用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
可随时退出，退出时，打印已购买商品和余额
'''
product_list=[
    ('Iphone',5800),
    ('Mac Pro',9800),
    ('Bike',800),
    ('Watch',10600),
    ('Coffee',31),
    ('Alex Python',120)
]

shopping_list=[] #创建空的购物车
salary=input("Input your salary:") #输入你的余额
if salary.isdigit(): #判断是否为数字
    salary=int(salary)
    while True:
        for index,item in enumerate(product_list): #enumerate建立索引
            print(index,item)
        user_choice=input("选择要买嘛?>>>：") #输入选择索引
        if user_choice.isdigit(): #判断输入是否为数字
            user_choice=int(user_choice)
            if user_choice < len(product_list) and user_choice >=0: #输入的数字大于等于0并小于商品列表的长度
                p_item = product_list[user_choice] #赋给p_item变量
                if p_item[1] <= salary:  #判断是否小于等于余额
                    shopping_list.append(p_item) ##添加到购物车
                    salary-=p_item[1] #总得余额相应减少
                    print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m" % (p_item, salary)) #打印购买的商品和剩余金额
                else:
                    print("\033[41;1m你的余额只剩[%s]啦，还买个毛线\033[0m" % salary) #打印剩余金额小于当前商品价格
            else:
                print("product code [%s] is not exist!" % user_choice) #当前没有商品的序号
        elif user_choice == 'q': #退出
            print("--------shopping list------") #打印商品列表
            for p in shopping_list:
                print(p)
            print("Your current balance:", salary) #打印剩余金额
            exit()
        else:
            print("invalid option") #不是数字