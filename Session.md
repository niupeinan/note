## 示例：

``` session
from flask import Flask, session
from flask.ext.session import Session

app = Flask(__name__)
# Check Configuration section for more details
SESSION_TYPE = 'redis'
app.config.from_object(__name__)
Session(app)

@app.route('/set/')
def set():
    session['key'] = 'value'
    return 'ok'

@app.route('/get/')
def get():
    return session.get('key', 'not set')
```

## flask中的session工作机制：

1. flask中的session机制是：把敏感数据经过加密后放入`session`中，然后再把`session`存放到`cookie`中，下次请求的时候，再从浏览器发送过来的`cookie`中读取`session`，然后再从`session`中读取敏感数据，并进行解密，获取最终的用户数据。

2. flask的这种`session`机制，可以节省服务器的开销，因为把所有的信息都存储到了客户端（浏览器）。

3. 安全是相对的，把`session`放到`cookie`中，经过加密，也是比较安全的，这点大家放心使用就可以了。

 





## 操作session：

1. session的操作方式：

    *使用`session`需要从`flask`中导入`session`，以后所有和`sessoin`相关的操作都是通过这个变量来的。

    *使用`session`需要设置`SECRET_KEY`，用来作为加密用的。并且这个`SECRET_KEY`如果每次服务器启动后都变化的话，那么之前的`session`就不能再通过当前这个`SECRET_KEY`进行解密了。

    *操作`session`的时候，跟操作字典是一样的。

    *添加`session`：`session['username']`。

    *删除：`session.pop('username')`或者`delsession['username']`。

    *清除所有`session`：`session.clear()`

    *获取`session`：`session.get('username')`

2. 设置session的过期时间：

    *如果没有指定session的过期时间，那么默认是浏览器关闭后就自动结束

    *如果设置了session的permanent属性为True，那么过期时间是31天。

    *可以通过给`app.config`设置`PERMANENT_SESSION_LIFETIME`来更改过期时间，这个值的数据类型是`datetime.timedelay`类型。
---------------------
## flask_session:

flask-session是flask框架的session组件，由于原来flask内置session使用签名cookie保存，该组件则将支持session保存到多个地方，如：

- redis：保存数据的一种工具，五大类型。非关系型数据库
- memcached
- filesystem
- mongodb
- sqlalchmey：那数据存到数据库表里面安装.

# 存储方式

### redis

```
#!/usr/bin/env python
# -*- coding:utf-8 -
import redis
from flask import Flask, session
from flask_session import Session
import memcache

app = Flask(__name__)
app.debug = True
app.secret_key = 'xxxx'


app.config['SESSION_TYPE'] = 'memcached' # session类型为redis
app.config['SESSION_PERMANENT'] = True # 如果设置为True，则关闭浏览器session就失效。
app.config['SESSION_USE_SIGNER'] = False # 是否对发送到浏览器上session的cookie值进行加密
app.config['SESSION_KEY_PREFIX'] = 'session:' # 保存到session中的值的前缀
app.config['SESSION_MEMCACHED'] = memcache.Client(['10.211.55.4:12000'])


Session(app)


@app.route('/index')
def index():
    session['k1'] = 'v1'
    return 'xx'


if __name__ == '__main__':
    app.run()
```

### filesystem

```
#!/usr/bin/env python
# -*- coding:utf-8 -
import redis
from flask import Flask, session
from flask_session import Session

app = Flask(__name__)
app.debug = True
app.secret_key = 'xxxx'

app.config['SESSION_TYPE'] = 'filesystem'  # session类型为redis
app.config[
    'SESSION_FILE_DIR'] = '/Users/wupeiqi/PycharmProjects/grocery/96.Flask新课程/组件/2.flask-session'  # session类型为redis
app.config['SESSION_FILE_THRESHOLD'] = 500  # 存储session的个数如果大于这个值时，就要开始进行删除了
app.config['SESSION_FILE_MODE'] = 384  # 文件权限类型

app.config['SESSION_PERMANENT'] = True  # 如果设置为True，则关闭浏览器session就失效。
app.config['SESSION_USE_SIGNER'] = False  # 是否对发送到浏览器上session的cookie值进行加密
app.config['SESSION_KEY_PREFIX'] = 'session:'  # 保存到session中的值的前缀

Session(app)


@app.route('/index')
def index():
    session['k1'] = 'v1'
    session['k2'] = 'v1'
    return 'xx'


if __name__ == '__main__':
    app.run()
```

### mongodb

```
#!/usr/bin/env python
# -*- coding:utf-8 -
import redis
from flask import Flask, session
from flask_session import Session
import pymongo

app = Flask(__name__)
app.debug = True
app.secret_key = 'xxxx'

app.config['SESSION_TYPE'] = 'mongodb'  # session类型为redis

app.config['SESSION_MONGODB'] = pymongo.MongoClient()
app.config['SESSION_MONGODB_DB'] = 'mongo的db名称（数据库名称）'
app.config['SESSION_MONGODB_COLLECT'] = 'mongo的collect名称（表名称）'

app.config['SESSION_PERMANENT'] = True  # 如果设置为True，则关闭浏览器session就失效。
app.config['SESSION_USE_SIGNER'] = False  # 是否对发送到浏览器上session的cookie值进行加密
app.config['SESSION_KEY_PREFIX'] = 'session:'  # 保存到session中的值的前缀

Session(app)


@app.route('/index')
def index():
    session['k1'] = 'v1'
    session['k2'] = 'v1'
    return 'xx'


if __name__ == '__main__':
    app.run()
```

