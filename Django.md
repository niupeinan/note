# django:

## 创建Django项目

```django
django-admin startproject 项目名称
```

## Django应用包中的目录信息

mysite     #file: mysite/ 根目录只是你项目的容器， Django 不关心它的名字，你可以将它重命名为任何你喜欢的名字 	

​	mysite  #里面一层的 `mysite/` 目录包含你的项目，它是一个纯 Python 包。它的名字就是当你引用它内部任何东西时需要用到的 Python 包名。 (比如 `mysite.urls`).

​		\_\_init\__.py  #将文件夹变为一个Python模块,Python 中的每个模块的包中，都有\_\_init\__.py 文件。通常__init__.py 文件为空，但是我们还可以为它增加其他的功能。我们在导入一个包时，实际上是导入了它的__init__.py文件。这样我们可以在__init__.py文件中批量导入我们所需要的模块，而不再需要一个一个的导入。

​		setting.py #配置文件 

​		urls.py      #路由

​		wsgi.py     #服务器文件

​	manage.py      #Django指令文件,一个让你用各种方式管理 Django 项目的命令行工具。 

`Buildout `是一个基于Python的构建工具, `Buildout `主要是为了解决两个问题:

- 中心化的应用组装和部署
- 重复的从Python软件发布中组装项目

通过一个配置文件 `buildout.cfg `, 可以从多个部分创建、组装并部署你的应用, 能够构建一个封闭隔离的开发环境.

## 创建Django应用

```django
python manage.py startapp 应用名
```

mysite 

​	mysite   #项目包

​	polls      #应用包

​		migrations    #迁移文件包

​		\__init__.py

​		admin.py   #自定义后台界面

​		apps.py      #应用配置，主要设置应用名称

​		models.py  #数据模型

​		tests.py      #测试文件

​		views.py    #视图（MVT中的V）

​	manage.py   #工具文件

## 配置项目

