> ## 博客导航
>
> 第一部分: 选购服务器
> 第二部分: 在本地安装远程连接服务器软件
> 第三部分: 在服务器安装软件
> 第四部分: 部署应用

> ## 一、选购服务器
>
> 此篇博客采用阿里服务器，学生价位更优惠（不满24岁自动为学生身份，已满24岁可认证学生身份）
>
> #### 购买地址
>
> - 阿里云学生优惠服务器(**推荐**) <https://promotion.aliyun.com/ntms/act/campus2018.html?accounttraceid=b580e226-1c85-492e-a500-21116affda2e&userCode=agtj8gav>
> - 百度云学生优惠服务器 <https://cloud.baidu.com/campaign/campus-2018/index.html?unifrom=eventpage>
>
> #### 购买流程（阿里云）
>
> 参考阿里云

> ## 二、安装所需软件
>
> #### 软件下载
>
> [WinSCP、PuTTY](https://pan.baidu.com/s/1neKfqqmZOt-WqqstT79_dw)下载, 提取码：nn5j
>
> #### 软件使用
>
> 稍后提供

> ## 三、在服务器安装软件
>
> ### 1、下载nginx
>
> #### Nginx概述
>
> Nginx是一款轻量级的HTTP服务器，采用事件驱动和异步非阻塞处理方式框架，这让其具有极好的IO性能，市场用于服务端的反向代理和负载均衡
>
> #### Nginx优点
>
> - 高并发连接：官方测试Nginx能够支撑5万并发连接，实际生产环境中更可以支撑2~4万并发连接数。
> - 内存消耗少：在主流的服务器中Nginx目前是内存消耗最小
> - 免费使用可以商业化：开源
> - 配置文件简单：网络和程序配置通俗易懂
>
> #### Ubuntu下载
>
> 详情参见[nginx官网](http://nginx.org/en/linux_packages.html#stable)
>
> #### 下载步骤
>
> **第一步**：更新下载源，请将以下内容追加到/etc/apt/sources.list文件的末尾
>
> ```
> deb http://nginx.org/packages/ubuntu/ 【codename】 nginx
> deb-src http://nginx.org/packages/ubuntu/ 【codename】 nginx
> ```
>
> 【codename】替换为Ubuntu版本参见下表
>
> | Version | codename | Supported Platforms                  |
> | ------- | -------- | ------------------------------------ |
> | 16.04   | xenial   | x86_64, i386, ppc64el, aarch64/arm64 |
> | 17.10   | artful   | x86_64, i386                         |
> | 18.04   | bionic   | x86_64                               |
>
> **第二步**：更新源
>
> ```
> apt-get update
> ```
>
> **第三步**：下载所需密钥，在/etc/apt目录下
>
> ```
> wget http://nginx.org/keys/nginx_signing.key 
> sudo apt-key add nginx_signing.key
> ```
>
> **第四步**：下载nginx命令
>
> ```
> sudo apt-get install nginx #下载 nginx
> ```
>
> ```
> # nginx其他命令
> sudo apt-get remove nginx nginx-common 
> # 卸载删除除了配置文件以外的所有文件。
> sudo apt-get purge nginx nginx-common 
> # 卸载所有东东，包括删除配置文件。
> sudo apt-get autoremove 
> # 在上面命令结束后执行，主要是卸载删除Nginx的不再被使用的依赖包。
> sudo apt-get remove nginx-full nginx-common 
> # 卸载删除两个主要的包。
> nginx -V 
> # 查看版本 1.14稳定版
> nginx 
> # 运行
> killall nginx 
> # 终止运行
> ```
>
> **第五步**：运行nginx此时浏览器打开 服务器公网ip 可以看到nginx欢迎页面

> ### 2、下载uwsgi
>
> #### uwsgi概述
>
> #### web服务器和web框架
>
> web服务器是用来接收客户端请求，建立连接，转发响应的程序 web框架是处理业务逻辑 举例： web服务器：nginx web框架：flask
>
> #### uWSGI和WSGI
>
> WSGI：通信协议 uWSGI：属于WSGI协议的web服务器（nginx、nginx都是web服务器）
>
> #### 为什么需要nginx+uWSGI
>
> 利用nginx可以实现反向代理的能力，可以实现分布式服务器功能可以解决网络访问量过大的问题。
>
> #### 安装步骤
>
> **第一步**：安装 pip 一般默认Ubuntu服务器自带python3.5但是却没有自带pip
>
> ```
> sudo apt-get install python3-pip
> ```
>
> **第二步**：安装 uwsgi
>
> ```
> pip3 install uwsgi
> ```
>
> Django自带wsgi为什么不直接使用，Django自带wsgi只是为了开发使用的是单进程的，不适合上线使用。

> ## 四、部署应用
>
> **第一步**：将项目上传
> （1）在/home/目录下 新建 /horns/ 目录
> （2）将文件上传至 /home/horns中
> **第二步**：运行文件，准备运行环境
> （1）下载项目依赖python包
> （2）安装mysql数据库

> ```
> sudo apt-get install mysql-server
> # 期间设置数据库密码
> sudo apt-get install
> # 数据库常用命令
> mysql -u root -p  
> # 登录数据库
> show databases; 
> # 查看数据库
> CREATE DATABASE db_name DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci; 
> # 创建数据库
> quit; 
> # 退出数据库
> ```
>
> 执行迁移
>
> ```
> python manage.py migrate
> ```
>
> （3）设置端口，以便让所有用户访问
>
> ```
> # settings.py
> ALLOWED_HOSTS = ['*']
> ```
>
> （4）运行项目
>
> ```
> python3 manage.py runserver 0.0.0.0:8080
> ```
>
> 8080端口需在阿里云轻量应用服务器控制台中防火墙添加规则
> 访问项目 39.108.113.110:8080
> **第三步**：通过uwsgi服务器运行项目
> （1）在项目根目录（manage.py同目录）下创建 uwsgi.ini 文件，详情访问 [uwsgi官网](https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html)
> 编辑内容
>
> ```
> [uwsgi]
> # socket = 127.0.0.1:8080
> http = :8080
> chdir = /home/horns/myproject/
> wsgi-file = myproject/wsgi.py
> processes = 4
> threads = 2
> stats = 127.0.0.1:9191
> ```
>
> 通过uwsgi服务运行项目
>
> ```
> uwsgi uwsgi.ini
> uwsgi -d --ini uwsgi.ini 
> # 后台运行
> ```
>
> **第四步**：通过nginx+uwsgi运行项目

> （1）在etc/nginx/conf.d/default.conf 配置nginx 将其中如下代码注释
>
> ```
> # location / {
> #    root   /usr/share/nginx/html;
> #    index  index.html index.htm;
> # }
> ```
>
> 替换为
>
> ```
> location / {
>     include uwsgi_params;
>     uwsgi_pass 127.0.0.1:8080;
> }
> ```
>
> （2）[settings.py](http://settings.py/)
>
> ```
> DEBUG = FALSE
> ```
>
> （3）[url.py](http://url.py/)
>
> ```
> + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
> ```
>
> （4）设置静态文件
>
> - 此时服务器路由统一由nginx管理，所以我们需要进行配置nginx，etc/nginx/conf.d/default.conf
>
> ```
> location  /static {
>    autoindex on;
>    alias  /home/horns/<项目根目录>/static;
> }
> ```
>
> - 将项目中的文件统一管理
>   1、在项目settion.py中设置STATIC_ROOT静态文件根目录
>
> ```
> STATIC_ROOT = os.path.join(BASE_DIR,'static')
> ```
>
> 2、在项目根目录创建 static 3、执行命令
>
> ```
> python3 manage.py collectstatic
> # 将静态文件收集到STATIC_ROOT
> ```
>
> （5）重启nginx
>
> ```
> killall nginx
> nginx
> ```