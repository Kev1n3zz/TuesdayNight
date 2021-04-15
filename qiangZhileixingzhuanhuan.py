password = input("please enter your password:")
print("your password is:", password)

# 测试一个变量的类型
# 这里的输出是一个str
# 强制类型转化问题
# a = int(password)
if type(password) == int:
    print("haha")
else:
    print("try again!", '\n'"the password should be int")

