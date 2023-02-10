
不同安装方式得到的 EMQX 其目录结构会有所不同，具体如下:

描述	使用 ZIP 压缩包安装	使用二进制包安装
配置文件目录	./etc	/etc/emqx/etc
数据文件	./data	/var/lib/emqx/data
日志文件	./log	/var/log/emqx
启动相关的脚本	./releases	/usr/lib/emqx/releases
可执行文件目录	./bin	/usr/lib/emqx/bin
Erlang 代码	./lib	/usr/lib/emqx/lib
Erlang 虚拟机文件	./erts-*	/usr/lib/emqx/erts-*
插件	./plugins	/usr/lib/emqx/plugins
