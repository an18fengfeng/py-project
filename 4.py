practice_list=["language_python" ]
practice_list.append("html网页定位")       #写法列表名.方法名
print(practice_list)              #列表不用重新赋值给原变量
practice_list.remove("html网页定位")
print(practice_list)
practice_list.append(1)
practice_list.append(True)
print(practice_list)          #python列表可以存不同的数据类型
number_list=[2,1,22,0.1,-1]
number_list.sort()       #列表可以对浮点数，正负数进行排序
print(number_list)
print(practice_list[1])         #列表同样可以用索引
print(max(number_list))
print(min(number_list))               #找最大最小值
print(sum(number_list))               #累加
print(sorted(number_list))            #此处是内置函数 和第10行是一样的效果

#这里有一个区别
s="hello"
s.upper()
print(s.upper())
print(s)               #由此看出列表是可变的，不用重新给变量赋值
                       #那之前学的整型，浮点数，字符串都是不可变的

# aa=1,1,2,4         然后查了一下，这是一个叫元组的东西，和列表很像，但也是不可变的
# aa.sort()          元组是用圆括号包起来的(区别于列表的方括号)，反正都要用逗号隔开
# print(aa)        这里就因为不是列表的问题，是不能修改自身的元素和长度的(自然不能用一些列表的方法)
