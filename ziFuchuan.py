# word = "字符串"
# sentence = "这是一个段落"
# paragraph = """
#     这是一个段落
#     可以由多行组成
# """
# print(word)
# print(sentence)
# print(paragraph)
# # \ 是强制转义字符
# # \t 往后缩进 制表符
# my_str = "Jason said \" I liked u \" "
# print(my_str)

# str = "chengdu"
# print(str)
# # 任意访问字符串中的一定规模的字符
# print(str[0:5])
# # 重复打印任意次数
# print(str[0:5]*10)

# 在下面数组中，输入元素的类型在数组中不会改变
namelist = ["xiaozhang", "xiaowang", "xiaoli", 1, "1"]
# print(namelist[0])
# print(namelist[1])
# print(namelist[2])
# print(type(namelist[3]))
# print(type(namelist[4]))
# # for打印所有数组中的元素
# for name in namelist:
#     print(name)
# # 使用while打印所有元素
# i = 0
# length = len(namelist)
# while i < length:
#     print(namelist[i])
#     i += 1

# 增加：[append]
print("——————————增加前列表——————————")
for name in namelist:
    print(name)

nametemp = input("输入一个增加学生的姓名")
namelist.append(nametemp)
print(namelist)
# 增加：[expend] 扩展数组，将新数组中的每一个元素加入原数组中
print("——————————增加前列表——————————")
for name in namelist:
    print(name)

nametemp = ["xiaoliu", "xiaoyu"]
namelist.extend(nametemp)
print(namelist)