# d浏览器作用：

- 呈现内容       解析内容和样式（解析html和css）     -webkit-   
- 实现交互逻辑    JavaScript引擎   v8引擎  解析js
- 进行数据传送的     Chrome net 引擎  用来上网
- 360  兼容模式(ie)  急速模式(谷歌)
- 应用，软件，APP基于两种：1.c/s架构 必须有客户端服务，更新不及时，使用比较流畅。比如QQ和微信 2.b/s 浏览器   比如淘宝，天猫，手机上的淘宝属于混合型开发。可以随时访问最新的内容，不需要用户去下载，但是有延迟，不能够流畅的去操作，体验性不好，ajax (async javascript and xml)
- 服务器：广义：指提供一切服务的。狭义：具体提供服务的
- 通过from  import  引用的内容只能执行一次。是为了提高运行效率。
- 应用逻辑放在服务器上：优点：业务逻辑清晰，工作量少，首页加载速度快；缺点：用户体验差，服务器压力大，不利于协同工作
- 应用逻辑放在客户端（ajax）上：优点：用户的体验比较流畅，减轻服务器的压力，有利于协同工作。缺点：首页加载速度慢，业务逻辑不清晰，工作量比较大。
- mvc(model view controller)->mvvm (model->模型->数据     view->视图->模板->html+css     数据到视图    视图到数据   双向数据的绑定)    代表：angular  vue  

# linux:

> linux是指一种操作系统，也可指操作系统的内核。Ubuntu是最受欢迎的发行版(永久免费，开源分享，定期更新和发布，六个月发布一个版本)。还有CentOS，redcat,Fedora等版本。是多用户多任务的支持远程操作的系统。



## linux命令：

### 文件和目录：

```linux
/              根目录
├── bin     存放用户二进制文件
├── boot    存放内核引导配置文件
├── dev     存放设备文件
├── etc     存放系统配置文件
├── home    用户主目录
├── lib     动态共享库
├── lost+found  文件系统恢复时的恢复文件
├── media   可卸载存储介质挂载点
├── mnt     文件系统临时挂载点
├── opt     附加的应用程序包
├── proc    系统内存的映射目录，提供内核与进程信息
├── root    root 超级管理员权限，用户主目录
├── sbin    存放系统二进制文件
├── srv     存放服务相关数据
├── sys     sys 虚拟文件系统挂载
|── tmp     存放临时文件
├── usr     存放用户应用程序
└── var     存放邮件、系统日志等变化文件
    run     运行的时候产生的临时文件
白色：表示普通文件
蓝色：表示目录
绿色：表示可执行文件
红色：表示压缩文件
浅蓝色：链接文件
红色闪烁：表示链接的文件有问题
黄色：表示设备文件
灰色：表示其它文件
```



