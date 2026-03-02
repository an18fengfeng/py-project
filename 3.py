now_age=int(input("你多大："))    #一般是默认字符串类型
print("你当前的年龄是"+str(now_age))    #后续可用int后者str进行数据类型转化
# print("您当前的年龄是"+21)   整数类型不能被打印出来
print("您当前的年龄是"+str(20))  #整数类型可以转化成字符串类型用来打印
after_4years_age=now_age+2**2   #运算存储默认的类型是整数也可以是浮点数
print("四年后你的年龄是："+str(after_4years_age))   #整数类型用str进行转化






#过一下条件语句


# if now_age<20 :
#         if money>10000 :
#             print("还是个有点钱的年轻人")

#嵌套
if now_age<20 :
    print("还是一个年轻人")
elif now_age>20 :
    print("哎,老了")
else:
    print("刚满二十岁")
money=int(input("目前有多少存款："))
if money>100:
    if money>1000:
        print("有钱")
    else:
        print("有点小钱")
else:
    print("有点穷")
