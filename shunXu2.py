import random
# 四间空办公室
offices = [[], [], [], []]
# 五位老师
names = ["a", "b", "c", "d", "e"]

for name in names:
    index = random.randint(0, 3)
    # 随机给数组中的元素一个下标，范围为办公室的编号
    offices[index].append(name)

i = 1
for office in offices:
    print("办公室%d的人数：%d" % (i, len(office)))
    i += 1
    for name in office:
        print("%s" % name, end="\t")
    print("\n")
    print("-"*20)