```linux
- ctrl shift +       放大窗口
- ctrl -             缩小窗口  
- alt 1/2/3...       切换窗口  
- ctrl+shift+t       打开新的窗口
- cd /               切换到根目录
- /s ls     				看根目录下的内容 
- clear    					这个命令将会刷新屏幕，本质上只是让终端显示页向后翻了一页，如果向上滚动屏幕还可以看到之前的操作信息。一般都会用这个命令。 
- ctrl + l  				这个命令将完全刷新终端屏幕，之前的终端输入操作信息将都会被清空，这样虽然比较清爽，但整个命令过程速度有点慢，使用较少。
- cd ~  						返回到家（home）目录
ls -F 							查看目录中的文件 
ls -l 							显示文件和目录的详细资料 
ls -a 							显示隐藏文件，可以和l共同使用 
ls -B                 屏蔽波浪线
ls *[0-9]* 					显示包含数字的文件名和目录名 
ls --help            查看关于ls的帮助
- cd .    					当前目录
- cd ..   					返回上一级目录
- cd ../../    			返回上两级目录  
- cd - 					回到最近一次操作的目录
- cd  /home/code  	直接跟路径
- /bin: 					 存放用户的二进制文件
- /etc:						存放系统的配置文件
- /dev :					 存放设备文件
- /boot:					 存放内核引导的配置文件
- /home：					本地用户主目录
- /lib:						动态共享库
- /lostfound：			文件系统恢复时的恢复文件
- /temp:					临时文件
- /mnt :					文件系统临时挂载点
- /media:					可卸载存储介质挂载点
- /proc：				 特殊的动态目录,这个目录本身是虚拟文件系统
- usr:						存放用户应用程序-
- man  ls：        man命令是Linux下的帮助指令，通过man指令可以查看Linux中的指令帮助、配置文件帮助和编程帮助等信息。  
-/root						超级管理员的命令
- f  						下翻
- q 						退出
- which ls  
结尾带波浪号的文件是文本编辑器在编辑文件时的备份文件，可以卸载。
- which cd  		 在超级命令中
- which  				寻找命令在哪里放着
- where 
- pwd:    			显示工作的路径
- echo 123 ：		输出内容
- echo 123 >1.txt: 创建文件夹
- touch 2.txt:		创建文件夹
- cat 1.txt :			预览文件夹
- echo 456 >>1.txt  追加文件，456后面是空格
- gedit 1.txt:		编辑文件
- vim 1.txt:			编辑文件，也可以直接创建， 命令模式（i键），插入模式（esc ,:wq）（q!强制退出）,末行模式，set number:显示行数
- ifconfig :			找到本机详细信息
- -开头的是文件，d开头的是文件夹
- sudo apt-get install vim 
- mkdir a:				创建新目录
- rmdir a:				删除目录，但是只能删除空目录
- mkdir -p a/b/c  创建多个文件
- rmdir -p a/b/c  删除目录，但是只限于a,b,c同时为空目录。
- rm -rf a: 			删除文件夹
- rm *.txt :			删除所有的.txt文件
- mv a aaa:				重命名(将a改名为aaa) 
- mv aaa documents:剪切
- cp 1.txt 2.txt:	拷贝文件 （原文件夹和目标文件夹）
- cp a -r b:			拷贝文件夹
tree 						 显示文件和目录由根目录开始的树形结构(1) 
iconv -l          列出已知的编码 
history           历史记录
history -c        清空历史记录
ln -s a.txt ../project/a.txt     软链接，又叫符号链接，基本不占内存的空间
ln a.txt b.txt                   硬链接，会占用内存空间，无论是软连接还是硬链接，改变其中一个，其他的都会随之改变。硬链接只能做文件，不能做文件夹，而软链接都可以。
sudo ln a.txt b.txt 
find nginx         查找相关的文件或者文件夹
find ngi* > 1.txt  将查找的内容放到一个文件里面
sudo find ngi* | grep con   通过|管道查询，find是查找文件，grep是查找内容
grep b *.txt       通过内容寻找（寻找文本）
sudo rm -rf 1.txt  提供超级管理员权限删除
ps -aux            process,即进程
ps -aux | grep 14  在进程中查找为14的内容
netstat -ano | grep '5000'  查找端口
echo $PATH 查看全局变量的路径，可以在~/.profile文件下设置全局变量
```

### 文件的解压缩：

```linux
tar -cvf b a   打包文件夹  b是目标文件，a是原文件夹
tar -xvf b -C c  解压文件夹
tar -cvf aaa a.txt 打包文件
tar -xvf aaa -C ../b 解压文件
tar -zcvf b a     压缩文件夹        -z grip压缩格式  -j  bz2压缩格式  
tar -zxvf b -C c  解压文件夹
-c   创建打包文件
-v   显示打包过程
-f   指定打包后的文件名
-x   解包
-z   压缩格式   gzip
-j   压缩格式   bz2
zip压缩： zip dest source
unzip解压:unzip dest
```

### 文件的传输：

```linux
通讯协议 1.电话2.手机3.QQ4.微信5.信件6.交通工具
ping   基于http协议
ssh    ssh（secure shell）协议，window不支持协议，所以需要装ssh协议 优点：1.速度快 2.加密 3.需要口令正确才可以
ftp协议
git     基于ssh协议
```

## ssh:

```linux
cmd上面：ssh 用户名@ip地址，然后yes就可以连接到。
putty:下载好之后直接输入IP地址，进入新的界面后为login as:用户名，然后接着填写密码。
scp aa.html npn @192.168.227.128:/home/npn    本地文件传送到另一台电脑。
scp -r a  npn @192.168.227.128:/home/npn      本地文件夹传送到另一台电脑。
scp -r npn@192.168.227.128:/home/code/a b			远程电脑的文件传递到本机上
全局变量  我的电脑->属性->高级选项-> 环境变量PATH="//c//user//admin//appdata//local//programe//python//python3.7"
启动pycharm   sudo sh pycharm.sh
```

