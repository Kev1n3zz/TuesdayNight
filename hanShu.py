# 带参数的函数
def add2num(a, b):
    c = a+b
    return a+b  #  通过return返回运算结果

print(add2num(1, 2))

def divid(a, b):
    shang = a//b
    yushu = a%b
    return shang,yushu
shang,yu = divid(2,1)  #需要使用多个值来保存内容，多个返回值用逗号分隔

print("shang:%d,yu:%d"% (shang, yu))
