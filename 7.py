class student:                                             #父类
    def __init__(self,name,stu_id):
        self.name = name                                   #用来定义通用属性
        self.id = stu_id
    def red(self):                                     #父类定义的方法。后续子类也能直接调用
        print(self.name+"正在读书")
afeng=student("阿峰",1)
print(afeng.name)
afeng.red()
class college(student):                            #子类(第一种用法可以不初始化参数，因为他没有除了父类外的其他属性)
    def fall_in_love(self):
        print(f"{self.name},你是大学生可以谈恋爱")
afengfeng=college("阿峰峰",2)
afengfeng.fall_in_love()                               #不同子类之间调用各自的函数
afengfeng.red()
class elementary(student):
    def __init__(self,name,stu_id,sex):             #第二种用法要初始化，因为有额外属性，子类参数（属性）可以比父类多些
        super().__init__(name,stu_id)                 #super写法：后面的参数必须和父类保持一致
        self.sex = sex
    def no_smart_phone(self):
        print(f"{self.name},你是小学生不能玩手机")
xiaofeng=elementary("小峰",3,"男")
print(f"姓名：{xiaofeng.name} 学号：{xiaofeng.id} 性别：{xiaofeng.sex}")
xiaofeng.no_smart_phone()
xiaofeng.red()                                   #子类调用父类方法
class middle(student):
    def __init__(self,school,stu_class,*args,nationality="中国" ,**kwargs): #子类函数自定义的参数的写法：# 子类专属必选位置参数 → *args → 子类专属带默认值的关键字参数 → **kwargs
     super().__init__(*args,**kwargs)                    #*args + **kwargs能直接代表父类参数，避免参数太多的问题
     self.school = school
     self.stu_class = stu_class
     self.nationality = nationality
stu_1=middle("八中","3班","小黄","04",nationality="美国")       #直接参数=值，去修改默认值
print(f"姓名：{stu_1.name} 学号：{stu_1.id} 学校：{stu_1.school},班级：{stu_1.stu_class} 国籍:{stu_1.nationality}")
#如果不想按定义时的顺序传参，必须用关键字参数（参数=值）如果按顺序传，可以直接写值，不用写参数名
