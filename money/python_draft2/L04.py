
# 元组tuple是一种不可变序列类型，元组中的元素是不允许修改的
tuple_one = ()
tuple_two = ('t', 'u', 'p')
tuple_three = (0, 'p', '&')

# 元组拆包 对应的赋值给不同变量
# return多个对象，默认就是以tuple形式返回
val = (10, 20)
a, b = val
# print(a)

# 集合 set, 分可变集合和不可变集合
# set([iterable])
# frozenset([iterable])


my_set = set(["abc", "efg", "abc"])
# 是否存在用in
print(dir(my_set))
print("abc" in my_set)

my_set.add("sss")




























