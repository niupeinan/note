##  fetch方法：

使用Fetch发送也很简单，只需要配置三个参数。

```
fetch('some-url', options);
```

第一个参数是设置请求方法（如`post`、`put`或`del`），Fetch会自动设置方法为`get`。

第二个参数是设置头部。因为一般使用JSON数据格式，所以设置`ContentType`为`application/json`。

第三个参数是设置包含JSON内容的主体。因为JSON内容是必须的，所以当设置主体时会调用`JSON.stringify`。

```
fetch(url, options).then(function(response) {
  // handle HTTP response
}, function(error) {
  // handle network error
})
```

具体参数案例：

```
//兼容包
require('babel-polyfill')
require('es6-promise').polyfill()

import 'whatwg-fetch'

fetch(url, {
  method: "POST",
  body: JSON.stringify(data),
  headers: {
    "Content-Type": "application/json"
  },
  credentials: "same-origin"
}).then(function(response) {
  response.status     //=> number 100–599
  response.statusText //=> String
  response.headers    //=> Headers
  response.url        //=> String

  response.text().then(function(responseText) { ... })
}, function(error) {
  error.message //=> String
})
```

#### url

定义要获取的资源。这可能是：

- 一个 `USVString` 字符串，包含要获取资源的 `URL`。
- 一个 `Request` 对象。

#### options（可选）

一个配置项对象，包括所有对请求的设置。可选的参数有：

- `method`: 请求使用的方法，如 `GET`、`POST`。
- `headers`: 请求的头信息，形式为 `Headers` 对象或 `ByteString`。
- `body`: 请求的 `body` 信息：可能是一个 `Blob`、`BufferSource`、`FormData`、`URLSearchParams` 或者 `USVString` 对象。注意 `GET` 或 `HEAD` 方法的请求不能包含 `body` 信息。
- `mode`: 请求的模式，如 `cors`、 `no-cors` 或者 `same-origin`。
- `credentials`: 请求的 `credentials`，如 `omit`、`same-origin` 或者 `include`。
- `cache`: 请求的 `cache` 模式: `default`, `no-store`, `reload`, `no-cache`, `force-cache`, 或者 `only-if-cached`。

#### response

一个 `Promise`，`resolve` 时回传 `Response` 对象：

