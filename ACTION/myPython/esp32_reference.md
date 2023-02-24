

* http://www.86x.org/en/latet/esp32/quickref.html

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