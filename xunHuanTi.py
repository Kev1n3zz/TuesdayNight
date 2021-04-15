# 用来熟悉循环体结构
# 遍历str
name = "liujiujiu"
for x in name:
    print(x, end="\t")
# 读取列表
a = ["a", "b", "c", "d"]
for i in range(len(a)):
    print(i, a[i])
# 计数器
n = 100
sum = 0
couter = 1
while couter <= n:
    sum = sum +couter
    couter += 1

print("计数结果为：", sum)
