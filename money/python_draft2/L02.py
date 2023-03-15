
def go(name, *param):
    print(len(param))
    print(param[0])
   

# 如果在定义函数时，*代表收集参数，**代表收集关键字参数。
def go2(**param):
    print(len(param))
    print(param)
    if "d" in param:
        print(param["d"])
    if "b" in param:
        print("b:%s" % param["b"])


go2(a=123, b=456, c=789)




