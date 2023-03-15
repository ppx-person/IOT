
# 替换元素 names[1] = '小强'
# 插入元素
"""
names = ['a', 'b', 'c']
names.insert(1, '小强')
print(names)

print("---begin---")
chars= ['a', 'b', 'c', 'b', 'k']
print(chars)
# 只会删除第一
chars.remove('b')
print(chars)
"""
obj = {
    "k": "OK"
}
list = ['a', 'b', 'c', obj]
list.append(80)
print(list)
# 多个元素相加是使用+或extend(list)方法
list2 = ['a2', 'b2', 'c2']
list += list2
print(list)

# 列表
list_one = []
list_two = ['p', 'y']
list_three = [1, 'a', '&', 2.3]
# 使用list()函数创建列表
# 接收的参数必须是一个可迭代类型的数据

# list_one = list(1)报错
# = list('python') 或 list[1, 'python'])















