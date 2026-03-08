d={"name":"afeng","age":18,"gender":"male","小明":"del演示","小红":"pop演示"}
print(d["name"])
#print(d[0])       字典不能用索引去打印，要用相应的键
d["weight"]=175            #可以直接输入键值对对应添加
print(d)
if "afeng" in d.values() :   #想要查看某个值是否存在，要加上.values
    print("有afeng这个")
if "name" in d:
    print("有name这个键")
del d["小明"]  #del不只能删除键，还能删除整个字典的内容
print(d)
deleted=d.pop("小红")
print(deleted)               #和del的一个区别：del没有返回值，pop有
print(d)
for k,v in d.items():       #items是列举出字典全部的键值对
     print(f"{k}：{v}")      #for循环先遍历一遍字典，相应的位置可以直接
                             #设置参数用字符串格式化转出
print(list(d.keys()))   #list是全局内置函数，能将里面的键输出成全新的列表
print(list(d.values()))  #这个同理，打印出值转换成列表
#最后还有一个元组相关的东西
d_1={("阿峰,18"):122222,
     ("阿峰,47"):111111,
     ("阿峰,98"):123455}       #元组能同时解决多个相同键名的问题
print(d_1["阿峰,18"])