- 属性：

  - `status (number)` - HTTP请求结果参数，在100–599 范围

  - `statusText (String)` - 服务器返回的状态报告

  - `ok (boolean)` - 如果返回200表示请求成功则为true

  - `headers (Headers)` - 返回头部信息，下面详细介绍

  - `url (String)` - 请求的地址

  - Github返回的响应是JSON格式的，所以调用`response.json`方法来转换数据。

    还有其他方法来处理不同类型的响应。如果请求一个XML格式文件，则调用`response.text`。如果请求图片，使用`response.blob`方法。

    所有这些方法(`response.json`等等）返回另一个Promise，所以可以调用`.then`方法处理我们转换后的数据。

- 方法：

  - `text()` - 以`string`的形式生成请求text
  - `json()` - 生成`JSON.parse(responseText)`的结果
  - `blob()` - 生成一个`Blob`
  - `arrayBuffer()` - 生成一个`ArrayBuffer`
  - `formData()` - 生成格式化的数据，可用于其他的请求

- 其他方法：

  - `clone()`
  - `Response.error()`
  - `Response.redirect()`

#### response.headers

- `has(name) (boolean)` - 判断是否存在该信息头
- `get(name) (String)` - 获取信息头的数据
- `getAll(name) (Array)` - 获取所有头部数据
- `set(name, value)` - 设置信息头的参数
- `append(name, value)` - 添加header的内容
- `delete(name)` - 删除header的信息
- `forEach(function(value, name){ ... }, [thisContext])` - 循环读取header的信息

## ajax:

> 利用js异步的与数据进行交互

```ajax
var ajax = new XMLHttpRequest()    创建对象
ajax.onreadystatechange=function(ev){   记录每一次的状态变化
	if(ajax.readyState==4){
    iif(ajax.status==200){
      console.log(ajax.response)
    }
	}
}
ajax.onload=function(ev){   监听对象
  console.log(ajax.response)（response获取的是文本形式）
}
ajax.open("post","2.html") #用什么方式取数据
ajax.send() 
xml 小于号加？号
lsof -p | grep 3333
```

### ajax解决的问题：

- - 页面无刷新操作数据
  - 按需获取的问题
  - 让b/s架构的软件，能够像基于c/s架构的软件操作流畅
- async javascript and xml
- new XMLHttpRequest()
- open() send()  
- 传递数据

### 注意:

- url  访问的地址

- [type]  object类型

- [dataType] text

- [date] 数据

- [success]  null

- jianja   模板引擎

- 在Form元素的语法中，EncType表明提交数据的格式 用 Enctype 属性指定将数据回发到服务器时浏览器使用的编码类型 

- 区块链  信任的问题，加密的技术

- 跨境电商   外贸和全球化  

- ```
  &：参数连接符号。用来链接多个参数的值。到后台进行单独获得和处理。
  ```

### 代码：

```js
//插入图片
ajax.onload=function(ev){
  var doc=(ajax.response)
  file=new FileReader()
  file.onload=function(ev2)
}
  
post方法：
ajax.open("post","/")
ajax.setRequestHeader("content-type","application/x-www-form-urllencoded")
ajax.send("name=zhangdsan")
  
get方法：
ajax.open("get","/?name=zhangsan")
ajax.send
  
GET请求会将参数跟在URL后进行传递，而POST请求则是作为HTTP消息的实体内容发送给WEB服务器。
GET - 从指定的资源请求数据
POST - 向指定的资源提交要处理的数据
```

## ajax解决跨域问题：

- jsonp  快捷一点  有着诸多限制   局限性：自己有权限操作的两个域名或者对方配合的服务
  - script  src="  " 通过script标签获取的内容，会当做js代码执行
- 代理   流程比较复杂 几乎没有限制 缺点：效率慢，开发慢 原理：python具有客户端的能力。  

## jsonp:

```py
概念：它是在文档中插入一个script标签，创建_callback方法，通过服务器配合执行_callback方法，并传入一些参数

 JSONP的优点是：它不像XMLHttpRequest对象实现的Ajax请求那样受到同源策略的限制；它的兼容性更好，在更加古老的浏览器中都可以运行，不需要XMLHttpRequest或ActiveX的支持；并且在请求完毕后可以通过调用callback的方式回传结果。

JSONP的缺点则是：它只支持GET请求而不支持POST等其它类型的HTTP请求；它只支持跨域HTTP请求这种情况，不能解决不同域的两个页面之间如何进行JavaScript调用的问题。

三种形式：
第一种形式：
1.HTML：
<script>
    function aaa(con){
        document.querySelector("div").innerHTML = con;
    }
</script>
<script src="http://127.0.0.1:9000/abc?callback=aaa"></script>
2.python:
@app.route("/abc")
def abc():
    fn = request.args.get("callback")
    return fn+"('ccc')"
 
第二种形式：
jquery:
$.ajax({
        url:"http://127.0.0.1:9000/abc?callback=callback",
        datatype:"jsonp",
        callback:"callback",
        success(e){
            $("div").html(e)
        }
    })
python:
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("ajax1.html")
@app.route("/abc")
def abc():
    return "ccc"

app.run(port=9000)

代理：
html:
var ajax = new XMLHttpRequest();
    ajax.onload = function(){
        console.log(ajax.response)
    };
    ajax.open("get","/ajax?http://127.0.0.1:9000/abc");
    ajax.send()
python:
from flask import Flask,render_template,request as request1
from urllib import request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("ajax2.html")
@app.route("/ajax")
def ajax():
    url = request1.args.get("vue");
    res = request.urlopen(url)
    con = res.read()
    con.decode("utf8")
    return render_template("ajax2.html")

app.run()
```

####  axios使用

- ##### 什么是axios?

  ```js
  一个基于promise的http库，可以用在浏览器和node.js上
  ```

- ##### 特性

  - 从浏览器上创建XMLHTTPRequests
  - 从node.js创建http请求
  - 支持PromiseAPI
  - 拦截请求和响应
  - 转换请求数据和响应数据
  - 取消请求
  - 自动转换JSON数据
  - 客户端支持防御XSRF（XSRF：跨站请求伪造。攻击者盗用你的身份，以你的名义发送恶意请求。它能做的事情包括： 以你的名义发送邮件，发送邮件，发消息，盗取你的账号，甚至购买商品，造成个人隐私泄露以及财产安全。）

- 