## mysql:

```linux
mysql -u root -p    登录mysql数据库，-u表示用户名，-p表示登录的密码。
```

## 磁盘管理：

- cd  切换目录
- df  查看磁盘使用情况
- df  -h  更利于查看
- df run
- du  查看当前目录下的存储状态

## 网络通讯：

- ifconfig  查看或者设置网卡

- ifconfig eth0 修改地址

- ipconfig  window上查看网卡

- cd /etc     vim host

- udp协议   u-所有  d-用网的所有软件   p-占用的端口  

- tcp 协议

  - TCP与UDP区别总结

  1.TCP面向连接（如打电话要先拨号建立连接）;UDP是无连接的，即发送数据之前不需要建立连接。

  2、TCP提供可靠的服务。也就是说，通过TCP连接传送的数据，无差错，不丢失，不重复，且按序到达;UDP尽最大努力交付，即不保证可靠交付。Tcp通过校验和，重传控制，序号标识，滑动窗口、确认应答实现可靠传输。如丢包时的重发控制，还可以对次序乱掉的分包进行顺序控制。

  3、UDP具有较好的实时性，工作效率比TCP高，适用于对高速传输和实时性有较高的通信或广播通信。

  4.每一条TCP连接只能是点到点的;UDP支持一对一，一对多，多对一和多对多的交互通信。

  5、TCP对系统资源要求较多，UDP对系统资源要求较少。

- netstat -aup  查看网络的状态

- netstat -atp  查看网络的状态 

## 软件安装和管理：

- apt-get 方式安装        从仓库里面安装，安全，但是更新速度慢，软件不丰富，相对较少
- sudo  apt-get update    获取新的软件包列表
- sudo apt-get-repository ppa :webupa8team/java       ppa(个人软件包档案)  
- sudo apt-get install mysql-server  mysql-client     安装软件的命令
- ps  -aux | grep mysql
- sudo apt-get remove packagename 卸载软件
- apt-get --purge  remove mysql-server mysql-client   删除软件包包括该软件的配置文件
- apt-get automove mysql-server mysql-client 删除该软件的依赖包
- sudo apt-get clean && sudo apt-get autoclean  删除该软件的无用包
- umake --remove ide pycharm   卸载社区版pycharm

## 源码安装：

- 下载源码：wget url

- 解压文件  tar -zxvf filename

- 进入解压目录 cd  filename

- 找到configure并执行以下命令  ./configure --prefix=(/usr/local/test)/opt/python3.7[--enable-optimizations] 配置安装位置[配置优化]

- 编译 make all

- 安装 make install  

- 多版本共存 

  -  sudo update-alternatives --install  /usr/bin/python3  python3 /opt/python/bin/python3.7   500(优先级) 

  - ​    update-alternatives --install link name path priority[]  

  - update-alternatives 是符号链接管理工具。用于分组管理命令的链接和优先级。 

  - --display name

    显示链接组的信息。信息包括链接组的模式（自动或手动）；链接的指针（链到了那一个文件）；优先级是多少；当前最优版本等。

  - ```
    --install <链接> <名称> <路径> <优先级>
    ```

  其中link为系统中功能相同的公共链接目录

  - python --version 查看版本

## python版本的变换：

```py
1.查询python3的路径：which python3
2.删除该路径下的python3：sudo rm -rf 路径
3.利用update-alternatives设置优先级。
```



### 参考：

```linux
一.下载对应的 .tgz包 
终端进入要保存tgz包的目录 
根据自己需要的版本来替换掉路径中的版本号（eg.我下的是3.6.1）
1.wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz

二.解压到安装目录
1.sudo mkdir /usr/lib/python 
2.tar -zxvf Python-3.6.1.tgz -C /usr/lib/python
3.余下步骤
cd /usr/lib/python/Python-3.6.1
sudo ./configure
sudo make all
sudo make install
```

## 关机：

- $ halt   立即关机

- $ poweroff 立刻关机

- $ shutdown -h now  立刻关机（root用户使用）

- $ shutdown -h 10     十分钟后自动关机

  

## 重启：

- $ reboot 
- $ shutdown -r now
- $ shutdown -r now 10
- $ shutdown -r 20.55
- $ shutdown -c 取消重启

## 进程：

