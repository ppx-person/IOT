

# Pin是“物理连接接口”(Physical Interface Connector)引脚

# 通过Shell调试窗口查询Pin类的的相关帮助信息from machine import Pin
# help(Pin)


'''
dengxz002
'''
from machine import Pin,Timer  # 导入GPIO脚和定时器
import time,utime,machine  # 导入时间模块

L_Red = Pin(27, Pin.OUT)  # 实例化27脚为输出模式

i = 0
def enter(t):  # 定义一个默认速度的函数
    global i
    i = i + 1
    print("enter:{}".format(i))
    L_Red.value(1)


Enter = Pin(14,Pin.IN,Pin.PULL_UP)  # 定义默认按钮，pin脚模式为输入，上拉

Enter.irq(trigger=Pin.IRQ_RISING, handler=enter)  # 默认按钮的中断，触发模式为上升沿中断，在中断触发时调用默认速度函数
print("begin")


# >>>>> 
'''
dengxz003
'''
from machine import Pin,Timer  # 导入GPIO脚和定时器
import time,utime,machine  # 导入时间模块

L_Red = Pin(27, Pin.OUT)  # 实例化27脚为输出模式
for attr in dir(Pin):
    print(attr)


Pin
__class__
__name__
value
__bases__
__dict__
DRIVE_0
DRIVE_1
DRIVE_2
DRIVE_3
IN
IRQ_FALLING
IRQ_RISING
OPEN_DRAIN
OUT
PULL_DOWN
PULL_UP
WAKE_HIGH
WAKE_LOW
init
irq
off
on

help(Pin) >>>
object <class 'Pin'> is of type type
  init -- <function>
  value -- <function>
  off -- <function>
  on -- <function>
  irq -- <function>
  IN -- 1
  OUT -- 3
  OPEN_DRAIN -- 7
  PULL_UP -- 2
  PULL_DOWN -- 1
  IRQ_RISING -- 1
  IRQ_FALLING -- 2
  WAKE_LOW -- 4
  WAKE_HIGH -- 5
  DRIVE_0 -- 0
  DRIVE_1 -- 1
  DRIVE_2 -- 2
  DRIVE_3 -- 3
MicroPython v1.19.1 on 2022-06-18; ESP32 module with ESP32
Type "help()" for more information.
>>> 
