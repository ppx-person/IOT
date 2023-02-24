

* http://www.86x.org/en/latet/esp32/quickref.html
* https://wokwi.com/projects/342366199858856532 流水

# 通用板控制
MicroPython REPL位于UART0（GPIO1=TX，GPIO3=RX）上，波特率115200。制表符完成有助于了解对象的方法。
粘贴模式（ctrl-E）用于将一大块Python代码粘贴到REPL中。


```
import machine
machine.freq()
machine.freq(240000000)
```


```
import esp
esp.osdebug(None) # turn off verdor O/S debugging messages
esp.osdebug(0) # redirect vendor O/S debugging messages to UART(0)

# low level methods to interact with flash storage
esp.flash_size()
esp.flash_user_start()
esp.flash_erase(sector_no)
esp.flash_write(byte_offset, buffer)
esp.flash_read(byte_offset, buffer)



```



```
import esp
print("begin >>>")
b = bytearray("中国", 'utf-8')
print(esp.flash_write(2097152, b))
read_b = bytearray(7)
esp.flash_read(2097152, read_b)
str = read_b.decode('gbk')
print(str)
print("end <<<")
```

# pass 
空语句 do nothing
保证语义的完整
```
while not wlan.isconnected():
	pass
# 可通过wlan.config(reconnects=n)来更改次数 0不重试 -1永久重新连接(默认)
```

```
import time
time.sleep(1)
time.sleep_ms(500)
time.sleep_us(10)
start = time.ticks_ms()
delta = time.ticks_diff(time.ticks_ms(), start)
```

# Timer
ESP32端口有四个硬件计时器。使用计时器ID从0到3（含）的machine.Timer 类
```
from machine import Timer

tim0 = Timer(0)
tim0.init(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print(0))

tim1 = Timer(1)
tim1.init(period=2000, mode=Timer.PERIODIC, callback=lambda t:print(1))

```


# baudrate 波特率
polarity