mongodb操作简单示例：

```
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pymongo import MongoClient

# 创建链接
conn = MongoClient('47.93.4.198', 27017)

# 选择数据库
db = conn['db1']

# 选择表
posts = db['posts']

post_data = {
    'name': 'alex',
    'age': 18
}

# 表中插入数据
# result = posts.insert_one(post_data)

# 获取一条数据
# row = posts.find_one()
# print(row)

# # 获取多条数据
# rows = posts.find()
# for row in rows:
#     print(row)

# 删除多条数据
# rows = posts.delete_many(filter={})
# print(rows)

# 更新多条数据
# posts.update({}, {'name': 'wupeiqi'})
```

### sqlalchemy

```
#!/usr/bin/env python
# -*- coding:utf-8 -
import redis
from flask import Flask, session
from flask_session import Session as FSession
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.secret_key = 'xxxx'

# 设置数据库链接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@127.0.0.1:3306/fssa?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 实例化SQLAlchemy
db = SQLAlchemy(app)



app.config['SESSION_TYPE'] = 'sqlalchemy'  # session类型为sqlalchemy
app.config['SESSION_SQLALCHEMY'] = db # SQLAlchemy对象
app.config['SESSION_SQLALCHEMY_TABLE'] = 'session' # session要保存的表名称
app.config['SESSION_PERMANENT'] = True  # 如果设置为True，则关闭浏览器session就失效。
app.config['SESSION_USE_SIGNER'] = False  # 是否对发送到浏览器上session的cookie值进行加密
app.config['SESSION_KEY_PREFIX'] = 'session:'  # 保存到session中的值的前缀
FSession(app)


@app.route('/index')
def index():

    session['k1'] = 'v1'
    session['k2'] = 'v1'

    return 'xx'


if __name__ == '__main__':
    app.run()
```
# Djaong Cookie、Session使用.md 

> #### Cookie

```
cookies
获取cookies   request.COOKIES['username']
设置cookie      response.set_cookie('key','value',max_length=秒钟,expires=日期)
path="/" 那个页面下可以使用cookie
domain  =""  生效的域名
secure = False https传输
httponly = js中获取不到
```

> #### Session
>
> 配置种类：

- 数据库（默认）
- 缓存
- 文件
- 缓存+数据库
- 加密cookie

> #### 数据库 Session

```
    # 配置
    SESSION_ENGINE = 'django.contrib.sessions.backends.db'   # 引擎（默认）
```

> #### 其他公共配置

```
    SESSION_COOKIE_NAME ＝ "sessionid"                       # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
    SESSION_COOKIE_PATH ＝ "/"                               # Session的cookie保存的路径（默认）
    SESSION_COOKIE_DOMAIN = None                             # Session的cookie保存的域名（默认）
    SESSION_COOKIE_SECURE = False                            # 是否Https传输cookie（默认）
    SESSION_COOKIE_HTTPONLY = True                           # 是否Session的cookie只支持http传输（默认）
    SESSION_COOKIE_AGE = 1209600                             # Session的cookie失效日期（2周）（默认）
    SESSION_EXPIRE_AT_BROWSER_CLOSE = False                  # 是否关闭浏览器使得Session过期（默认）
    SESSION_SAVE_EVERY_REQUEST = False                       # 是否每次请求都保存Session，默认修改之后才保存（默认）
```

> #### session使用

```
    #使用
        def index(request):
            # 获取、设置、删除Session中数据
            request.session['k1'] = 'ydh' # 设置
            request.session.get('k1',None)
            request.session['k1'] = 123
            request.session.setdefault('k1',123) # 存在则不设置
            del request.session['k1']
     
            # 所有 键、值、键值对
            request.session.keys()
            request.session.values()
            request.session.items()
            request.session.iterkeys()
            request.session.itervalues()
            request.session.iteritems()
     
     
            # 用户session的随机字符串
            request.session.session_key
     
            # 将所有Session失效日期小于当前日期的数据删除
            request.session.clear_expired()
     
            # 检查 用户session的随机字符串 在数据库中是否
            request.session.exists("session_key")
     
            # 删除当前用户的所有Session数据
            request.session.delete("session_key")
     
            request.session.set_expiry(value)
                * 秒数
                * datatime或timedelta
                * 0,用户关闭浏览器session失效。
```

> #### 缓存Session

```
    配置：
    SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # 引擎
    SESSION_CACHE_ALIAS = 'default'                            # 使用的缓存别名（默认内存缓存，也可以是memcache），此处别名依赖缓存的设置
 
```

> #### 文件

```
    SESSION_ENGINE = 'django.contrib.sessions.backends.file'    # 引擎
    SESSION_FILE_PATH = None                                    # 缓存文件路径，如果为None，则使用tempfile模块获取一个临时地址tempfile.gettempdir()
 
```

> #### 缓存+数据库session

```
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'        # 引擎
```

> #### 加密cookie Session

```
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'   # 引擎
```