# RabbitMQ配置使用SSL加密通信

作者：蒙宇明

日期：2019-12-6

## 测试环境

- ubuntu  16.04
- rabbitmq-server  3.5.7
- openssl  1.0.2g

## 大致步骤

### server端配置

1. 安装openssl
2. 生成证书文件夹（ssl）并拷贝到rabbitmq安装目录下
3. 配置rabbitmq.conf文件
4. server开放5671端口（入方向）
5. 增加rabbitmq新用户
6. 重启rabbitmq服务

### client端配置

1. 将server生成的证书文件夹ssl保存到本地
2. 源码中进行相应配置即可

## 实际操作步骤

## 安装openssl

```bash
sudo apt-get install openssl
```

## 生成证书

从网络获取生成证书工具:

```bash
git clone https://github.com/Berico-Technologies/CMF-AMQP-Configuration.git && cd CMF-AMQP-Configuration/ssl
```

生成证书文件:

```bash
sh setup_ca.sh {your-ca-file-name}
sh make_server_cert.sh {your-hostname} {passwd}
sh create_client_cert.sh {your-client-name} {passwd}
```

完成后会在当前目录生成 `ca` `server` `client`  文件夹, 里面是各自的证书文件;

##  服务端配置

服务端需要上面生成的 `ca` 和 `server` 文件夹, 拷贝到`/etc/rabbitmq/ssl` 目录下, 如果此目录不存在就手动创建.

`cp -a ssl /etc/rabbitmq/`

修改 `/etc/rabbitmq/rabbitmq.config` 文件, 添加以下内容, 注意替换其中的 `{your-hostname}`,  如果此文件不存在则直接创建:

```config
[
  {ssl, [{versions, ['tlsv1.2', 'tlsv1.1']}]},
  {rabbit, [
    {tcp_listeners, [5672]},
    {ssl_listeners, [5671]},
    {ssl_options, [
      {cacertfile,"/etc/rabbitmq/ssl/ca/cacert.pem"},
      {certfile,"/etc/rabbitmq/ssl/server/{your-hostname}.cert.pem"},
      {keyfile,"/etc/rabbitmq/ssl/server/{your-hostname}.key.pem"},
      {verify, verify_peer},
      {fail_if_no_peer_cert, true},
      {versions, ['tlsv1.2', 'tlsv1.1']}
    ]}
  ]}
].
```

重启rabbitmq-server:

```bash
sudo rabbitmqctl stop
sudo rabbitmq-server -detached
```

网页控制台出现  `amqp/ssl 	:: 	5671`  字样说明配置成功.

## 测试

### 使用openssl库提供的测试程序进行ssl回路测试

替换以下命令中  `/path/to/server/{hostname}.cert.pem` 路径.
替换以下命令中  `/path/to/client/{clientname}.cert.pem` 路径.
替换以下命令中  `/path/to/ca/cacert.pem` 路径.

启动服务端:

```bash
sudo openssl s_server -cert /path/to/server/{hostname}.cert.pem -key /path/to/server/{hostname}.key.pem -CAfile /path/to/ca/cacert.pem
```

客户端连接服务端:

```bash
sudo openssl s_client -cert /path/to/client/{clientname}.cert.pem -key /path/to/client/{clientname}.key.pem -CAfile /path/to/ca/cacert.pem
```

此时应该可以在服务端和客户端之间收发消息.

### 使用openssl库提供的测试程序连接到rabbitmq-server

替换以下命令中  `/path/to/client/{clientname}.cert.pem` 路径.
替换以下命令中  `/path/to/ca/cacert.pem` 路径.

客户端连接服务端:

```bash
sudo openssl s_client -connect localhost:5671 -cert /path/to/client/{clientname}.cert.pem -key /path/to/client/{clientname}.key.pem -CAfile /path/to/ca/cacert.pem
```

目前测试连接后一会自动断开, 猜测应该是没有使用rabbitmq库, 服务端自动断开.

### C++程序连接到rabbitmq-server

使用AMQP-CPP库, 需要作出部分修改, 主要是添加了读取证书调用:

修改 `src/linux_tcp/openssl.cpp` 文件, 添加以下内容:
```cpp
int SSL_CTX_load_verify_locations(SSL_CTX *ctx, const char *cafile, const char *capath) {
    // create a function
    static Function<decltype(::SSL_CTX_load_verify_locations)> func(handle, "SSL_CTX_load_verify_locations");
    
    // call the openssl function
    return func(ctx, cafile, capath);
}

int SSL_CTX_use_certificate_file(SSL_CTX *ctx, const char *file, int type) {                                                                        
   // create a function
   static Function<decltype(::SSL_CTX_use_certificate_file)> func(handle, "SSL_CTX_use_certificate_file");
   
   // call the openssl function
   return func(ctx, file, type);
}

int SSL_CTX_use_PrivateKey_file(SSL_CTX *ctx, const char *file, int type) {
   // create a function
   static Function<decltype(::SSL_CTX_use_PrivateKey_file)> func(handle, "SSL_CTX_use_PrivateKey_file");
   
   // call the openssl function
   return func(ctx, file, type);
}
```

