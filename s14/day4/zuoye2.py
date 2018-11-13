#！/usr/bin/env python
# Author:Hank
#！/usr/bin/env python
# Author:Hank
'''
程序：购物车程序

需求:

启动程序后，让用户输入工资，然后打印商品列表
允许用户根据商品编号购买商品
用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
可随时退出，退出时，打印已购买商品和余额

进一步优化购物车
用户入口：
1.商品信息保存到文件
2.已购商品和余额保存到文件中

商家入口：
1.添加商品
2.修改商品价格

'''

#商品列表
# product_list=[
#     ('iphone',5800),
#     ('Mac Pro',10200),
#     ('Watch',3000),
#     ('Bike',800),
#     ('Coffee',20)
# ]

#商品鞋标存入文件中
with open('F:/goods.txt','r') as product_list:

    #建立购物车
    shopping_list=[]

    #输入你的钱
    salary=input("请你输入当前有多少余额：")
    f = open('F:/test.txt', 'a')

    #判断余额是否为数字
    if salary.isdigit():
        salary=int(salary)
        while True: #通过while函数判断前面无错误情况下，运行以下程序
            for index,item in enumerate(product_list): # 生成商品编号
                print(index,item)
            choice=input('请输入商品编号：') # 输入商品编号
            if choice.isdigit(): #判断商品编号是否为数字
                choice=int(choice)
                if choice < len(product_list) and choice >= 0: #判断编号是否在范围内
                    p_item=product_list[choice] #将赋给p_item
                    if p_item[1] <= salary: #判断有足够的钱买当前商品
                        shopping_list.append(p_item) #买的商品放到购物车
                        salary=salary-p_item[1] #相应减少手头余额
                        print("当前商品%s已经添加到购物车,并你的手头余额已还有%s "%(p_item[0],salary))
                        f.write('已购商品：' + str(p_item[0]) + '\n' + '余额：' + str(salary) + '\n')
                    else:
                        print("你当前只有%s钱,不够买%s商品！"% (salary,p_item[0]))
                        break
                else:
                    print("没有当前商品编号！")
            elif choice=="q":
                print("----------shopping list------------") #打印商品列表
                for p in shopping_list:
                    print(p)
                print("剩下的钱：",salary)
                f.close()
                exit() #退出
            else:
                print("你输入的不是商品编号！")
                break
    else:
        print("输入余额错误！")
product_list.close()