
import traceback

msg = "OK"
print(f">>>{msg}")

# P100
try:
    r = 1 / 0;
except ZeroDivisionError as e:
    print(f"error:{e}")
    print("error\n{}".format(traceback.format_exc(limit=3)))

# 多个异常 except (NameError, IndexError) as e
# Exception
# finally:


# >>> 主动抛出异常
# 1.raise 异常类名 raise NameError
# 2.raise 异常对象 
# name_error=NameError()
# raise name_error

# 自定义异常
class CustomError(Exception):
    pass

try:
    pass
    raise CustomError('出现错误')
except CustomError as e:
    print(e)

# pass 空语句 do nothing





















