
# pin = machine.Pin(0)
Pin.PULL_UP或None作为输入拉模式。默认为None，既无拉电阻。
通过pin.value()读取值


外部中断
```
def callback(p):
	print('pin change', p)

from machine import Pin
p0 = Pin(0, Pin.IN)
p0 = Pin(2, Pin.IN)

p0.irq(trigger=Pin.IRQ_FALLING, handler=callback)
p2.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, hander=callack)
```

PULL_UP输入上拉 PULL_DOWN输入下拉，上拉默认高电平，下拉默认低电平

上拉下拉是对于输入而言的，作用是当外部输入电平不确定的时候给定一个确定的电平。



