now_age=int(input("你多大："))    #一般是默认字符串类型
print("你当前的年龄是"+str(now_age))    #后续可用int后者str进行数据类型转化
# print("您当前的年龄是"+21)   整数类型不能被打印出来
print("您当前的年龄是"+str(20))  #整数类型可以转化成字符串类型用来打印
after_4years_age=now_age+2**2   #运算存储默认的类型是整数也可以是浮点数
print("四年后你的年龄是："+str(after_4years_age))   #整数类型用str进行转化






#过一下条件语句


# if now_age<20 :
#         if money>10000 :                       #双if加一个else的应用场景不广
#             print("还是个有点钱的年轻人")
#         else:
#           print("一般人")

#嵌套
money=int(input("目前有多少存款："))
# if now_age<20 :
#     print("还是一个年轻人")
# elif now_age>20 :                #此处结构if  else之间可以有多个elif
#     print("哎,老了")              #语句是一行一行执行的
# else:
#     print("刚满二十岁")
if money>1000:
    print("有钱")
elif money>100:
    print("有点小钱")
else:
    print("有点穷")                #最常见的嵌套结构：if-elif-else
