
# lambda函数也称匿名函数
# lambda argument_list:expersion
# a,b, *args, a,b=1,*args
# a+b sum(a) 1 if a > 10 else 0
# [i for i in range(10)]


print("begin...")
a = 5
b = 'yes' if a > 10 else 'no'
print(b)

array = [i for i in range(1, 10, 2)]
print(array)

# lambda函数没有返回值
b = lambda x: "Even" if x%2==0 else "Odd"
print(b(9))


# 高阶函数：一个函数的函数名作为参数传给另外一个函数 map filter
arr = [2,4,6,8] 
arr = list(map(lambda x: x*x, arr)) 
print(arr)
# ** 幂运算 例如“2**3”可表示2的三次方，结果为8。








