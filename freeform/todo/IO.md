

# UART (RXD、TXD)
* Universal Asynchronous Receiver/Transmitter 通用异步收发传输器
一般是RS-232C规格
波特率

UART相连于产生兼容RS232规范信号的电路。
RS232标准定义逻辑"1"信号相对于地为-3到-15伏，而逻辑"0"相对于地为+3到+15伏。

Uart串口的RXD、TXD等一般直接与处理器芯片的引脚相连，而RS232串口的RXD、TXD等一般需要经过电平转换(通常由Max232等芯片进行电平转换)才能接到处理器芯片的引脚上，否则这么高的电压很可能会把芯片烧坏

uart是一种异步通信协议。而rs232只是物理层的电气接口要求。uart可以使用rs232物理层来进行通信。而rs232作为物理层也可以用其余不同于uart的协议来做通信。

UART是一种异步串行通信的方式，而RS-232是一种所对应的接口或者标准。
RS-232与常见的TTL电平不同，采用的是负逻辑，
因此我们一般会使用MAX-232转化芯片以匹配所需要的要求简单来说，
可以理解成，UART是异步串行通信的一中的方式，根据这种方式，我们实际中有RE-232这种工具来实现这种方式

TTL电平信号规定，+5V等价于逻辑“1”，0V等价于逻辑“0”(采用二进制来表示数据时)。
这样的数据通信及电平规定方式，被称做TTL（晶体管-晶体管逻辑电平）信号系统。
这是计算机处理器控制的设备内部各部分之间通信的标准技术。

TTL Transister-Transister-Logic

# SPI (片选)
* Serial Peripheral Interface串行外设接口
是一种高速的，全双工，同步的通信总线
SPI的通信原理很简单，它以主从方式工作

它们是MISO(主设备数据输入)、MOSI(主设备数据输出)、SCLK(时钟)、CS(片选)。
Master Input Slave Output,
Master Output Slave Input,


# I2C (寻址)
一种简单、双向二线制同步串行总线
它只需要两根线即可在连接于总线上的器件之间传送信息。
主器件用于启动总线传送数据，并产生时钟以开放传送的器件，此时任何被寻址的器件均被认为是从器件
SDA（串行数据线）和SCL（串行时钟线）都是双向I/O线






SCL : Serial Clock (often used for I2C)
So "SCLK" is "Serial CLocK".
RXD: receive external data
TXD: transmit external data






















































