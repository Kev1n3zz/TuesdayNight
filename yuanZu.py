# Tuple（元组）
# tuple与list相似，但是tuple的元素不能修改。
# tuple中的元素可以使用变量作为元素

# 创建空的元组
tup1 = ()
print(type(tup1))

tup2 = (50)
print(type(tup2))

tup3 = (50, )
print(type(tup3))

tup4 = ("a", "b", "c", "d", "e")
print(tup4[0])
print(tup4[-2]) #  从尾部开始访问
print(tup4[1:5]) #  依旧是左闭又开

# 增

# 删 del会删除整个元组变量

# 改
# tup4[1] = 100 报错则无法直接修改元素
tup = tup4 + tup3
print(tup)
# 这里是在内存中新建了一个tup元组将tup4和tup3的内容放置进去了

# 查