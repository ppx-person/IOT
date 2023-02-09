
##### MQTT 遗嘱消息（Will Message）

遗嘱消息是 MQTT 为那些可能出现 意外断线 的设备提供的将 遗嘱 优雅地发送给第三方的能力
Will Retain 的使用场景，它是保留消息与遗嘱消息的结合。
如果订阅该遗嘱主题（Will Topic）的客户端不能保证遗嘱消息发布时在线，
那么建议为遗嘱消息设置 Will Retain，避免订阅端错过遗嘱消息



#### QoS(Quality of Service)
* QoS0 发送就不管了，最多一次;
* QoS1 发送之后依赖MQTT规范，是否启动重传消息，所以至少一次；
* QoS2 发送之后依赖MQTT消息机制，确保只有一次。

#### 
QoS 是消息的发送方（Sender）和接受方（Receiver）之间达成的一个协议：（MQTT不是端到端的通信）
QoS1, 发送后收到PUBACK才停止，Recieiver有可能会收到重复的消息


##### Retained消息
* 一个 Topic 只能有 1 条 Retained 消息，发布新的 Retained 消息将覆盖老的 Retained 消息；
* 如果订阅者使用通配符订阅主题，它会收到所有匹配的主题上的 Retained 消息；
* 只有新的订阅者才会收到 Retained 消息，如果订阅者重复订阅一个主题，也会被当做新的订阅者，然后收到 Retained 消息；
* Retained 消息发送到订阅者时，消息的 Retain 标识仍然是 1，订阅者可以判断这个消息是否是 Retained 消息，以做相应的处理。

如果你想删除一个 Retained 消息也很简单，只要向这个主题发布一个 Payload 长度为 0 的 Retained 消息就可以了。

LWT(最后遗嘱)
Last Will and Testament
当 Broker 检测到 Client 非正常地断开连接的时候，就会向遗嘱主题里面发布一条消息。
遗嘱相关的设置是在建立连接的时候，在 CONNECT 数据包里面的 Variable header(可变头与) Payload(有效载荷) 中 指定的

根据遗嘱的属性和触发机制，我们不难看出，遗嘱常用于获取设备的连接状态。


* 文档入口
https://www.emqx.io/docs/en/v5.0/messaging/explore-mqtt.html#will-message
左边菜单-Messaging-Explore MQTT-Will message

1. Initiate a connection request with one client, set the topic to t/1 and payload to A will message from MQTTX CLI:
```
mqttx conn -h '193.112.101.68' -p 1883 --will-topic 't/1' --will-message 'A will message from MQTTX CLI'
```
2. Subscribe to topic t/1 with another client for receiving the will messages:
```
mqttx sub -t 't/1' -h '193.112.101.68' -p 1883 -v
```
3. Disconnect the client specified in Step 1, then the client specified in Step 2 will receive the will message:
```
topic:  t/1
payload:  A will message from MQTTX CLI
```

#### cleansession清除会话
服务器必须在客户端断开之后继续存储/保持客户端有订阅状态
 * 存储订阅的消息Qos1和Qos2消息，当客户端重新订阅时发送
 * 服务端正在发送消息给客户端期间连接丢失导致发送失败的消息
#### retain持久消息
#### will遗愿消息


#### share subscription共享订阅

https://blog.csdn.net/zhetmdoubeizhanyong/article/details/104871483

假设 4 个订阅者订阅了同一个主题，都会收到,
现在假如只想每条消息有一个订阅者处理即可，那么使用共享订阅就可以了

* 共享订阅针对场景应是数据的生产者远超出数据消费者数量
共享订阅针对场景应是数据的生产者远超出数据消费者数量，而且同一条数据(消息)只需要被任意其中一个消费者处理一次。
主要是实现消费者数量处理消息的均衡负载。

两种方式
主题前缀$queue/:topic, 实例sub $queue/up/data
主题前缀$share/:group/:topic 实例sub $share/group/up/data

共享订阅由三部分组成：
* 静态共享标识符 （$queue 与 $share）
* 组标识符（可选）
* 实际接收消息的主题

$queue 之后的主题中所有消息将轮流发送到客户端
$share 之后，您可以添加不同的组，例如:
* $share/group_1/topic
* $share/group_2/topic
* $share/group_3/topic
当broker 向 topic 发送消息时，每个组都会收到该消息，并将该消息随机发送给本组中的一个设备



#### What is off-line message?
Usually an MQTT client receives messages only when it is connected to an EMQX broker, 
and it will not receive messages if it is off-line. 
But if a client has a fixed ClientID, and it connects to the broker with clean_session = false, 
the broker will store particular messages for it when it is off-line. 
If the Pub/Sub is done at certain QoS level (broker configuration), 
these messages will be delivered when this client is reconnected.
Off-line messages are useful when the connection is not stable, or the application has special requirements on QoS.
