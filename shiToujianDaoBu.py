import random
player = int(input("请输入一个0到2的数字:"))
# rob = random.randint(0, 2)
rob = 1
while player == rob:
    print("平局！再来一次")
    # 这里写input(player)会再次显示player的赋值，但是可以赋给新值
    input("请输入一个0到2的数字:")
    if player - rob == 1:
        print("player获得胜利！")
    else:
        print("rob获得胜利！")
    break
