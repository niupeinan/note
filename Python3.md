## os.list方法：

### 概述

os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。 它不包括 '.' 和'..' 即使它在文件夹中。

只支持在 Unix, Windows 下使用。

### 语法

**listdir()**方法语法格式如下：

```
os.listdir(path)
```

### 参数

- **path** -- 需要列出的目录路径

### 返回值

返回指定路径下的文件和文件夹列表。

## insert_id().affected_rows()区别：

> 1.mysql_insert_id() 函数返回上一步 INSERT 操作产生的 ID。这个ID号是执行数据插入时的ID。 
>
>   如果上一查询没有产生 AUTO_INCREMENT 的 ID，则 mysql_insert_id() 返回 0。 
>
> 2.当执行写入操作（insert,update等）的查询后，显示被影响的行数 

## python处理图形图像的包：

- pillow
- 计算机底层处理图像的工具：opengl技术
- 浏览器处理对象的是canvas，实际上用的是webgl技术

## request 请求

```
from flask import request


@blue.route('/getrequest/', methods=['GET', 'POST'])
def get_request():
    if request.method == 'GET':
        args = request.args
    else:
        form = request.form
    return '获取request'
```

### 1.request的常用属性

##### a)methods

默认的请求方式只有GET，其他请求都需要通过参数methods进行指定。

```
methods=['GET', 'POST']
```

##### b)args：获取GET请求参数

flask中，要获取get请求的参数，不是通过request.GET.get()，而是通过request.args.get()获取。

```
request.agrs.get('参数名')
```

##### c)form：获取POST请求参数

flask中，要获取get请求的参数，不是通过request.POST.get()，而是通过request.form.get()获取。

```
request.form.get('参数名')
```

##### d)files 获取上传文件

```py
request.files("文件名")
```



##### e)base_url 获取请求路径

```py
request.base_url('路径')
```



##### f)host 获取ip和端口

```py
request.host('端口号')
```

## 二、make_response 响应

make_response()，相当于DJango中的HttpResponse。

##### 1.返回内容

```
from flask import make_response

@blue.route('/makeresponse/')
def make_response_function():
    response = make_response('<h2>羞羞哒</h2>')
    return response, 404
```

##### 2.返回页面

```
from flask import make_response

@blue.route('/makeresponse/')
def make_response_function():
    temp = render_template('hello.html')
    response = make_response(temp)
    return response
```

\>>>注意：make_response 想要返回页面，不能直接写做：make_response('hello.html')，必须用render_template('hello.html')形式。

##### 3.返回状态码

\>>>方式一：在make_response()中传入状态码

```
from flask import make_response

@blue.route('/makeresponse/')
def make_response_function():
    temp = render_template('hello.html')
    response = make_response(temp, 200)
    return response
```

\>>>方式二：直接return状态码

```
from flask import make_response

@blue.route('/makeresponse/')
def make_response_function():
    temp = render_template('hello.html')
    response = make_response(temp)
    return response, 200
```

## 三、redirect 跳转

flask中的 redirect 相当于 DJango中的 HttpResponseRedirect。

##### 1.参数是url形式

```
from flask import redirect


@blue.route('/redirect/')
def make_redirect():
    return redirect('/hello/index/')
```

##### 2.参数是 name.name 形式

url_for 相当于reverse，name.name 相当于django中的namespace:name，第一个name是初始化蓝图时的参数名，第二个name是函数名

```
from flask import redirect


@blue.route('/redirect/')
def make_redirect():
    return redirect(url_for('first.index'))
```
### 解决flask返回的字符创乱码的问题：

> 理论上说是要**保持client、MySQL中的character_set_client、table charset这三个字符集编码一致**，就可以保证乱码一定不会出现。 

​	在if __name__ == "\__main\__":加上一句

​		app.config[‘JSON_AS_ASCII’] = False 

​	json.dumps()解决同样的问题可以加入ensure_ascii=False

 

