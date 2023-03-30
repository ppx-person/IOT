

#### emqx
https://www.emqx.io/


#### 端口如下

```
1883 MQTT 协议端口
8883 MQTT/SSL 端口
8083 MQTT/WebSocket 端口
8080 HTTP API 端口
18083 Dashboard 管理控制台端口
```
通过IP访问18083端口可以通过Dashboard在线观察EMQ的运行状态等参数
默认用户: admin，密码：public (可在平台中配置用户)



 

######
Download the EMQX repository
```
curl -s https://assets.emqx.com/scripts/install-emqx-rpm.sh | sudo bash
```

Install EMQX
```
sudo yum install emqx -y
```

Run EMQX
```
sudo systemctl start emqx
```


```
https://www.emqx.io/

http://193.112.101.68:18083/ 
admin deng8*****

```

#### 客户端
MQTT.fx

web工具
http://www.emqx.io/online-mqtt-client#/recent_connections/0?oper=create

* MQTT X CLI：在终端快速开发和调试 MQTT 服务与应用
https://mqttx.app/zh/docs/cli/get-started

mqttx pub -t 'hello' -h '193.112.101.68' -p 1883 -m 'from test001'

mqttx sub -t 'hello' -h '193.112.101.68' -p 1883 -v -q 1

mqttx pub -t 'hello' -h '193.112.101.68' -p 1883 -m 'from test001' -q 1


##### MQTT v5.0 版本的 Clean Start 与 Session Expiry Interval
>> 如果 CONNECT 报文中的 Clean Start 为 1，客户端和服务端必须丢弃任何已存在的会话，并开始一个新的会话。
>> 如果 CONNECT 报文中的 Clean Start 为 0 ，并且存在一个关联此客户端标识符的会话，
服务端必须基于此会话的状态恢复与客户端的通信。
如果不存在任何关联此客户端标识符的会话，服务端必须创建一个新的会话。

>> Session Expiry Interval 以秒为单位，如果 Session Expiry Interval 设置为 0 或者未指定，会话将在网络连接关闭时结束。
如果 Session Expiry Interval 为 0xFFFFFFFF ，则会话永不过期。
如果网络连接关闭时（DISCONNECT 报文中的 Session Expiry Interval 可以覆盖 CONNECT 报文中的设置） 
Session Expiry Interval 大于0，则客户端与服务端必须存储会话状态 。

####  Keep Alive 参数
在建立连接的时候，我们可以传递一个 Keep Alive 参数，它的单位为秒，
MQTT 协议中约定：在 1.5*Keep Alive 的时间间隔内，如果 Broker 没有收到来自 Client 的任何数据包，
那么 Broker 认为它和 Client 之间的连接已经断开；
同样地, 如果 Client 没有收到来自 Broker 的任何数据包，
那么 Client 认为它和 Broker 之间的连接已经断开。



uptime n.(计算机等的)运行时间;


http://193.112.101.68:18083/

API文档 
http://193.112.101.68:18083/api-docs/index.html 


Install/launch the plugin
```
./bin/emqx_ctl plugins install {pluginName}
```


while 1:
	#micropython.mem_info()
	c.wait_msg()
finally:
	c.disconnect()复制代码

def sub_cb(topic, msg):

c = MQTTClient(CLIENT_ID, server,6002,username,password)
# Subscribed messages will be delivered to this callback
c.set_callback(sub_cb)

