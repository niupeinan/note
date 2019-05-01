# cookile:

调用cookie
引入request中的cookie字典对象即可

    request.cookies['']
### 写入cookis:

1需要导入

flask.make_response
from flask import make_response

2.在视图函数中虽不可直接操作response对象，但是，对于cookies这种低层次的操作，可以在视图函数中使用make_response() 
包装，则可以得到一个response对象
response = make_response(render_template('index.html',title='Hello World!'))

3通过response.set_cookie()就可以写入相应的cookie内容了

​	response.set_cookie('username','')

## 一、cookie和session的介绍

cookie不属于http协议范围，由于http协议无法保持状态，但实际情况，我们却又需要“保持状态”，因此cookie就是在这样一个场景下诞生。

cookie的工作原理是：由服务器产生内容，浏览器收到请求后保存在本地；当浏览器再次访问时，浏览器会自动带上cookie，这样服务器就能通过cookie的内容来判断这个是“谁”了。

cookie虽然在一定程度上解决了“保持状态”的需求，但是由于cookie本身最大支持4096字节，以及cookie本身保存在客户端，可能被拦截或窃取，因此就需要有一种新的东西，它能支持更多的字节，并且他保存在服务器，有较高的安全性。这就是session。

问题来了，基于http协议的无状态特征，服务器根本就不知道访问者是“谁”。那么上述的cookie就起到桥接的作用。

我们可以给每个客户端的cookie分配一个唯一的id，这样用户在访问时，通过cookie，服务器就知道来的人是“谁”。然后我们再根据不同的cookie的id，在服务器上保存一段时间的私密资料，如“账号密码”等等。

总结而言：cookie弥补了http无状态的不足，让服务器知道来的人是“谁”；但是cookie以文本的形式保存在本地，自身安全性较差；所以我们就通过cookie识别不同的用户，对应的在session里保存私密的信息以及超过4096字节的文本。

另外，上述所说的cookie和session其实是共通性的东西，不限于语言和框架

## 二、登录应用原理

​      先说一下这种认证的机制。每当我们使用一款浏览器访问一个登陆页面的时候，一旦我们通过了认证。服务器端就会发送一组随机唯一的字符串（假设是123abc）到浏览器端，这个被存储在浏览端的东西就叫cookie。而服务器端也会自己存储一下用户当前的状态，比如login=true，username=hahaha之类的用户信息。但是这种存储是以字典形式存储的，字典的唯一key就是刚才发给用户的唯一的cookie值。那么如果在服务器端查看session信息的话，理论上就会看到如下样子的字典

{'123abc':{'login':true,'username:hahaha'}}

因为每个cookie都是唯一的，所以我们在电脑上换个浏览器再登陆同一个网站也需要再次验证。那么为什么说我们只是理论上看到这样子的字典呢？因为处于安全性的考虑，其实对于上面那个大字典不光key值123abc是被加密的，value值{'login':true,'username:hahaha'}在服务器端也是一样被加密的。所以我们服务器上就算打开session信息看到的也是类似与以下样子的东西

{'123abc':dasdasdasd1231231da1231231}

## 三、cookie的简单使用

### **1、获取Cookie**

```
request.COOKIES.get("islogin",None)  #如果有就获取，没有就默认为none
```

### **2、设置Cookie**

```
  obj = redirect("/index/")
  obj.set_cookie("islogin",True)  #设置cookie值，注意这里的参数，一个是键，一个是值
  obj.set_cookie("haiyan","344",20)  #20代表过期时间
  obj.set_cookie("username", username)
```

### **3、删除Cookie**

```
obj.delete_cookie("cookie_key",path="/",domain=name)
```

 **登录认证示例：**

需要知道几点

一共有三次请求
　　注意：form表单的action走的路径还是/login/
　　　　　第一次请求：url:http://127.0.0.1:8080/login get请求
　　　　   第一次请求：url:http://127.0.0.1:8080/login post请求 user pasw
　　　　   第一次请求：url:http://127.0.0.1:8080/index post请求 携带着cookie的了
　　　　   所以在index页面中就会取到cookie,因为这是的index里面已经有cookie了

![img](https://images2017.cnblogs.com/blog/1184802/201711/1184802-20171101150351857-966823567.png)

cookie存储到客户端

优点：数据存储在客户端。减轻服务端的压力，提高网站的性能

缺点：安全性不高，在客户端很容易被查看或破解用户会话信息

## 四、session的简单使用

**1、基本操作(需要掌握的)**

```
1、设置session值
　　　　request.session["session_name"]="admin"
2、获取session值
　　　　session_name = request.session("session_name")
3、删除session值
　　　　del request.session["session_name"]  删除一组键值对
　　　　request.session.flush()   删除一条记录
4、检测是否操作session值
　　　　if "session_name"  is request.session:
5、get(key, default=None)
 
fav_color = request.session.get('fav_color', 'red')
 
6、pop(key)
 
fav_color = request.session.pop('fav_color')
 
7、keys()
 
8、items()
 
9、setdefault()
 
10、flush() 删除当前的会话数据并删除会话的Cookie。
            这用于确保前面的会话数据不可以再次被用户的浏览器访问
            例如，django.contrib.auth.logout() 函数中就会调用它。
 
 
11 用户session的随机字符串
        request.session.session_key
  
        # 将所有Session失效日期小于当前日期的数据删除
        request.session.clear_expired()
  
        # 检查 用户session的随机字符串 在数据库中是否
        request.session.exists("session_key")
  
        # 删除当前用户的所有Session数据
        request.session.delete("session_key")
  
        request.session.set_expiry(value)
            * 如果value是个整数，session会在些秒数后失效。
            * 如果value是个datatime或timedelta，session就会在这个时间后失效。
            * 如果value是0,用户关闭浏览器session就会失效。
            * 如果value是None,session会依赖全局session失效
```

**2、流程解析图**

![img](https://images2017.cnblogs.com/blog/1184802/201711/1184802-20171101152145982-1740200133.png)

由于cookie会把所有的信息都保存在客户端，也就是浏览器上，这样会导致不安全，所以引用了session，但是只是单单的session也不好用，必须session和cookie配合这去用。

session会把信息保存在服务端。

session原理分析流程：

{"sessionID":"dfhasdjfhkjlcn4352kjdsfhkjsd"}

if  post:

　　request.session["is_login"]=True

　　request.session["user"]=username

　　return redirect("/index/”)

Django会做三件事：

　　1、创建随机字符串。假如s="sdgsdfg4565dfgsdfgsdf" 

　　2、 在django-session表中，添加一条记录

　　　　django-session有三个字段，分别是：session_key，session_data，expire_data

　　　   SQL: 语句： insert into django-session values (s,"{"IS_LOGON":True,"USER":egon}",12321)

　　3、给浏览器设置sessionID：  obj.set_cookie("sessionID",s)  

执行完之后重定向：

/home/ ----> {"sessionID":"fasdlkfjsakdl324ada2adhdjlka99"}

request.session.get("IS_LOGON",None)
在django-session表中，进行查询：
s=requset.COOKIE.get("sessionID")
select session-data from django-session where session-key=s

**3、示例**

**views.py**

**template**

**4、session存储的相关配置**

 (1)默认的是数据库配置：        

（2）缓存配置

（3）文件配置