```django
#'django.middleware.csrf.CsrfViewMiddleware',:跨域验证

# 配置语言
LANGUAGE_CODE = 'zh-hans'

# 配置时区
TIME_ZONE = 'Asia/Shanghai'

# 配置应用
INSTALLED_APPS 设置项。这里包括了会在你项目中启用的所有 Django 应用。应用能在多个项目中使用，你也可以打包并且发布应用，让别人使用它们。

通常， INSTALLED_APPS 默认包括了以下 Django 的自带应用：
django.contrib.admin -- 管理员站点.
django.contrib.auth -- 认证授权系统。
django.contrib.contenttypes -- 内容类型框架。
django.contrib.sessions -- 会话框架。
django.contrib.messages -- 消息框架。
django.contrib.staticfiles -- 管理静态文件的框架。
'polls'
这些应用被默认启用是为了给常规项目提供方便。

# 配置数据库
1.mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'polls',
	    'HOST':'localhost',
		'PORT':3306,
		'USER':'root',
		'PASSWORD':'',
    }
}

2.pymysql配置
在mysite/__init__.py下写入
import pymysql
pymysql.install_as_MySQLdb()

# 创建第一个视图
1.在应用视图文件中创建视图函数
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("123")

2.在应用中创建路由文件（urls.py）
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
]
# 函数 path() 具有四个参数，两个必须参数：route 和 view，两个可选参数：kwargs 和 name。
path() 参数： route¶
route 是一个匹配 URL 的准则（类似正则表达式）。当 Django 响应一个请求时，它会从 urlpatterns 的第一项开始，按顺序依次匹配列表中的项，直到找到匹配的项。

这些准则不会匹配 GET 和 POST 参数或域名。例如，URLconf 在处理请求 https://www.example.com/myapp/ 时，它会尝试匹配 myapp/ 。处理请求 https://www.example.com/myapp/?page=3 时，也只会尝试匹配 myapp/。

path() 参数： view¶
当 Django 找到了一个匹配的准则，就会调用这个特定的视图函数，并传入一个 HttpRequest 对象作为第一个参数，被“捕获”的参数以关键字参数的形式传入。稍后，我们会给出一个例子。

path() 参数： kwargs¶
任意个关键字参数可以作为一个字典传递给目标视图函数。本教程中不会使用这一特性。

path() 参数： name¶
为你的 URL 取名能使你在 Django 的任意地方唯一地引用它，尤其是在模板中。这个有用的特性允许你只改一个文件就能全局地修改某个 URL 模式。

3.在项目文件包中导入应用路由（mysite/urls.py）
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include("polls.urls")),
]

# 创建模型
在polls/models.py
from django.db import models

# Create your models here.
class Question(models.Model):  #models.Model自动创建主键
    question_text = models.CharField(max_length=200)  #max_length必填
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)   # 添加外键，on_delete必填
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# 创建迁移文件
python manage.py makemigrations polls

# 执行迁移
python manage.py migrate

# 创建站点
python manage.py createsuperuser

# 如果想使用mysqldb的方式，那么直接在py文件的开头加入如下两行代码即可(/musite/__init__.py)。
import pymysql
pymysql.install_as_MySQLdb()

#在HTML中两种路径的表达的方式
<td><a href="/polls/{{ item.id }}">{{item.question_text}}</a></td>    #{% url 'polls:results' item.id %}}

class Meta:
	abstract = True   # 不能被实例

# 获取变量的方式
name = request.POST.get("name",None)

# 创建对象的方法：
1.类名.objects.create()
2.obj = 类名（）
  obj.save()

# 引进js静态文件
{% load static %}
<script src="{% static '/demo/js/jquery.js '%}"></script>

# 修改表格
contenteditable属性   contenteditable='true'

# 逆向查询
person.objects.all()[0].project_set.all

# 正向查询
person.objects.all()[0]

# 在admin.py文件中注册信息：
1.admin.site.register(Question, QuestionAdmin)

2.@admin.register()

# form.save
可以保存一对一，一对多，多对多。注意：在多对多中如果使用了save（commit=save），还需执行form.save_m2m()

# 过滤器
{{ h2 | safe }} ‘|‘：这是一个模板过滤器，用于过滤变量值。

添加table标签可以使form表单换行

# jinjia标签
{% csrf_token %}    #跨域的令牌，解决跨域的问题，允许跨域，可以认为是jiajia的函数，必须有返回值

# 如何理解on_delete=models.CASCADE  
主外关系键中，级联删除，也就是当删除主表的数据时候从表中的数据也随着一起删除

# classmethod(function)
中文说明：
classmethod是用来指定一个类的方法为类方法，没有此参数指定的类的方法为实例方法，使用方法如下：
 
class C:
    @classmethod
    def f(cls, arg1, arg2, ...): ...

# 模板继承
这就是 {% extends "base.html" %} 的作用。它的含义是''先加载名为 base 的模板，并且用下面的标记块对模板中定义的标记块进行填充''。简而言之，模板继承可以使模板间的冗余内容最小化：每个模板只需包含与其它文档有区别的内容。

# STATIC_URL='/static/'     加载静态文件
STATICFILES_DIRS=[  
os.path.join(BASE_DIR,'static')
]  #加载静态文件，除了static文件还包括括号里面的
STATIC_ROOT="Users/yang/desktop/myblog/static" #部署服务器，静态文件整合后所有静态文件所在的文件夹
```

## 操作第三方表的方法：

- add()     添加
- remove()  移除
- projects.objects.set()      重置关系
- projects.objects.clear()    清除所有关系

### 查看Django的版本号：

```django
python -m django --version
```

### 项目 VS 应用

> 项目和应用有啥区别？应用是一个专门做某件事的网络应用程序——比如博客系统，或者公共记录的数据库，或者简单的投票程序。项目则是一个网站使用的配置和应用的集合。项目可以包含很多个应用。应用可以被很多个项目使用。

### 何时使用 [`include()`](https://docs.djangoproject.com/zh-hans/2.1/ref/urls/#django.urls.include)

> 当包括其它 URL 模式时你应该总是使用 `include()` ， `admin.site.urls` 是唯一例外。

## Model 的 `Meta` 选项

