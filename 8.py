# with open("./data.txt","r",encoding="UTF-8") as f:   #读取模式
            #  line=f.read(10)      #读文件的第一种方法--调用read方法
            #  print(line)          #line只是一个储存了第一次结果的变量
            #  print(line)          #想让他继续往下读必须要用 方法（f.read()）
            #  print(f.read(20))
            #  print(f.read(20))



            # 读文件第二种方法--readline
    # line = f.readline()
   # print(f.readline())
   # print(f.readline())     #会自动读取每一行，并记录读到哪一行
   #  while  line !="":
   #      print(line)
   #      line = f.readline()



            # 读文件第三种方法--readlines
            # print(f.readlines())
            # lines = f.readlines()
            # for line in lines:
            #     print(line)
# with open("./unknown.txt","w",encoding="UTF-8") as f:      #写入模式
#      f.write("Hello\n")            #写入会把原来的文件给清空，重新开始写入
#      f.write("World!\n")
#
#
# #附加模式（不改变原基础上只能添加到末尾）
# with open("./data.txt","a",encoding="UTF-8") as f:
#     f.write("Hello\n")
#     f.write("World!\n")
 #r+可读可写
with open("./data.txt","r+",encoding="UTF-8") as f:

    print(f.read())

    f.write("11")
    f.seek(0)         #seek能把指针调回开头，所以三者位置不同导致的写入结果的位置也不同
    #写放在读后面，指针会指到末尾，所以会才末尾不断写入(会不断写入)
        #写放在读前面，指针会指到开头，会覆盖掉前面的内容(只会重复覆盖，不会继续写入)

    #每次先读，指针就会到末尾，如果调零就是写到开头，不调零就是写到末尾
    #还有就是如果是写入放第一位，那么指针是默认在开头的（r+模式默认的）