- ps -aux   显示所有包含使用者的进程，是静态的
- top        动态显示所有进程，关掉q退出
- kill pad  杀死进程     如果杀不掉，说明他是守护进程，在etc/init.d/里面寻找 ，直接输入命令sudo /etc/inint.d/mysql stop(停止)/start(开始)/restart(重启)
- kill -9或者-10  pad 强制杀死进程

### 下载pycharm：

- 同上，并且运行bin/pycharm.sh    $ sudo sh pycharm/bin/pycharm.sh  
- 破解
  - 获得注册码，输入网址http://idea.lanyus.com
- 修改host文件
  - 修改host文件   将0.0.0.0 account.jetbrains.com和0.0.0.0 www.jetbrains.com添加到/etc/hosts文件里面
  - 如果是window系统，host文件在C:\Windows\System32\drivers\etc\hosts下。
- 创建快捷方式：
  - ubuntu的快捷方式都放在/usr/shar中

## 权限管理：

> 多用户 多任务的操作系统

- whoami 查看当前用户

- who 查看所有的登录用户

- sudo useradd   -m first 创建新用户  
  - -m  自动创建家目录
  - -d 指定用户登录时的起始目录
  - -g  添加
  - -G 追加

- passwd 修改密码   可以在cat /etc/passwd下可以寻找     sudo passwd first(设置密码)

- userdel -f  first删除用户    

  - -f 强制删除  

- usermod  修改用户

- usermod first -d /home/first/demo  指定用户的登录起始目录

- usermod first -g  aaa 将用户指定为一个组（主组 无法删除）

- cat group 

- sudo groupadd demo  创建demo组   

- groups first             查询first组

  将用户添加到组中：

  - adduser aaa -g bbb 属于bbb组
  - sudo gpasswd -a first demo 追加

- adduser aaa -G bbb  既属于aaa又属于bbb，最前面的是主组，后面的是副组

- sudo gpasswd -d first demo 删除

- sudo groupdel demo 删除demo组

- sudo groupmod  组名 -n 新组名        修改组

- sudo usermod -a -G sudo first   给first sudo组的权限

- sudo usermod -a -G adm  first    给first adm组的权限

- sudo gpasswd -a first npn           将first放到npn中

- 日志在var下auth.log      shift+g   翻页到最下面 

- su 切换用户

- chown  用来修改文件或者目录所属的用户 sudo chown -R first：first   aaa  

- -R  递归的意思

- chmod  更改文件的权限  chmod  u=rwx  ,g=remx ,o=rmx    aaa  

- 1->x  2->w  4->r 3->xw 5->rx  6->wr  7->rwx  eg:sudo chmod -R  777 aaa

- 在py文件里面写入#！/usr/bin/env python，比如为demo.py，输入命令./demo.py,表示这个文件在python下执行。

- mount -o remount wr /  挂载的意思

- 重启时按住shift进入高级选项，进入恢复模式，进入root，执行上面代码。

- ajax    (asyc javascript and xml)

### pip升级命令：

```linux
python -m pip install --upgrade pip 
python -m pip install -U --force-reinstall pip 可以实现。
pip install --upgrade pip   更新pip的命令
pip install 文件名   利pip下载一些软件
python -m pip uninstall pip  卸载pip

```

## window杀死进程的命令：

```window
netstat -ano | findstr 8080   通过端口号找到某个进程
tasklist | findstr 7740       通过进程编号，找到对应的应用程序
taskkill -PID 7704 -F         根据查询到的线程编号，直接强制杀死该进程。
```

## Linux当遇到Operation not permitted的问题时：

lsattr命令告诉你答案：

```linux
[root@meizhiyin .ssh]# lsattr 文件夹路径
----i--------e- ./authorized_keys
-------------e- ./known_hosts
```

多了一个i，执行如下：

```linux
[root@meizhiyin .ssh]# chattr -i 文件夹路径
[root@meizhiyin .ssh]# lsattr 
-------------e- ./authorized_keys
-------------e- ./known_hosts
[root@meizhiyin .ssh]# vim authorized_keys 
```

ok，可以编辑保存了。

如果想把文件保护起来，执行如下：

```linux
chattr +i authorized_keys 
```

## 虚拟环境：

- 步骤
  - 创建：python3  -m venv  tutorial-env
  - 激活：source  tutorial-env /bin/activate
  - 退出虚拟环境：deactivate
  - 进入虚拟环境：python3 -m  venv
  - ctrl+z 进入后台;fg %1 返回以前的环境

