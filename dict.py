# # python中的(map)字典是无序的对象合集 可以称为map或者dict
# # 键-值的存储,一一对应
#
# # 字典的定义
# info = {"name": "吴彦祖", "age": "18"}
#
# # 直接访问dict中没有的键可能会报错
# print(info["name"], info["age"])
#
# # get访问不会报错,会返回null
# print(info.get("name"))
#
# # 增
# newID = input("请输入一个学号")
# info["id"] = newID
# print(info["id"])
#
# # 删
# # del info["name"] #  删除dict是整个变量在内存中都删除了
# # print(info["name"])  #  会整个name键-值对后都删掉
# # [clear]清空键-值对
# # info.clear()
#
# # 改
# # info["age"] = 20
# # print(info["age"])
#
# # 查 每个键-值对是一个元组
# # print(info.keys())  #  拿到所有的键
# # print(info.values())  #  拿到所有的值
# # print(info.items())  #  拿到所有的项
#
# # 遍历所有的值
# for key in info.keys():
#     print(key)
# for key, value in info.items():
#     print("keys=%s,value=%s" % (key, value))
#

# 拿到列表中的下标和元素内容
mylist = ["a", "b", "c", "d", "e"]
for i, x in enumerate(mylist):
    # print(type(i))
    # print(type(x))
    print( "下标是：%d,对应的元素为：%s" % (i, x))
    # print("对应的元素为：%s" % x)

# set集合 两个set可以做集合的一些操作
s = set([1, 2, 3])
print(s)