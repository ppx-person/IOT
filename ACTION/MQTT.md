

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
web工具
http://www.emqx.io/online-mqtt-client#/recent_connections/0?oper=create

* MQTT X CLI：在终端快速开发和调试 MQTT 服务与应用
https://mqttx.app/zh/docs/cli/get-started

mqttx pub -t 'hello' -h '193.112.101.68' -p 1883 -m 'from test001'

mqttx sub -t 'hello' -h '193.112.101.68' -p 1883 -v -q 1

mqttx pub -t 'hello' -h '193.112.101.68' -p 1883 -m 'from test001' -q 1




