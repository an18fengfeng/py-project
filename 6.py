class student:
   def __init__(self,name,stu_id):            #init是常用的实例初始化方式，要给每个实例设置独有的个性化属性-->必须要有
       self.name=name
       self.stu_id=stu_id
       self.grades={"语文":0,"数学":0,"英语":0}
   def  set_grade(self,course,grade):                 #修改成绩
       if course in self.grades:
           self.grades[course] = grade                  #这里是字典的常规用法，类似于列表list[0],对应值
   def print_grade(self):
       print(f"学生:{self.name}(学号：{self.stu_id})的成绩为：")
       for course in self.grades:                        #遍历字典用于下面打印
           print(f"{course}:{self.grades[course]}分")

#student_1=("小明","01")        #这里要有一个变量去存储，这样写只是创建了一个元组
xiaoming=student("小明","01")#定义类好比定义了一个函数 def add,都要引用绑定的变量名(这里用的就是student这个类名)
print(xiaoming.name)
print(xiaoming.grades)
xiaoming.set_grade("数学",95)
xiaoming.set_grade("语文",99)
xiaoming.set_grade("英语",100)
print(xiaoming.grades)
xiaoming.print_grade()                   #原函数是打印函数，所以直接引用函数