下面是在model中使用的 `class Meta` 内嵌类的所有 [元数据选项 (meta options)](https://django-chinese-docs-14.readthedocs.io/en/latest/topics/db/models.html#meta-options)

### 可用的 `Meta` 选项

#### `abstract`

- `Options.``abstract`

  如果 `abstract = True` ，这个 model 就是一个 [抽象基类](https://django-chinese-docs-14.readthedocs.io/en/latest/topics/db/models.html#abstract-base-classes) 。

#### `app_label`

- `Options.``app_label`

  如果一个 model 定义在默认的 `models.py` 之外 (例如，如果你的 app 的 models 在 `myapp.models` 子模块下)，你必须定义 app_label 让 Django 知道它属于哪一个 app`app_label = 'myapp' `

#### `db_table`

- `Options.``db_table`

  定义该 model 在数据中的表名称:`db_table = 'music_album' `

#### 数据库中的表名称

为了节省时间，Django 会自动的使用你的 model class 的名称和包含这个 model 的 app 名称来构建 数据库的表名称。一个 model 的数据库表名称是通过将 “app label” – 你在 [`manage.py startapp`](https://django-chinese-docs-14.readthedocs.io/en/latest/ref/django-admin.html#django-admin-startapp) 中使用的名称 – 和 model 的类名称，加上一个下划线在他们之间来构成。

例如，如果你有一个 app 叫做 `bookstore` (使用 `manage.py startapp bookstore` 创建)，以 及一个 model 定义为 `class Book` 这样将会创建一个名为 `bookstore_book` 的数据库表。

如果想自定义数据库的表名称，需要在 `class Meta` 使用 `db_table` 参数来自定义。

如果你的数据库表名称是一个SQL保留字，或者它包含不允许出现在 Python 变量中的字符 (比如连字 符)这是没问题的。这是因为 Django 会自动给列名和表名添加引号。

在 MySQL 中使用小写字母作为数据库表名称

强烈建议你在通过 `db_table` 重载数据库表名称时，使用小写字母，特别是当你在使用 MySQL 作为后台数据库时。查看 [MySQL notes](https://django-chinese-docs-14.readthedocs.io/en/latest/ref/databases.html#mysql-notes) 了解更多细节。

#### `db_tablespace`

- `Options.``db_tablespace`

  定义这个 model 所使用的 [数据库 表空间](https://django-chinese-docs-14.readthedocs.io/en/latest/topics/db/tablespaces.html) 。如果在项目的 setting 中定义了 [`DEFAULT_TABLESPACE`](https://django-chinese-docs-14.readthedocs.io/en/latest/ref/settings.html#std:setting-DEFAULT_TABLESPACE) 那么它会使用这个值。如果后台数据库不支持 表空间，这个选项会被忽略。

#### `get_latest_by`

- `Options.``get_latest_by`

  在 model 中指定一个 [`DateField`](https://django-chinese-docs-14.readthedocs.io/en/latest/ref/models/fields.html#django.db.models.DateField) 或者 [`DateTimeField`](https://django-chinese-docs-14.readthedocs.io/en/latest/ref/models/fields.html#django.db.models.DateTimeField) 。这个设置让你在使用 model 的 [`Manager`](https://django-chinese-docs-14.readthedocs.io/en/latest/topics/db/managers.html#django.db.models.Manager) 上的 `latest` 方法时，默认使用指定字段来排序。例如:`get_latest_by = "order_date" `详见 [`latest()`](https://django-chinese-docs-14.readthedocs.io/en/latest/ref/models/querysets.html#django.db.models.query.QuerySet.latest) 。

#### `managed`

- `Options.``managed`

  默认值为 `True` ，这意味着 Django 可以使用 [`syncdb`](https://django-chinese-docs-14.readthedocs.io/en/latest/ref/django-admin.html#django-admin-syncdb) 和 [`reset`](https://django-chinese-docs-14.readthedocs.io/en/latest/ref/django-admin.html#django-admin-reset) 命令 来创建或移除对应的数据库。换句话说， Django *管理* 了数据库的生命周期。如果设置为 `False` ，Django 将不会为当前 model 创建或者删除数据库表。 通常在表示某个 通过其他方法创建的现有数据表时这会非常有用。这是当 `managed=False` 时 *仅有* 的不同之 处。model 在处理所有其他方面的事情时是完全一致的。这包括如果没有声明主键字段，Django 将自动的为 model 增加一个自增的主键字段。当你使用不被* 管理* 的 models 时，为了避免让将来阅读代码的人迷惑，建议指明所有所有托管在 model 中的字 段与数据库表的关系。如果两个非托管的 models (`managed=False`) 之间，使用了 [`ManyToManyField`](https://django-chinese-docs-14.readthedocs.io/en/latest/ref/models/fields.html#django.db.models.ManyToManyField) 关联，就不会创建多对多关系的中间表。然而 如果是一个托管的 model 与另一个非托管的 model 的话，多对多关系 *将会* 被创建。如果你需要改变默认的行为，就的显示的定义中间 model 来在数据库中创建中间表(要将 `managed` 设置为 `True`)，然后在你的原 model 上使用 [`ManyToManyField.through`](https://django-chinese-docs-14.readthedocs.io/en/latest/ref/models/fields.html#django.db.models.ManyToManyField.through) 属性指向中间 model，就能实现自定义的多对多关系。如果你的测试中包含非托管 model (`managed=False`)，那么在测试之前，你应该要确保在测试 创建时已经创建了正确的数据表。如果你想更改 model 类中某个 Python 层级的行为，你 *可以* 令 `managed=False` ，然后创 建该 model 的拷贝，在拷贝中定义新的行为。不过在面对这种情况时还有个更好的办法就是使 用 [Proxy models](https://django-chinese-docs-14.readthedocs.io/en/latest/topics/db/models.html#proxy-models) 。

#### `order_with_respect_to`

- `Options.``order_with_respect_to`

  根据给定的字段对 model 排序。在关联关系中,它经常用在根据目标对象对源对象排序的场合。举 个例子，一个 `Answer` 只关联一个 `Question` 对象，而一个 question 对象却可以关联多 个 answer 对象。根据 question 对 answer 排序，你应该这么做:`class Answer(models.Model):     question = models.ForeignKey(Question)     # ...      class Meta:         order_with_respect_to = 'question' `当 `order_with_respect_to` 被设置时，会提供两个附加的方法用于获取和设置关联对象的排序：`get_RELATED_order()` 和 `set_RELATED_order()` ，这其中的 `RELATED` 是 model 的小 写名字。例如，假定一个 `Question` 对象关联到多个 `Answer` 对象，这将返回一个包含 `Answer` 对象主键的列表:`>>> question = Question.objects.get(id=1) >>> question.get_answer_order() [1, 2, 3] `可以通过传入一个 `Answer` 主键的列表的方式来设置 `Question` 对象关联的 `Answer` 对象的顺序:`>>> question.set_answer_order([3, 1, 2]) `关联的对象同样有两个方法, `get_next_in_order()` 和 `get_previous_in_order()` ， 可 以用来访问那些特定的对象。假定 `Answer` 对象是以 `id` 排序的:`>>> answer = Answer.objects.get(id=2) >>> answer.get_next_in_order() <Answer: 3> >>> answer.get_previous_in_order() <Answer: 1> `

改变 order_with_respect_to 时注意

`order_with_respect_to` 增加了一个名为 `_order` 的字段(数据库字段)，因此在你进 行 [`syncdb`](https://django-chinese-docs-14.readthedocs.io/en/latest/ref/django-admin.html#django-admin-syncdb) 操作后，如果你增加或者改变了 `order_with_respect_to` 请确保 处理得当。

#### `ordering`

- `Options.``ordering`

  定义了当获取对象的列表时，对象的默认排序:`ordering = ['-order_date'] `这是一个字符串的元组或列表。没一个字符串都是由一个字段名和一个可选的表明降序的 “-” 前缀构成。 当字段名前面没有 “-” 时，将默认使用升序排列。使用 ”?” 将会随机排列。例如，以 `pub_date` 字段升序排序，可用:`ordering = ['pub_date'] `以 `pub_date` 降序排列时，可用:`ordering = ['-pub_date'] `以 `pub_date` 降序排列，然后再以 `author` 升序排列，可用:`ordering = ['-pub_date', 'author'] `Django admin 将采用列表/元组中所有的元素; 在 1.4 版之前, 只有第一个元素被采用。

#### `permissions`

- `Options.``permissions`

  在创建对象时，添加到权限表当中的附加权限信息。Django 自动为每个设置了 `admin` 的对象创建了添 加，删除和修改的权限。下面这个例子展示了如何添加一个附加的权限 `can_deliver_pizzas`:`permissions = (("can_deliver_pizzas", "Can deliver pizzas"),) `该项可以是一个列表或一个由两个元组构成的元组，以这样的格式 `(permission_code, human_readable_permission_name)` 。

#### `proxy`

- `Options.``proxy`

  如果 `proxy = True` ，表示该 model 是其父类的代理 model [proxy model](https://django-chinese-docs-14.readthedocs.io/en/latest/topics/db/models.html#proxy-models) 。

#### `unique_together`

- `Options.``unique_together`

  用来设置的不重复的字段组合，必须唯一(将两个字段做联合唯一):`unique_together = (("driver", "restaurant"),) `它是一个字段名称的列表，列表内的字段组合在数据库中是唯一，不重复的，也就是说不可以有两 个对象，它们在列表中的字段值是完全相同的。它被用在 Django admin 后台，在数据库层级约束 数据。(比如，在 `CREATE TABLE` 语句中包含 `UNIQUE` 关键字)为了使用方便，你可以赋给该项一个单独的字段列表的元组:`unique_together = ("driver", "restaurant") `一个 [`ManyToManyField`](https://django-chinese-docs-14.readthedocs.io/en/latest/ref/models/fields.html#django.db.models.ManyToManyField) 不能包含在 `unique_together` 中。 (这 将会导致它看起来不明不白！) 如果你需要验证关联到[`ManyToManyField`](https://django-chinese-docs-14.readthedocs.io/en/latest/ref/models/fields.html#django.db.models.ManyToManyField) 字段的唯一性验证，尝试使用 signal(信号) 或者 明确指定 model 的 [`through`](https://django-chinese-docs-14.readthedocs.io/en/latest/ref/models/fields.html#django.db.models.ManyToManyField.through) 属性。

#### `verbose_name`

- `Options.``verbose_name`

  指明一个易于理解和表述的对象名称，单数形式:`verbose_name = "pizza" `如果这个值没有设置， Django 将会使用该 model 的类名的分词形式作为他的对象表述名: `CamelCase` 将会转换为 `camel case` 。

#### `verbose_name_plural`

- `Options.``verbose_name_plural`

  对象的复数表述名:`verbose_name_plural = "stories" `如果没有指定，Django 会使用 [`verbose_name`](https://django-chinese-docs-14.readthedocs.io/en/latest/ref/models/options.html#django.db.models.Options.verbose_name) + `"s"` 的形式作为对象的表述名。

## Django相关：

```
1. urls相关操作
from django.urls import path, re_path, include
from django.urls import reverse  // 注意reverse 和另一个reversed区别。前者要明确导入，后者是built-in内置不用导入；两者功能也不一。
2. HttpResponse生成
from django.shortcuts import render, Httpresponse, redirect
from django.http import JsonResponse // 响应一个content-type：text/json 返回一个json响应报文
3. 组件auth
from django.contrib import auth  //contrib 意味：构件
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
4. 组件forms
from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError  // django的异常定义都在django.core.exceptions模块中，该异常用于自定义钩子。
from django.forms import ModelForm  // 如果一个form的字段数据是被用映射到一个django models.那么一个ModelForm可以帮助你节约很多开发时间。因为它将构建一个form实例，连同构建适当的field和field attributes，利用这些构建信息，都来自一个Model class. 
from django.core.files.uploadedfile import SimpleUploadedFile

5. 邮件组件
from django.core.mail import send_mail

6. model组件
from django.db import models
from django.db.models import F, Q
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import transaction  # 利用model做数据库的事务操作

7. 分页器相关
from django.core import paginator

8. django admin site相关
from django.contrib import admin
from django.contrib.admin import ModelAdmin

9. view 相关
from django.view import View  # 用于media访问内置视图

10. 中间件
from django.utils.deprecation import MiddlewareMixin

11. template模版相关
from django import template  # 自定义tag和filter需要用到

12. 工具
from django.utils.module_loading import autodiscover_modules # 自动发现项目下所有注册app的指定模块并将其加载导入执行。
from django.utils.safestring import mark_safe # 由于django的模版引擎 出于安全原因，在生成html字符串时，会将与html相关的特殊字符进行转义。这时如果是我们后台自己要输出html字符，那么就需要提前将字符通过mark_safe处理一下，再用于模版解析中就不会出现 html标签也展示在页面上的情况了。
```