修改 `src/linux_tcp/openssl.h` 文件, 添加函数声明:

```cpp
int SSL_CTX_load_verify_locations(SSL_CTX *ctx, const char *cafile, const char *capath);
int SSL_CTX_use_certificate_file(SSL_CTX *ctx, const char *file, int type);
int SSL_CTX_use_PrivateKey_file(SSL_CTX *ctx, const char *file, int type);
```

修改 `src/linux_tcp/sslcontext.h` 文件, 在构造函数中添加以下内容, 注意替换证书路径:

```cpp
OpenSSL::SSL_CTX_load_verify_locations(_ctx, "/path/to/ssl/ca/cacert.pem", nullptr);
OpenSSL::SSL_CTX_use_certificate_file(_ctx, "/path/to/client/{clientname}.cert.pem", SSL_FILETYPE_PEM);
OpenSSL::SSL_CTX_use_PrivateKey_file(_ctx, "/path/to/client/{clientname}.key.pem", SSL_FILETYPE_PEM);
```

测试程序使用 `examples/libev.cpp`, 修改以下部分使用ssl安全连接:

```cpp
  // AMQP::Address address("amqp://guest:guest@localhost/");
  AMQP::Address address("amqps://guest:guest@localhost/");
```

编译:

```bash
mkdir build && cd build
cmake ../ -DAMQP-CPP_BUILD_EXAMPLES=ON -DAMQP-CPP_LINUX_TCP=ON
make
```
如果缺少`libev` `libuv` `libevent`库, 使用以下命令安装:

```bash
 sudo apt-get install libev4 libuv1-dev libevent-2.0-5
```

运行:

```bash
./examples/amqpcpp_libev_example
```

此时应该正确连接到rabbitmq-server.

### Python程序连接到rabbitmq-server

示例代码 `rmq_sender.py`:

```python
# 适用于 pika 1.1
import logging
import pika
import ssl

# 请替换所有证书路径
ca_certfile = "/etc/rabbitmq/ssl/ca/cacert.pem"
certfile = "/etc/rabbitmq/ssl/client/rabbitmq_client.cert.pem"
private_key = "/etc/rabbitmq/ssl/client/rabbitmq_client.key.pem"
# 服务器信息
hostname = "192.168.3.122"
port = 5671

# logging.basicConfig(level=logging.INFO)

context = ssl.create_default_context(cafile=ca_certfile)
context.load_cert_chain(certfile, private_key)
ssl_options = pika.SSLOptions(context, hostname)
conn_params = pika.ConnectionParameters(port=port, ssl_options=ssl_options)

with pika.BlockingConnection(conn_params) as conn:
    ch = conn.channel()
    ch.queue_declare("ssl_test")
    ch.basic_publish("", "ssl_test", "Hello, world!")
    input("Please enter any key to exit!!!\n")
#    print(ch.basic_get("ssl_test"))
    conn.close()
```
```python
# 适用于 pika 0.12
import logging
import pika
import ssl

# 使用 guest 用户无法远程登录
creds = pika.PlainCredentials("admin", "123456");
conn_params = pika.ConnectionParameters(host = "192.168.3.122",
                                        port = 5671,
                                        ssl = True,
                                        credentials = creds,
                                        ssl_options = dict(
                                            ca_certs="/etc/rabbitmq/ssl/ca/cacert.pem",
                                            certfile="/etc/rabbitmq/ssl/client/rabbitmq_client.cert.pem",
                                            keyfile="/etc/rabbitmq/ssl/client/rabbitmq_client.key.pem",
                                            cert_reqs=ssl.CERT_REQUIRED))

with pika.BlockingConnection(conn_params) as conn:
   ch = conn.channel()
   ch.queue_declare("ssl_test")
   ch.basic_publish("", "ssl_test", "Hello, pika!!!")
   input("Please enter any key to exit!!!\n")
   # print(ch.basic_get("ssl_test"))
   conn.close()

```



运行:

```bash
python3 ./rmq_sender.py
```
此时应该正确连接到rabbitmq-server.



### 增加一个RabbitMQ用户

```bash
sudo rabbitmqctl add_user admin 123456
sudo rabbitmqctl set_user_tags admin administrator
sudo rabbitmqctl set_permissions -p '/' admin '.' '.' '.'
sudo service rabbitmq-server restart
```

## FAQ

### server端增加用户或者重启rmq服务失败

可能的原因：配置rabbitmq.conf文件出了错，大概率是由于逗号引起的json格式非法。

解决方案：重点检查一下json文件的完整性（多少一个逗号都会出错）

### 启动后SSL连接被拒绝

可能的原因：server的端口没有开启（入方向） 

解决方案：防火墙打开5671端口即可

## 引用

[RabbitMQ SSL设置](https://blog.csdn.net/Vstars/article/details/84733995)
[rabbitmq ssl/tls及pika tls认证连接方法](https://blog.csdn.net/comprel/article/details/94663170)
[SSL编程指南](https://blog.csdn.net/rzytc/article/details/50647095)

