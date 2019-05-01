# 类和对象：

```py
class Play:
    name = "lj"   #类属性  静态变量   静态数据
    def __init__(self):  #初始化
        # self.name = "lk"   #实例属性
        pass
    def type(self):  #实例的方法
        print("司令")
    def ability(self):  #实例的方法
        print("指挥")

    @staticmethod
    def tell():
        print("这是tell方法")
    @staticmethod   #静态方法,属于类的方法，所以不能调用实例的属性和方法，但同时也不能调用类的属性和方法,也不能调用类的其他静态方法
    def say():
        print("这是say方法")

    @classmethod
    def say2(cls):
        print("这是say2方法")
    @classmethod    #类方法，不能调用实例的属性和方法,但是能调用类属性和方法,也能调用静态属性和方法

    def say1(cls):
        print("这是类方法")
        print(cls.name)
        cls.say2()
        cls.say()


p1 = Play()  # p1 实例
             # play 类
# p1.name = "lk"
# print("类属性：",Play.name)
# print("实例属性：",p1.name)
 
# Play.name = "小白"
# print("类属性：",Play.name)
# print("实例属性：",p1.name)
p2 = Play()


p1.say()
p2.say()

```

## 类方法.静态方法

> 两者都可以通过类或者实例来调用，特点都是不能够调用实例的属性和方法。
>
> 类属性和方法是类固有的方法与属性，不会因为实例不同而改变。

## 类内建属性：

```py
# 类的方法：
class Car:
    def __init__(self):
        """
        这是一个汽车类
        """
        self.pp = "大众"
    def run(self):
        print("运行")


print(Car.__name__) #类名   
print(Car.__doc__)  #对类的描述  
print(Car.__bases__)#所有的父类，返回一个元组
print(Car.__base__) #父类
print(Car.__dict__) #以字典的形式返回所有的方法 
print(Car.__module__) #返回类所在的模块 __main__ 
print(Car.__class__)  #类对应的类 <class type> 


```

## 特殊实例的方法：(魔法方法)

```py
# 魔法方法：
#1.__new__  “方法在Python中是真正的构造方法（创建并返回实例），通过这个方法可以产生一个”cls”对应的实例对象，所以说” __new__”方法一定要有返回，对于”2.__init__ “方法，是一个初始化的方法，“self”代表由类产生出来的实例对象，” __init__”将对这个对象进行相应的初始化操作
class Car:
    def __new__(cls):  #“__new__” 方法是在类实例化对象时第一个调用的方法，将返回实例对象，“__new__” 方法始终都是类方法（即第一个参数为cls），即使没有被加上装饰器
        """
        创建实例
        """
        return object.__new__(cls) #__new__至少有一个参数cls，代表要实例化的类，此参数在实例化时python自动提供
        #__new__必须要有返回值，返回出实例化的实例，这点在自己实现__new__时要特别注意，可以return父类__new__出来的实例
    def __init__(self):
        """
        初始化实例
        """
        self.pp = "大众"
    def run(self):
        print("运行")
        
    def __str__(self):
    		"""
    		作用：给实例一个描述
    		"""
    		return "这是一个汽车实例"
		def  __repr__(self):
				"""
    		作用：给实例一个描述
    		"""
    		return "这是一个汽车实例"
     def __del__(self):
     		"""
     		作用：实例被注销时调用
     		"""
     		print("实例被删除")
     def __dir__(self)   以列表形式返回实例属性和方法

c = Car()
c.run()

```



## 封装：

> 对内部数据进行保护(隐藏)，或合理的暴露
>
> Python中私有化的方法也比较简单，即在准备私有化的属性（包括方法、数据）名字前面加两个下划线即可。 
>
> 类中所有双下划线开头的名称如__x都会自动变形成：_类名__x的形式 

```py
class Car:
	def __init__(self):
		self.__name = "大众"
	def getname(self):
		return self.__name
	def setname(self,var):
		self.__name = var
c = Car()
c.__name = "宝马"

class A:
    __N=0 #类的数据属性就应该是共享的,但是语法上是可以把类的数据属性设置成私有的如__N,会变形为_A__N
    def __init__(self):
        self.__X=10 #变形为self._A__X
    def __foo(self): #变形为_A__foo
        print('from A')
    def bar(self):
        self.__foo() #只有在类内部才可以通过__foo的形式访问到.　
        
   1、这种机制也并没有真正意义上限制我们从外部直接访问属性，知道了类名和属性名就可以拼出名字：_类名__属
性，然后就可以访问了，如a._A__N
   2.变形的过程只在类的定义是发生一次,在定义后的赋值操作，不会变形
   3.在继承中，父类如果不想让子类覆盖自己的方法，可以将方法定义为私有的
```



## 继承和派生：

> 继承：目的是延续父元素的属性和方法     派生：在旧类的基础上添加新的功能 ，包括方法的重写。

> 基类  超类   父类             派生类  子类  

> 继承：直接或者间接继承object类，objects是一切类的基类（超类）父类  ，分为单继承和多继承。就近原则，深度优先  
>
> 派生： 在继承父类的基础上衍生出新的属性  

## 类内建函数：

- issubclass(sub,parent)   判断sub是否为parent的子类，返回bool

- isinstance(ins,class) 判断ins是否为class的实例，返回bool

- hasattr(obj,"attr")  判断obj中是否有attr属性，返回bool

- getattr(obj,"attr")  获取obj中attr属性

- setattr(obj,attr,value)  设置obj中attr属性

- delattr(obj,attr)  删除obj中attr属性

- dir() 列出类或实例的属性和方法，以列表的形式显示出来

- super()  寻找父类信息super(type[,object-or-type]),python3可以直接使用，python2 不可以

- python中的super( test, self).__init__()

  ```
  首先找到test的父类（比如是类A），然后把类test的对象self转换为类A的对象，然后“被转换”的类A对象调用自己的__init__函数
  ```

- super().xxx代替super(Class,self).xxx

- vars(object) 返回类或实例的属性，以字典的形式

  ```py
  class Myfloat(float):
      def __new__(cls,var):
          return float.__new__(cls,round(var,3))
      def __init__(self,num):
          self.num = num
      def get1(self):
          #return str(self.num)+"$"
          return "%0.2f%s/"%(self.num,type)
  num = Myfloat(4.5555)
  print(num.get1())
  ```


# 模式：

### 单例模式：实例只有一个

```py
class Person():
    __instance = None
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    def __init__(self):
        pass
def say(self):
    print(self.name)
 
p = Person()
p.name = "小艾"
print(p.name)
```



### 工厂模式：

   ```py
class Dz():
    def __init__(self):
        self.type = "大众"
    def run(self):
        print("启动")
    def stop(self):
        print("熄火")

class Bmw():
    def __init__(self):
        self.type = "宝马"
    def run(self):
        print("启动")
    def stop(self):
        print("熄火")




class Carfactory():
    def CreateCar(self,type):
        if type == "dz":
            obj = Dz()
        elif type == "BMW":
            obj = Bmw()
        return obj

cf = Carfactory()
car = cf.CreateCar('dz')
print(car,type)
car.run()
car.stop()
   ```

# 异常：

> 程序出现了错误而在正常控制流以外采取的行为。
>
> 异常发生两个阶段：1.发生异常   2.异常处理

```py
try:#标志的作用，如果try里面的内容出错，则执行except里面的内容
	print((1/0))
except(ZeroDivisionError,ValueError):  #捕获多个异常
	prite("出错")
except ValueError： #分支
	prite("ValueError")
	
except ValueError as e: #获取异常信息
	prite(e)
	
else:  #没有捕获到异常时，执行的模块
	print("没有错误")
	
finally：
	print("不管有没有异常，都执行的代码")
	
	
def A():    #异常的传递
	print(1/0)
def B():
	A()
def C():
	B()
try:
	C()
except:
	print("error")
	
```

```py
异常类.md

BaseException
 +-- SystemExit  解释器请求退出
 +-- KeyboardInterrupt  用户中断执行（ctr + c）
 +-- GeneratorExit   生成器发生异常来通知退出
 +-- Exception   常规错误基类
      +-- StopIteration 	迭代器没有更多的值
      +-- StopAsyncIteration
      +-- ArithmeticError   数值计算错误基类
      |    +-- FloatingPointError   浮点计算错误
      |    +-- OverflowError    数值运算超出最大限制
      |    +-- ZeroDivisionError    除(或取模)零 (所有数据类型)
      +-- AssertionError    断言语句失败
      +-- AttributeError    对象没有这个属性
      +-- BufferError   
      +-- EOFError  没有内建输入，到达EOF标记
      +-- ImportError   导入模块失败
      |    +-- ModuleNotFoundError
      +-- LookupError   无效数据查询基类
      |    +-- IndexError 序列中没有此索引(index)
      |    +-- KeyError 映射中没有这个键
      +-- MemoryError   内存溢出错误
      +-- NameError 未声明未初始化的本地变量
      |    +-- UnboundLocalError 	访问未初始化的本地变量
      +-- OSError   操作系统错误
      |    +-- BlockingIOError 操作阻塞设置为非阻塞操作的对象（例如套接字）时引发
      |    +-- ChildProcessError 子进程上的操作失败时引发
      |    +-- ConnectionError 连接相关的问题的基类
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError 尝试创建已存在的文件或目录时引发
      |    +-- FileNotFoundError    在请求文件或目录但不存在时引发
      |    +-- InterruptedError 系统调用被输入信号中断时触发
      |    +-- IsADirectoryError 在目录上请求文件操作时引发
      |    +-- NotADirectoryError 在对非目录的os.listdir()事物请求目录操作（例如）时引发
      |    +-- PermissionError 尝试在没有足够访问权限的情况下运行操作时引发 - 例如文件系统权限。
      |    +-- ProcessLookupError 当给定进程不存在时引发
      |    +-- TimeoutError 系统功能在系统级别超时时触发。
      +-- ReferenceError    弱引用(Weak reference)试图访问已经垃圾回收了的对象
      +-- RuntimeError  一般的运行时错误
      |    +-- NotImplementedError  	尚未实现的方法
      |    +-- RecursionError
      +-- SyntaxError 一般的解释器系统错误
      |    +-- IndentationError 缩进错误
      |         +-- TabError    Tab 和空格混用
      +-- SystemError Python 语法错误
      +-- TypeError     对类型无效的操作
      +-- ValueError    传入无效的参数
      |    +-- UnicodeError  Unicode 相关的错误
      |         +-- UnicodeDecodeError  	Unicode 解码时的错误
      |         +-- UnicodeEncodeError  Unicode 编码时错误
      |         +-- UnicodeTranslateError   Unicode 转换时错误
      +-- Warning   警告的基类
           +-- DeprecationWarning   关于被弃用的特征的警告
           +-- PendingDeprecationWarning    关于特性将会被废弃的警告
           +-- RuntimeWarning   可疑的运行时行为(runtime behavior)的警告
           +-- SyntaxWarning    可疑的语法的警告    
           +-- UserWarning  用户代码生成的警告
           +-- FutureWarning    关于构造将来语义会有改变的警告
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
```

### 总结：



1. except语句不是必须的，finally语句也不是必须的，但是二者必须要有一个，否则就没有try的意义。

2. Except语句可以有 多个，Python会按照except语句的顺序依次匹配你指定的异常，如果异常已经处理就不会进入后面的except语句。
3. Except语句可以以元组形式同时指定多个异常
4. Except语句后面如果不指定异常类型。 则默认捕获所有的异常，你可以通过logging或sys模块获取当前异常。
5. 如果要捕获异常后重复抛出请使用raise，后面不要带任何参数或信息
6. 不建议捕获并抛出同一个异常。

# 模块和包

## 模块：

> 模块就是一个py文件

## 包：

> 包就是一个文件夹，包含多个py文件，必须有\__init__py文件

## 引用方法：

### 构建模块的层级包：

> 模块和包是任何大型数据的核心，就连python安装程序本身也是一个包。

```py
import a,b
import bao1.a,bao1.b
from bao1 import a
from bao1 import a as a2  #相当于给a起了新的名字
from bao1.a import aa3,aa2
from bao1.a import * #一次性导入
__all__=['aa2','aa3']   
from .a import aa3  #使用相对路径导入子模块,一个点是在当前目录，两个点是退出当前目录，相对路径只能在子模块中使用。
```

### 控制模块全部导出：

> from moudle import *  从mouble模块中全部导出内容。在模块中定义变量\__all__,可以有效的控制被全部导入



### 使用相对路径导入包中子模块:

将代码组织成包，想用import语句从另一个包名没有编码过的包中导入子模块。使用包的相对导入，使一个模块导入同一个包的另一个模块。

```py
mypackage/
	__init__py
	A/
		__init__.py
		spam.py
		grok.py
	B/
		__init__.py
		br. 
```

- 如果要导入同目录下的模块grok，语句如下：

  ```py
  from .  import grok
  ```

- 如果要导入不同目录下的模块B bar,语句如下：

  ```py
  from ..B  import bar
  ```

### 将模块分为多个文件：

> 在包(package)中的\__init__模块中利用from .a import  A的方式将其他模块导入到\__init__这个模块中，这时它所在的包可以被认作一个模块，然后在主模块中利用from mypackage.con1.myclass import *导入使用。

分为三步：

1. mymodule目录来替换文件mymodule.py,这个目录下，创建以下文件：

   ```py
   mymodule/
   	__init__.py
   	a,py
   	b,py
   ```

2. 分别在a.py和b.py文件中插入一下代码：

   ```py
   # a.py
   class A:
   	def spam(self):
   		print("A.spam)
   # b.py
   class B:
   	def spam(self):
   		print("B.spam)
   ```

3. 最后在\__init__.py中，将两个文件粘合在一起：

   ```py
   from .a import A
   from .b import B
   ```

   

### 利用命名空间导入分散的代码：

> 这种工作机制被称为包命名空间，从本质上讲，包命名空间是一种特殊的封装设计，为合并不同的目录的代码到一个共同的命名空间.它是将两个不同的包目录合并在一起，可以导入spam.xbd和spam.xmd,并且他们能够工作。

```py
import sys
sys.path.extend([r"C:\Users\牛培楠\Desktop\python\xb",r"C:\Users\牛培楠\Desktop\python\xm"])
from spam import xbd,xmd
xbd.a()
xmd.a()

# 在目录里，有着共同的命名空间，在任何一个目录里面都没有__init__py文件。
import sys
print(sys.path)
可以在python 环境下使用sys.path.append(path)添加相关的路径，但在退出python环境后自己添加的路径就会自动消失！
```

### 重新加载模块：

> 重新加载先前加载,但修改了其源码的模块

```py
import spam
import imp
imp.reload(spam)  
```

### 运行目录或压缩文件：

> 如果应用程序有多个文件，可以把应用程序放进他自己的目录并添加一个\__main__.py文件。比如以下例子：

```py
myspplication/
	spam.py
	bar.py
	grok.py
	__main__.py
```

如果\__main__.py存在，可以简单的在顶级目录运行python解释器。

python.myapplication

解释器将执行\__main__.py文件作为主程序。

将代码打包成zip文件，这种技术同样适用。

### 读取位于包中的数据文件：

```py
mypackage/
	__init__.py
	somedate.dat
	spam.py
```



> 1.假设spam.py文件需要读取somedate.dat文件中的内容，可以用data = pkgutil.get_data(\__packge__,"mydate.dat")实现。     #字节
>
> 2.f = open("mypackage/mydate.dat","r")   con = f.read()   f.close()

### 通过字符串名导入模块：

> 如果想要导入一个模块，但是模块的名字在字符串里，逆像对字符串调用导入命令。使用importlib.import_mouble()函数来手动导入名字为字符串的一个模块或者包的一个模块。

> import_moudle知识简单的执行个import相同的步骤，但是返回生成的模块对象，你只需将其存储在一个变量，然后像正常的模块一样使用。如果你正在使用的包，import_moudle()也可用于相对导入，但是，你需要给他一个额外的参数。

```py
import importlib   #通过字符串创建模块
data = importlib.import_mouble("mydate.dat")
u = mod.urlopen("http://www.python.org")
print(aa,data)
```

## if \_\_name\__ == "\_\_main__":

```py
if __name__ == '__main__' 就相当于是 Python 模拟的程序入口。Python 本身并没有规定这么写，这只是一种编码习惯。由于模块之间相互引用，不同模块可能都有这样的定义，而入口程序只能有一个。到底哪个入口程序被选中，这取决于 __name__ 的值。

__name__ 是内置变量，用于表示当前模块的名字，同时还能反映一个包的结构

python 的 -m 参数用于将一个模块或者包作为一个脚本运行，而 __main__.py 文件则相当于是一个包的”入口程序“。
```



# GUI

### tkinter编程

#### tkinter里边的Tk方法

```py
import tkinter as tk
window=tk.Tk()       #创建窗口（顶层窗口）
window.title("我的窗口")   #设置窗口的title
window.geometry('600x300')   #设置窗口尺寸  中间为x,不是乘法
window.resizable(0,0)#重置尺寸的大小,分别是x轴和y轴（0和非0），非0的方向可以改变大小，0的方向不可改变大小，默认都为非0
window.mainloop()    #进行事件循环
```

### Label标签   文本标签

> Label 控件用以显示文字和图片. Label 通常被用来展示信息, 而非与用户交互. 
>
> Text文本组件用于显示和处理多行文本。在Tkinter的所有组件中，Text组件显得异常强大和灵活，它适用于处理多任务，虽然该组件的主要目的是显示多行文本，但它常常被用于作为简单的文本编辑器和网页浏览器使用。

l=tkinter.Label(window)

l['text']=""    文本

l['font']=("",20,'blod/italic')   设置字体样式，大小，加粗/倾斜

l['bg']=""   设置背景颜色      background

l['fg']=""    设置前景（字体）颜色      foreground

l['width']=    设置宽

l['height']=    设置高

l['anchor']='n'                   n北（north）/s南/w西/e东（east）/c居中/nw/ne/sw/se

l['image']  = tk.PhotoImage(file="文件路径.gif/png")

### Button  按钮标签

b=tk.Button(window)

b['activebackground']添加点击后的背景颜色

b['activeforeground']添加点击后的字体颜色

b['state']='disable/normal'   disable不可点击，normal可以点击

b['text']=   文本提示

```py
# 输入组件
# e = tk.Entry(window)
# e['selectbackground'] = "red"  #选中文字，的背景色
# e['selectforeground'] = "blue" #选中文字，的颜色
# e['show'] = ""   #默认不指定，指定对应的字符
#button
# def fn1():
#     val = e.get()
#     t.insert('insert',val)  #从任意位置插入

# b1 = tk.Button(window,text="insert",command=fn1)
# def fn():
#     val = e.get()
#     t.insert('end',val)      #从最后插入
 
# b2 = tk.Button(window,text="after",command=fn)
```



### Entry输入组件

e=tk.Entry(window)

e['state']='normal/disable'

e['show']=""     设置字体表现形式

e['selectbackground']="red"   添加字体选中背景颜色

e['selectforeground']="#fff"   添加字体选中的字体颜色

### 文本域组件  Text

t=tk.Text(window)

t.insert("end",con插入内容)  在末尾插入内容

t.insert("insert",con插入内容)   在选中位置插入内容  （不可以使用下标插入）  

```py
import tkinter as tk
window=tk.Tk()       #创建窗口
window.title("我的窗口")  #设置窗口的title
window.geometry('600x300')#设置窗口尺寸
window.resizable(0,0)#重置尺寸的大小,分别是x轴和y轴（0和非0），非0的方向可以改变大小，0的方向不可改变大小，默认都为非0

# str1=tk.StringVar()
#Label  标签 
img1=tk.PhotoImage(file="book1.png")
l1=tk.Label(window)   #实例化Label   第一个参数是主窗口  
#l1=tk.Label(window,text="hello world",font=("",20,"bold italic"))设置字体样式，字体样式，大小，加粗/倾斜
l1['text']="hello world"   #文本
l1['font']=("",20,"bold italic")   #设置字体，利用元组（字体样式，大小，加粗/倾斜）
l1['bg']='#ff6700'    #设置背景色
l1['fg']='#fff'   #前景色
l1['width']=20
l1['height']=1
l1['anchor']='c'       #n北/s南/w西/e东/c居中/nw/ne/sw/se
# l1['image']=img1   #引用图片



#Button  按钮标签
num=1
def aa():
    global num
    l1['text']="你好%d"%num
    num=num+1
def fn():
    val=e.get()  #获取e中输入组件的数据
    t.insert('end',val)   #在文本域组件t的末尾添加
def fn1():
    val=e.get()   #获取e中输入组件的数据
    t.insert('insert',val)   #在文本域组件t的选中位置添加
b1=tk.Button(window,text="点击",width=20,height=1,bg="#333",fg="#fff",command=aa)
b2=tk.Button(window,text="插入",width=20,height=1,bg="#333",fg="#fff",command=fn)
b3=tk.Button(window,text="insert",width=20,height=1,bg="#333",fg="#fff",command=fn1)
#输入组件
e=tk.Entry(window)
e['selectbackground']="red"  #选中文字，添加的背景色
e['selectforeground']="blue"  #选中文字，字体的颜色
e['show']="*"  #指定输入的样式
#文本域组件
t=tk.Text(window)
#相对布局
l1.pack()
b1.pack()
e.pack()
b2.pack()
b3.pack()
t.pack()
window.mainloop()    #进行事件循环
```

### 单选按钮   Radiobutton

```py
import tkinter as tk
window=tk.Tk()       #创建窗口
window.title("我的窗口")
window.geometry('600x400')


# l1=tk.Label(window,width=20,height=3,bg="blue",fg="#fff",font=("",20))

# v1=tk.Variable()  #设置可变的值  可变量
# v1.set("A")   #设置初值
# def fn():
#     con=v1.get()    #获取v1的值
#     l1['text']="你选择了%s"%con
# #  单选按钮
# r1=tk.Radiobutton(window,text="A",variable=v1,value="A",command=fn)  当选中时，value赋值给variable
# r2=tk.Radiobutton(window,text="B",variable=v1,value="B",command=fn)
# r3=tk.Radiobutton(window,text="C",variable=v1,value="C",command=fn)
# l1.pack()
# r1.pack()
# r2.pack()
# r3.pack()
v1=tk.Variable()
# v1.set("请输入数据")
v2=tk.Variable()
def fn1():
    con=e.get()
    print(con)
    if len(con)>10:
        return True
    else:
        return False
def fn3():
    con=v2.get()
    print(con)
    if len(con)>10:
        return True
    else:
        return False
def fn2():
    print("长度不够")
def fn4():
    print("22")
e=tk.Entry(window,width=40,textvariable=v1,validate="focusout",validatecommand=fn1,invalidcommand=fn2)#当
#validate focus获取焦点或失去焦点  focusin获取焦点  focusout失去焦点  key输入    引发validate事件后进行验证fn1,验证不对执行fn2
e1=tk.Entry(window,width=40,textvariable=v2,validate="focusout",validatecommand=fn3,invalidcommand=fn2)
b=tk.Button(window,text="登录",width=20,height=1,command=fn4)
e.pack()
e1.pack()
b.pack()
window.mainloop()
```

### 多选按钮Checkbutton

```py
import tkinter as tk
window=tk.Tk()
window.title("多选框")
window.geometry("600x400")

v1=tk.Variable()
v2=tk.Variable()
v1.set(0)
v2.set(0)
def fn():
    con1=int(v1.get())
    con2=int(v2.get())
    if con1==1 and con2==0:
        l['text']="我喜欢看电影"
    elif con1==0 and con2==1:
        l['text'] = "我喜欢敲代码"
    elif con1==1 and con2==1:
        l.config(text="都喜欢")
    else:
        l.config(text="都不喜欢")
l=tk.Label(window,width=60,height=3,bg="#333",fg="#fff",font=("",20))
l.pack()
c1=tk.Checkbutton(window,text="看电影",variable=v1,command=fn)   #多选按钮
c1.pack()
c1=tk.Checkbutton(window,text="看电影",variable=v2,command=fn)
c1.pack()

window.mainloop()
```

### 登录系统案列

```py
import tkinter as tk
window=tk.Tk()
window.title("登录系统")
window.geometry("600x400")

username,password=False,False

def fn1():
    con=len(en1.get())
    global username
    if con>=10:
        username=True
        l1['text']="成功"
        l1['background']="green"
        l1['foreground']='#fff'
        isOk(username,password)
        return True
    else:
        return False
def fn3():
    con=len(en2.get())
    global password
    if con>=10:
        password=True
        l2['text']="成功"
        l2['background']="green"
        l2['foreground']='#fff'
        isOk(username,password)
        return True
    else:
        return False

def fn2():
    l1['text']="长度不够10位"
    l1['background']="red"
    l1['foreground']='#fff'
def fn4():
    l2['text']="长度不够10位"
    l2['background']="red"
    l2['foreground']='#fff'

def isOk(username,password):
    if username==True and password==True:
        btn1['state']="normal"
    else:
        btn1['state']="disable"

def issuccess():
    u=en1.get()
    p=en2.get()
    if u=='1234567890' and p=='1234567890':
        l3=tk.Label(window)
        l3.place(x=100,y=150)
        l3['text']="登录成功"
        l3['bg']="green"
        l3['fg']="#fff"
        btn1['state']='disable'
    else:
        l3=tk.Label(window)
        l3.place(x=100,y=150)
        l3['text']="输入错误"
        l3['bg']="red"
        l3['fg']="#fff"
tk.Label(window,text="用户名:").place(x=40,y=40)

en1=tk.Entry(window,validate="focusout",validatecommand=fn1,invalidcommand=fn2)
en1.place(x=100,y=40)


l1=tk.Label(window)
l1.place(x=280,y=40)

tk.Label(window,text="密码:").place(x=40,y=80)


en2=tk.Entry(window,validate="focusout",validatecommand=fn3,invalidcommand=fn4)
en2.place(x=100,y=80)


l2=tk.Label(window)
l2.place(x=280,y=80)


btn1=tk.Button(window,text="登录",command=issuccess)
btn1.place(x=100,y=120)
btn1['state']='disable'
btn1['activebackground']="green"
btn1['activeforeground']="#fff"


btn2=tk.Button(window,text="注销")
btn2.place(x=200,y=120)
btn2['state']='normal'
btn2['activebackground']="red"
btn2['activeforeground']="#fff"






window.mainloop()
```



### 下拉列表Listbox

lx1=tk.Listbox(window)

lx1['selectmode']="extend"   设定多选模式

lx1.selection()   所选择选项对应的的当前下标，元组的形式返回

lx1.insert('end',con内容)   在末尾插入

lx1.insert(0,con)  可指定下标插入

```py
import tkinter as tk
window=tk.Tk()
window.title("登录系统")
window.geometry("600x400")


l=tk.Label(window,width=10,height=1,bg="#333",fg="#fff")
l.pack()
en=tk.Entry(window)
en.pack()
def fn():
    arr=lxl.curselection()   #index=lxl.curselection()   #所选择的当前下标，元组的形式返回
    con=en.get()
    if con=="":
        return
    elif len(arr)==0:
        lxl.insert('end',con)
    elif len(arr)==1:
        lxl.insert(arr[0]+1,con)
    else:
        num=1
        for item in range(0,len(arr)):
            lxl.insert(arr[item]+num,con)
            num=num+1
btn=tk.Button(window,text="插入",command=fn)
btn['activebackground']="green"
btn['activeforeground']="#fff"
btn.pack()
#下拉列表
lxl=tk.Listbox(window,selectmode="extended")   #selectmode="extended"多选模式
lxl.insert(0,"北京")     #可以指定下标插入
for item in ['上海','广州',"深圳"]:
    lxl.insert("end",item)                             


lxl.pack()
```

### scale  滑块

```py
import tkinter as tk
window=tk.Tk()
window.title("我的窗口")
window.geometry('600x400')
l1=tk.Label(window)
# l1['bg']='red'
l1['fg']='black'
l1.config({
    'text':"this is labal",
})
l1.pack()
def fn():
    con=s1.get()
    # print(type(con))
    if con>100:
        l1['bg']='red'
    else:
        l1['bg']='green'
    l1['text']='获取的温度是%s'%con
btn=tk.Button(window,text='查询',command=fn)
btn.pack()
e1=tk.Entry(window)
v1=tk.Variable()
v1.set('A')
r1=tk.Radiobutton(window,text='A',variable=v1,value='A')
r2=tk.Radiobutton(window,text='B',variable=v1,value='B')
r1.pack()
r2.pack()
#scale  滑块
def fn1(v):
    pass
s1=tk.Scale(window,command=fn1)#需要传参数，参数自动传送每一次滑动的数值
  #属性
s1.config({
    'orient':tk.HORIZONTAL,   #设置方向 水平方向
    'from_':50,   #设置数值变化范围   默认为0-100
    'to':200,
    'length':500,   #设置滑块长度
    'resolution':10,  #设置滑动的步进值
    'digits':4,   #设置数字的位数
    'tickinterval':50,   #间隔刻度提示  最小为步进值的一半
    'showvalue':1,   #bool 1 0   显示上方的值
    'label':'温度',     #添加滑块文字标签
    #command方法  需要传参数，参数自动传送每一次滑动的数值
})
   #方法
s1.set(150)   #设置默认初值
s1.get()     #获取值
s1.pack()
window.mainloop()
```

### Spinbox  数字框



```py
import tkinter as tk
window=tk.Tk()
window.title("我的窗口")
window.geometry('600x400')
l1=tk.Label(window)
# l1['bg']='red'
l1['fg']='black'
l1.config({
    'text':"this is labal",
})
l1.pack()
def fn1(v):
    # print(float(v))
    if float(v)>100:
        l1['bg']='red'
    else:
        l1['bg']='green'
    l1['text']='获取的温度是%s'%v
    sp1['value']=v
    sp1['value']=""
s1=tk.Scale(window,command=fn1)#需要传参数，参数自动传送每一次滑动的数值，文件执行会自动运行
  #属性
s1.config({
    'orient':tk.HORIZONTAL,   #设置方向 水平方向
    'from_':50,   #设置数值变化范围   默认为0-100
    'to':200,
    'length':500,   #设置滑块长度
    'resolution':1,  #设置滑动的步进值
    'digits':4,   #设置数字的位数
    'tickinterval':50,   #间隔刻度提示  最小为步进值的一半
    'showvalue':1,   #bool 1 0   显示上方的值
    'label':'温度',     #添加滑块文字标签
    #command方法  需要传参数，参数自动传送每一次滑动的数值
})
   #方法
s1.set(150)   #设置默认初值
s1.get()     #获取值
s1.pack()
#Spinbox  数字框
def fn2():    #不需要传参
    num=sp1.get()
    s1.set(num)
sp1=tk.Spinbox(window,command=fn2)
sp1.config({
    "from_":50,     #设定数值范围
    "to":200,
    'width':20,   #设置宽度，没有高度
    # 'value':50    #设置固定值,设为空字符串""就相当于删除了该属性
})
# sp1['values']=('北京','上海','广州')  不仅可以设置数字还可以设置文字  
sp1.get()   #获取值  没有sp1.set()  可以通过value可以设置固定值，设为空字符串""就相当于删除了该属性
sp1.pack()





window.mainloop()
```

### canvas画布

```py
import tkinter as tk
window=tk.Tk()
window.geometry('600x600')

#canvas  画布
can=tk.Canvas(window)
can.config({
    'width':500,
    'height':500,
    'bg':'#ccc'
})
#画图片
img1=tk.PhotoImage(file="book1.png",width=200,height=200)#设置图片的大小
cimg=can.create_image(0,0,image=img1)#图片位置
#画线
cline=can.create_line(0,0,200,200,fill='red')   #开始坐标，结束坐标，填充
#画扇形
carc=can.create_arc(200,200,300,300,extent=270,start=90,fill='blue') #旋转角度，开始旋转角度，填充
#画圆
coval=can.create_oval(300,300,350,350,fill='yellow')
#文本
ctext=can.create_text(50,50,text='Python',font=("",20))
#画多边形
cp=can.create_polygon(0,0,0,100,100,100,fill='green')#确定顶点位置
#画正方形
cr=can.create_rectangle(300,300,500,500,fill='pink')
can.pack()
def fn():
    can.move(coval,-50,-50)#移动方法
btn=tk.Button(window,text='click',command=fn)
btn.pack()

window.mainloop()
```

### Menu 菜单栏

- 首先创建菜单栏，并添加到window上

  ```py
  menubar=tk.Menu(window)#创建菜单栏
  window.configure(menu=menubar)#添加菜单栏
  ```

- 然后创建菜单项（一级菜单），并添加到菜单栏，命名（向谁添加就向谁Menu实例化）

  ```py
  menu1=tk.Menu(menubar,tearoff=False)#创建菜单项,一级菜单，tearroff取消默认可移动样式
  menubar.add_cascade(label='文件(F)',menu=menu1)
  ```

- 菜单项中包括功能和二级菜单

  - [ ] 添加功能

    ```py
    menu1.add_command(label='新建文件(N)',command=fn1)#添加菜单功能项
    fn1为对应功能函数
    ```

  - [ ] 添加二级菜单

    ```py
    向一级菜单Menu实例化，并添加到一级菜单中
    menu1_1=tk.Menu(menu1,tearoff=False)#创建二级菜单
    menu1.add_cascade(label='打开最近的文件(R)',menu=menu1_1)
    ```

- 以后步骤同上

```py
import tkinter as tk
window=tk.Tk()
window.geometry('600x600')
#Menu 菜单栏
menubar=tk.Menu(window)#创建菜单栏
menu1=tk.Menu(menubar,tearoff=False)#创建菜单项,一级菜单，tearroff取消默认可移动样式
def fn1():
    pass
menu1.add_command(label='新建文件(N)',command=fn1)#添加菜单功能项
menu1.add_command(label='新建窗口(W)')
menu1.add_separator()#设置分割线
menu1.add_separator()#一个下拉菜单的分割线
menu1.add_command(label='打开文件(O)')
menu1.add_command(label='打开文件夹(F)')
menu1.add_command(label='打开工作区(K)')
menu1_1=tk.Menu(menu1,tearoff=False)#创建二级菜单
menu1_1.add_command(label='重新打开已关闭的编辑器(R)')
menu1.add_cascade(label='打开最近的文件(R)',menu=menu1_1)
menu1.add_separator()
menu1.add_command(label='将文件添加到工作区(D)')
menu1.add_command(label='将工作区另存为..')
menu1.add_separator()
menu1.add_command(label='保存(S)')
menu1.add_command(label='另存为(A)...')
menu1.add_command(label='全部保存(L)')
menu1.add_separator()
menu1.add_command(label='自动保存(O)')
menu1.add_separator()
menu1_2=tk.Menu(menu1,tearoff=False)#创建二级菜单
menu1_2.add_command(label='设置(S)')
menu1_2.add_separator()
menu1_2.add_command(label='键盘快捷方式(K)')
menu1_2.add_command(label='按键映射扩展(K)')
menu1_2.add_separator()
menu1_2.add_command(label='用户代码片段(S)')
menu1.add_cascade(label='首选项(P)',menu=menu1_2)
menu1.add_separator()
menu1.add_command(label='还原文件(V)')



menubar.add_cascade(label='文件(F)',menu=menu1)

window.configure(menu=menubar)#添加菜单栏

#菜单单选功能   语言选项
yuyan=tk.Variable()
yuyan.set(0)
def fn1():
    print(yuyan.get())
menu1_3=tk.Menu(menu1)
menu1.add_cascade(label='选择语言',menu=menu1_3)
menu1_3.add_radiobutton(label='英语',variable=yuyan,value=0,command=fn1)
menu1_3.add_radiobutton(label='中文',variable=yuyan,value=1,command=fn1)
menu1_3.add_radiobutton(label='俄语',variable=yuyan,value=2,command=fn1)
#菜单选项添加图片
img1=tk.PhotoImage(file="book1.png",width=50,height=50)
menu1_4=tk.Menu(menu1)
menu1_4.add_command(label="图片",image=img1,compound='left')
menu1.add_cascade(label='图片',menu=menu1_4)
#菜单多选功能
s1=tk.Variable()
s2=tk.Variable()
s3=tk.Variable()
tkinter 里的每个构件的variable属性不一样,如对于复选框Checkbutton来说,variable的值为1或0,代表着选中或不选中;对于单选框来说,variable与value相配套,当variable==value时代表该框选中。
s1.set(0)
s2.set(0)
s2.set(0)
def fn2():
    print(s1.get())
    print(s2.get())
    print(s3.get())
menu1_5=tk.Menu(menu1,tearoff=False)
menu1_5.add_checkbutton(label='加粗',variable=s1,command=fn2)
menu1_5.add_checkbutton(label='倾斜',variable=s2,command=fn2)
menu1_5.add_checkbutton(label='下划线',variable=s3,command=fn2)
menu1.add_cascade(label='字体',menu=menu1_5)


window.mainloop()
```

菜单点击事件

```py
import tkinter as tk
window=tk.Tk()
window.geometry('600x600')
menubar=tk.Menu(window,tearoff=False)
for item in ['css','html','javasript','python']:
    menubar.add_command(label=item)

def click(e):
    menubar.post(e.x_root,e.y_root)   #定位  返回点击的位置
window.bind('<Button-1>',click)  #<Button-3>右击事件  <Button-1>左击事件   <Button-2>滚轮事件


window.mainloop()
```

### frame框标签

```py
import tkinter as tk
window=tk.Tk()
window.geometry('600x600')
#frame框标签，相当于div
f1=tk.Frame(window,width=200,height=200,bg='red')
f1.pack(side='left')   #pack相对定位，side指定上下左右，实现横排排列
# f2=tk.Frame(f1,width=100,height=100,bg='blue')  #框的嵌套
# f2.pack()
f2=tk.Frame(window,width=100,height=100,bg='blue')  #框的嵌套
f2.pack(side='right')

# l1=tk.Label(f1,text='this is l1')
# l1.pack()
window.mainloop()
```

### 布局

#### 布局管理器：

> 第三种布局管理器是Gnd，可以基于网络坐标，使用Gnd来指定GUI控件的位置，Gnd会在他们的网络位置上渲染GUI应用中的每个对象。

> Packer ,这个命名时分恰当，因为他会把控件填充到正确的位置（即指定的父控件中），然后对于之后的每个控件，会去寻找剩余的空间进行填充。

#### 事件驱动处理：

> 事件可以包括按钮按下或释放，鼠标移动，敲击回车键等，一个GUI应用从开始到结束就是通过整套事件体系来驱动的，这种方式成为事件驱动处理。

#### 窗口和控件：

> 在GUI编程中，顶层的跟窗口对象包含组成GUI应用所有的小窗口对象，他们可能是文字标签，按钮，列表框等，这些独立的GUI组件称为控件，所以当我们说创建一个顶层窗口时，只是表示需要一个地方来摆放所有的控件。在python中，都会写成如下语句：top = Tkinter.Tk()

#### Tkinter编程的步骤：

- 导入tkinter模块
- 创建一个顶层对象，容纳整个GUI应用
- 在顶层窗口之上（或者“其中”），构建所有GUI组件（及其功能）
- 通过底层的应用代码将这些GUI组件连接
- 进入主事件循环。

#### 相对布局pack：

组建的位置和大小会随着窗口的大小的改变而改变

pack(side='left/top/bottom/right/tk.TOP/tk.BOTTOM/tk.LEFT/tk.RIGHT')   对齐方式

pack(anchor='n')    n北/s南/w西/e东/c居中/nw/ne/sw/se 位置，当剩余空间远远大于所需空间

pack(fill=tk.X/tk.Y/X/Y)   填充，横向填充/纵向填充

pack(expand=0/1)  扩充、展开      0为不将剩余空间扩展   1为将剩余空间扩展

pack(padx=10，pady=10）(外间距)

pack(ipadx=10,ipady=10)(内间距)   

b2.pack_forget()   将b2隐藏，想再次出现，重写创建步骤

```py
# l1=tk.Label(window,bg='blue')
# l1.pack(fill='x')
# btn=tk.Button(l1,text='class')
# btn.pack(side='left',expand=1,fill='x')
# btn1=tk.Button(l1,text='class')
# btn1.pack(side='left',expand=1,fill='x')
```



#### 绝对布局place：

组建的位置和大小不会随着窗口的大小的改变而改变

```py
f1=tk.Frame(window,width=200,height=200,bg='red')
f1.place(x=100,y=100)#x/y   相对于父元素的x轴偏移量，y轴偏移量
                    #relx/rely=[0-1]  参照于父元素的x y
                    #width/height  指定容器的宽和高
                    #relwidth/relheight=[0-1]  参照于父元素的宽高（父元素的多少倍）
f2=tk.Frame(f1,bg='blue',width=100,height=100)
f2.place(relwidth=0.5,relheight=0.5)
f2.place_forget() #隐藏
```



#### 网格布局grid：

通过表格的形式进行布局

```py
btn1=tk.Button(window,width=6,height=6,text='click1')
btn2=tk.Button(window,width=6,height=6,text='click2')
btn3=tk.Button(window,width=6,height=6,text='click3')
btn4=tk.Button(window,width=6,height=6,text='click4')
btn1.grid(row=0,column=0,padx=10,pady=10)
btn2.grid(row=0,column=1,padx=10,pady=10)
btn3.grid(row=1,column=0,padx=10,pady=10)
btn4.grid(row=1,column=1,padx=10,pady=10,columnspan=2)   #横跨两列
#row/column  指定行列位置
#columnspan  横跨列数  rowspan  行跨行数
# 用 row 表示行，用 column 表示列，其中值得注意的是 row 和 column 的编号都从 0 开始。
# grid 函数还有个 sticky 参数，它可以用 N， E， S， W 表示上右下左，它决定了组件在表格的对齐方式，九个方位
# ipadx：设置控件里面水平方向空白区域大小； ipady：设置控件里面垂直方向空白区域大小；
# padx：设置控件周围水平方向空白区域保留大小； pady：设置控件周围垂直方向空白区域保留大小；
```

#### 注意：

> 注意这三种布局管理在同一个 master window 里一定不可以混用! 
>
>  \# self.quit() #主窗口关闭
>
> ​        self.destroy()  #顶层窗口关闭 
>
> Toplevel（顶级窗口）组件类似于Frame组件，但Toplevel组件是一个独立的顶级窗口，这种窗口通常拥有标题栏、边框等部件，和Tk()创建出来的根窗口是一样的，共享着一样的方法。 

## messagebox:

> 介绍：messagebox是tkinter中的消息框。对话框
>
> 使用：
>
> - 导入模块：imoort tkinter.messagebox or
>
>   from tkinter import messagebox
>
> - 选择消息框的模式。

## filedialog:

> 介绍：filedialog是tkinter的文件对话框
>
> 使用：
>
> - 导入模块：import tkinter.filedialog
>
> or  from tkinter import filedialog
>
> - 选择文件对话框的内容

## super:

> super( test, self).__init__()
>
> ```
> 首先找到test的父类（比如是类A），然后把类test的对象self转换为类A的对象，然后“被转换”的类A对象调用自己的__init__函数
> ```

## tkinter总结：

```py
Tkinter 控件详细介绍

1.Button 按钮。类似标签,但提供额外的功能,例如鼠标掠过、按下、释放以及键盘操作/事件
2.Canvas 画布。提供绘图功能(直线、椭圆、多边形、矩形) ;可以包含图形或位图
3.Checkbutton 选择按钮。一组方框,可以选择其中的任意个(类似 HTML 中的 checkbox)
4.Entry 文本框。单行文字域,用来收集键盘输入(类似 HTML 中的 text)
5.Frame 框架。包含其他组件的纯容器
6.Label 标签。用来显示文字或图片
7.Listbox 列表框。一个选项列表,用户可以从中选择
8.Menu 菜单。点下菜单按钮后弹出的一个选项列表,用户可以从中选择
9.Menubutton 菜单按钮。用来包含菜单的组件(有下拉式、层叠式等等)
10.Message 消息框。类似于标签,但可以显示多行文本
11.Radiobutton 单选按钮。一组按钮,其中只有一个可被“按下” (类似 HTML 中的 radio)
12.Scale 进度条。线性“滑块”组件,可设定起始值和结束值,会显示当前位置的精确值
13.Scrollbar 滚动条。对其支持的组件(文本域、画布、列表框、文本框)提供滚动功能
14.Text 文本域。 多行文字区域,可用来收集(或显示)用户输入的文字(类似 HTML 中的 textarea)
15.Toplevel 顶级。类似框架,但提供一个独立的窗口容器。

Tkinter支持15个核心的窗口部件，这个15个核心窗口部件类列表如下：
窗口部件及说明：
Button：
一个简单的按钮，用来执行一个命令或别的操作。

Canvas：
组织图形。这个部件可以用来绘制图表和图，创建图形编辑器，实现定制窗口部件。

Checkbutton：
代表一个变量，它有两个不同的值。点击这个按钮将会在这两个值间切换。

Entry：
文本输入域。

Frame：
一个容器窗口部件。帧可以有边框和背景，当创建一个应用程序或dialog(对话）版面时，帧被用来组织其它的窗口部件。

Label：
显示一个文本或图象。

Listbox：
显示供选方案的一个列表。listbox能够被配置来得到radiobutton或checklist的行为。

Menu：
菜单条。用来实现下拉和弹出式菜单。

Menubutton：
菜单按钮。用来实现下拉式菜单。

Message：
显示一文本。类似label窗口部件，但是能够自动地调整文本到给定的宽度或比率。

Radiobutton：
代表一个变量，它可以有多个值中的一个。点击它将为这个变量设置值，并且清除与这同一变量相关的其它radiobutton。

Scale：
允许你通过滑块来设置一数字值。

Scrollbar：
为配合使用canvas, entry, listbox, and text窗口部件的标准滚动条。

Text：
格式化文本显示。允许你用不同的样式和属性来显示和编辑文本。同时支持内嵌图象和窗口。

Toplevel：
一个容器窗口部件，作为一个单独的、最上面的窗口显示。

注意在Tkinter中窗口部件类没有分级；所有的窗口部件类在树中都是兄弟。

所有这些窗口部件提供了Misc和几何管理方法、配置管理方法和部件自己定义的另外的方法。此外，Toplevel类也提供窗口管理接口。这意味一个典型的窗口部件类提供了大约150种方法。

Button窗口部件

Button（按钮）窗口部件是一个标准的Tkinter窗口部件，用来实现各种按钮。按钮能够包含文本或图象，并且你能够将按钮与一个Python函数或方法相关联。当这个按钮被按下时，Tkinter自动调用相关联的函数或方法。

按钮仅能显示一种字体，但是这个文本可以跨行。另外，这个文本中的一个字母可以有下划线，例如标明一个快捷键。默认情况，Tab键用于将焦点移动到一个按钮部件。

一、那么什么时候用按钮部件呢？

简而言之，按钮部件用来让用户说“马上给我执行这个任务”，通常我们用显示在按钮上的文本或图象来提示。按钮通常用在工具条中或应用程序窗口中，并且用来接收或忽略输入在对话框中的数据。

关于按钮和输入的数据的配合，可以参看Checkbutton和Radiobutton部件。

二、样式

普通的按钮很容易被创建，仅仅指定按钮的内容（文本、位图、图象）和一个当按钮被按下时的回调函数即可：
b = Button(master, text="OK", command=self.ok)

没有回调函数的按钮是没有用的，当你按下这个按钮时它什么也不做。你可能在开发一个应用程序的时候想实现这种按钮，比如为了不干扰你的beta版的测试者：
b = Button(master, text="Help", state=DISABLED)

如 果你没有指定尺寸，按钮的大小将正好能够容纳它的内容。你可以用padx和pady选项来增加内容与按钮边框的间距。你也可以用height和width 选项来显式地设置按钮的尺寸。如果你在按钮中显示文本，那么这些选项将以文本的单位为定义按钮的尺寸。如果你替而代之显示图象，那么按钮的尺寸将是象素 （或其它的屏幕单位）。你实际上甚至能够用象素单位来定义文本按钮的尺寸，但这可能带来意外的结果。下面是指定尺寸的一段例子代码：
f = Frame(master, height=32, width=32)
f.pack_propagate(0) # don't shrink
b = Button(f, text="Sure!")
b.pack(fill=BOTH, expand=1)

按钮能够显示多行文本（但只能用一种字体）。 你可以使用多行或wraplength选项来使按钮自己调整文本。当调整文本时，使用anchor,justify,也可加上padx选项来得到你所希望的格式。一个例子如下：
b = Button(master, text=longtext, anchor=W, justify=LEFT, padx=2)

为了使一个普通的按钮看起来像凹入的，例如你想去实现某种类型的工具框，你可简单地将relief的值从"RAISED"改变为"SUNKEN：
b.config(relief=SUNKEN)

你也可能想改变背景。注意：一个大概更好的解决方案是使用一个Checkbutton或Radiobutton其indicatoron选项的值设置为false：
b = Checkbutton(master, image=bold, variable=var, indicatoron=0)

三、方法

Button窗口部件支持标准的Tkinter窗口部件接口，加上下面的方法：

flash()：频繁重画按钮，使其在活动和普通样式下切换。

invoke() ：调用与按钮相关联的命令。

下面的方法与你实现自己的按钮绑定有关：

tkButtonDown(), tkButtonEnter(), tkButtonInvoke(), tkButtonLeave(), tkButtonUp() 
这些方法可以用在定制事件绑定中，所有这些方法接收0个或多个形参。

四、选项

Button窗口部件支持下面的选项：

activebackground, activeforeground
类型：颜色；
说明：当按钮被激活时所使用的颜色。

anchor
类型：常量；
说明：控制按钮上内容的位置。使用N, NE, E, SE, S, SW, W, NW, or CENTER这些值之一。默认值是CENTER。

background (bg), foreground (fg)
类型：颜色；
说明：按钮的颜色。默认值与特定平台相关。

bitmap
类型：位图；
说 明：显示在窗口部件中的位图。如果image选项被指定了，则这个选项被忽略。下面的位图在所有平台上都有 效：error, gray75, gray50, gray25, gray12, hourglass, info, questhead, question, 和 warning.
Tkinter类之窗口部件类
这 后面附加的位图仅在Macintosh上有 效：document, stationery, edition, application, accessory, folder, pfolder, trash, floppy, ramdisk, cdrom, preferences, querydoc, stop, note, 和 caution.

你也可以从一个XBM文件中装载位图。只需要在XBM文件名前加一个前缀@,例如"@sample.xbm"。

borderwidth (bd)
类型：整数；
说明：按钮边框的宽度。默认值与特定平台相关。但通常是1或2象素。

command
类型：回调；
说明：当按钮被按下时所调用的一个函数或方法。所回调的可以是一个函数、方法或别的可调用的Python对象。

cursor
类型：光标；
说明：当鼠标移动到按钮上时所显示的光标。

default
类型：常量；
说明：如果设置了，则按钮为默认按钮。注意这个语法在Tk 8.0b2中已改变。

disabledforeground
类型：颜色；
说明：当按钮无效时的颜色。

font
类型：字体；
说明：按钮所使用的字体。按钮只能包含一种字体的文本。

highlightbackground, highlightcolor
类型：颜色；
说明：控制焦点所在的高亮边框的颜色。当窗口部件获得焦点的时候，边框为highlightcolor所指定的颜色。否则边框为highlightbackground所指定的颜色。默认值由系统所定。

highlightthickness
类型：距离；
说明：控制焦点所在的高亮边框的宽度。默认值通常是1或2象素。

image
类型：图象；
说明：在部件中显示的图象。如果指定，则text和bitmap选项将被忽略。

justify
类型：常量；
说明：定义多行文本如何对齐。可取值有：LEFT, RIGHT, 或 CENTER。

padx, pady
类型：距离；
说明：指定文本或图象与按钮边框的间距。

relief
类型：常量；
说明：边框的装饰。通常按钮按下时是凹陷的，否则凸起。另外的可能取值有GROOVE, RIDGE, 和 FLAT。

state
类型：常量；
说明：按钮的状态：NORMAL, ACTIVE 或 DISABLED。默认值为NORMAL。

takefocus
类型：标志；
说明：表明用户可以Tab键来将焦点移到这个按钮上。默认值是一个空字符串，意思是如果按钮有按键绑定的话，它可以通过所绑定的按键来获得焦点。

text
类型：字符串；
说明：显示在按钮中的文本。文本可以是多行。如果bitmaps或image选项被使用，则text选项被忽略。

textvariable
类型：变量；
说明：与按钮相关的Tk变量（通常是一个字符串变量）。如果这个变量的值改变，那么按钮上的文本相应更新。

underline
类型：整数；
说明：在文本标签中哪个字符加下划线。默认值为-1，意思是没有字符加下划线。

width, height
类型：距离；
说明：按钮的尺寸。如果按钮显示文本，尺寸使用文本的单位。如果按钮显示图象，尺寸以象素为单位（或屏幕的单位）。如果尺寸没指定，它将根据按钮的内容来计算。

wraplength
类型：距离；
说明：确定一个按钮的文本何时调整为多行。它以屏幕的单位为单位。默认不调整。

Mixins

Tkinter模块提供了相应于Tk中的各种窗口部件类型的类和一定数量的mixin和别的帮助类（mixin是一个类，被设计来使用多态继承与其它的类结合）。当你使用Tkinter时，你不将直接访问mixin类。

一、实施mixins

通过root窗口和窗口部件类，Misc类被用作mixin。它提供了大量的Tk和窗口相关服务，这些服务对所有Tkinter核心窗口部件者有效。这些通过委托完成；窗口部件仅仅直接请求适当的内部对象。

Wm类通过root窗口和顶级窗口部件类被用作mixin。通过委托它提供了窗口管理服务。

使用委托像这样简化你的应用程序代码：一旦你有一窗口部件，你能够使用这个窗口部件的实例的方法访问Tkinter的所有部份。

二、Geometry(几何学)与mixins

Grid,Pack,Place这些类通过窗口部件类被用作mixins。通过委托，它们也提供了访问不同几何管理的支持。
下面是Geometry Mixins的列表及说明：
管理器及说明：

Grid：grid几何管理器允许你通过在一个二维网格中组织窗口部件来创建一个类似表的版面。
Pack：pack几何管理器通过在一个帧中把窗口部件包装到一个父部件中来创建一个版面。为了对窗口部件使用这个几何管理器，我们在这个窗口部件上使用pack方法来集成。
Place：place几何管理器让你显式将一个窗口部件放到给定的位置。要使用这个几何管理器，需使用place方法。

三、窗口部件配置管理
Widget类使用 geometry mixins来混合Misc类，并通过cget和configure方法来增加配置管理，也可以通过一个局部的字典接口。

窗口部件的配置

要配置一个窗口部件的外观，你用选项比使用方法调用好。典型的选项包括text、color、size、command等等。对于处理选项，所有的核心窗口部件执行同样的配置接口：

配置接口

widgetclass(master, option=value, ...) => widget 
说明：
创 建这个窗口部件的一个实例，这个实例作为给定的master的孩子，并且使用给定的选项。所有的选项都有默认值，因此在简单的情况下，你仅需要指定这个 master。如果你想的话，你也可以不指定master；Tkinter这时会使用最近创建的root窗口作为master。注意这个name选项仅能 在窗口部件被创建时设置。

cget(option) => string 
说明：
返回一个选项的当前值。选项的名字和返回值都是字符串。要得到name选项，使用str(widget)代替。

configure(option=value, ...), config(option=value, ...) 
说明：
设置一个或多个选项（作为关键字参数给定）。
注意一些选项的名字与Python中的保留字相同(class,from等)。要使用这些作为关键字参数，仅需要在这些选项名后添加一下划线(class_,from_)。注意你不能用此方法来设置name选项；name选项只能在窗口部件被创建时设置。

为了方便起见，窗口部件也实现一个局部的字典接口。 __setitem__ 方法映射configure，而__getitem__方法映射cget。你可以使用下面的语法来设置和查询选项：
value = widget[option]
widget[option] = value
注意每个赋值都导致一个对Tk的调用。如果你希望去改变多个选项，单独地调用(config或configure)去改变它们是一个好的主意。

这下面的字典方法也适用于窗口部件：
keys() => list 
说明：
返回窗口部件中所有可以被设置的选项的一个列表。name选项不包括在这个列表中（它不能通过字典接口被查询或修改）。

向后兼容性

关键字参数在Python1.3时被引入。之前，使用原始的Python字典将选项传递给窗口构造器和configure方法。原代码类似如下：
self.button = Button(frame, {"text": "QUIT", "fg": "red", "command": frame.quit})
self.button.pack({"side": LEFT})

关键字参数语法更优雅和少容易发生错误。但是为了与存在的代码兼容，Tkinter仍支持老的语法。在新的程序中你不应再用老的语法，即使是在某些情况下是很有吸引力的。例如，如果你创建了一个定制的窗口部件，它需要沿它的父类传递配置选项，你的代码可能如下：
def __init__(self, master, **kw):
Canvas.__init__(self, master, kw) # kw 是一个字典
上面的代码在当前版本的Tkinter下工作的很好，但是它在将来的版本下可能不工作。一个通常的办法是使用apply函数：
def __init__(self, master, **kw):
apply(Canvas.__init__, (self, master), kw)
这个apply函数使用了一个函数（一个未约束的方法），一个带参数的元组（它必须包括self，因为我们调用一个未约束的方法），一个可选的，提供了关键字参数的字典。

窗口部件的样式之颜色

所有的Tkinter标准窗口部件提供了一套样式设置选项，这让你可以去修改这些窗口部件的外观如颜色、字体和其它的可视外观。

颜色

大部份窗口部件都允许你指定窗口部件和文本的颜色，这可以使用background和foreground选项。要指定颜色，你可以使用颜色名，也可以使用红、绿、蓝颜色组合。

1、颜色名
Tkinter 包括一个颜色数据库，它将颜色名映射到相应的RGB值。这个数据库包括了通常的名称如Red, Green, Blue, Yellow, 和 LightBlue，也可使用外来的如Moccasin，PeachPuff等等。在X window系统上，颜色名由X server定义。你能够找到 一个名为xrgb.txt的文件，它包含了一个由颜色名和相应RGB值组成的列表。在Windows和Macintosh系统上，颜色名表内建于Tk中。

在Windows下，你可以使用Windows系统颜色（用户可以通过控制面板来改变这些颜色）：
SystemActiveBorder, SystemActiveCaption, SystemAppWorkspace, SystemBackground, 
SystemButtonFace, SystemButtonHighlight, SystemButtonShadow, SystemButtonText, 
SystemCaptionText, SystemDisabledText, SystemHighlight, SystemHighlightText, 
SystemInactiveBorder, SystemInactiveCaption, SystemInactiveCaptionText, SystemMenu, 
SystemMenuText, SystemScrollbar, SystemWindow, SystemWindowFrame, SystemWindowText。

在Macintosh上，下面的系统颜色是有效的：
SystemButtonFace, SystemButtonFrame, SystemButtonText, SystemHighlight, SystemHighlightText, SystemMenu, SystemMenuActive, SystemMenuActiveText, SystemMenuDisabled, SystemMenuText, SystemWindowBody。

颜色名是大小写不敏感的。许多颜色名词与词之间有无格都有效。例如"lightblue", "light blue", 和 
"Light Blue"都是同一颜色。

2、RGB格式

如果你需要显式地指定颜色名，你可以使用如下格式的字符串：
#RRGGBB
RR, GG, BB 分别是red,green和blue值的十六进制表示。下面的例子演示了如何将一个颜色三元组转换为

一个Tk颜色格式：
tk_rgb = "#%02x%02x%02x" % (128, 192, 200)

Tk也支持用形如"#RGB"和"rrrrggggbbbb"去分别指定16和65536程度之间的值。

你可以使用窗口部件的winfo_rgb方法来将一个代表颜色的字符串（名字或RGB格式）转换为一个三元组：
rgb = widget.winfo_rgb("red")
red, green, blue = rgb[0]/256, rgb[1]/256, rgb[2]/256
注意winfo_rgb返回16位的RGB值，范围在0~65535之间。要将它们映射到更通用的0~255范围内，你必须将每个值都除以256（或将它们向右移8位）。

窗口部件的样式之字体

字体
窗口部件允许你显示文本和指定所使用的字体。所有的窗口部件都提供了合理的默认值，你很少需要去为简单元素如标签和按钮指定字体。

字体通常使用font窗口部件选项指定。Tkinter支持一定数量的不同字体描述类型：
* Font descriptors

* User-defined font names

* System fonts

* X font descriptors

Tk8.0以前的版本仅X font描述被支持。

1、字体描述
从Tk8.0开始，Tkinter支持独立于平台的字体描述。你可以使用元组来指定一个字体，这个元组包含了一个字体类型名字，一个以磅为单位的高度，代表一个或多个样式的字符串。例如：
("Times", 10, "bold")
("Helvetica", 10, "bold italic")
("Symbol", 8)

要得到默认的尺寸和类型，你可以给出作为单一字符串的字体名。如果这个字体类型名字没有包括空格，你也可以给这个字符串自身增加尺寸和样式：
"Times 10 bold"
"Helvetica 10 bold italic"
"Symbol 8"

在大部份Windows平台上存在如下有效的字体类名：
Arial (相 应 于 Helvetica), Courier New (Courier), Comic Sans MS, Fixedsys, MS Sans Serif, MS Serif, Symbol, System, Times New Roman (Times), 和 Verdana：
Tkinter类之窗口部件类

注意：如果这个字体类型名包含空格，你必须使用上面所描述的元组语法。

有效的样式有normal, bold, roman, italic, underline, and overstrike。

Tk8.0自动映射Courier, Helvetica, 和Times到所有平台上相应的本地字体类型名。此外，在Tk8.0下字体格式不会引起问题，如果Tk不能找出确切的匹配，它会试着找类似的字体，如果失败，Tk就使用特定平台的默认字体。

Tk4.2在Windows下同样支持这种字体描述。这儿有几个限制，包括字体类型名必须在平台上存在，并非这所有上面样式名都存在（或它们中的一些有不同的名字）。

2、字体名
此外，Tk8.0允许你去创建已命名的字体并且当为一个窗口部件指定字体时使用它们的名字。

tkFont模块提供一个Font类，这个类允许你去创建字体实例。你可以随处使用这样一个实例。你也可能使用一个字体实例来得到字体的量度，包括存在于那个字体中的字符串所站用的尺寸。

tkFont.Font(family="Times", size=10, weight=tkFont.BOLD)
tkFont.Font(family="Helvetica", size=10, weight=tkFont.BOLD,
slant=tkFont.ITALIC)
tkFont.Font(family="Symbol", size=8)

如果你修改一个已命名的字体（使用config方法），这个改变将自动影响到所有使用这个字体的窗口部件。

Font构造器支持下列的样式选项（注意常量被定义在tkFont模块中）：

样式选项及说明：

family选项
类型：字符串
说明：字体类型

size选项
类型：整型
说明：以磅为单位的字体的尺寸。要以象素为单位的话，使用负值。

weight选项
类型：常量
说明：字体的粗细。使用NORMAL或BOLD。默认为NORMAL。

slant选项
类型：常量
说明：字体倾斜。使用NORMAL或ITALIC。默认为NORMAL。

underline选项
类型：标志
说明：字体下划线。如果1(true)，字体加下划线。默认为0(false)。

overstrike选项
类型：标志
说明：字体划线。如果为1(true)，则字体上有一条线；默认为0(false)。

3、系统字体

Tk也支持特定系统的字体名。在X下，这些通常是字体别名如fixed,6x10等等。

在Windows下，这些包括ansi,ansifixed,device,oemfixed,system和systemfixed：
Tkinter类之窗口部件类

在Macintosh上，系统字体名是application和system。

注意：系统字体是字体名，不是字体类型名，它们不能与尺寸或样式属性结合。为了可移植性，尽可能避免使用这些名字。

4、X字体描述

X字体描述是如下格式的字符串（星号所代表的是无关字段。具体细节可查看Tk文档或X手册）：
-*-family-weight-slant-*--*-size-*-*-*-*-charset

典型的字体类别如：Times, Helvetica, Courier or Symbol。

weight可以是"Bold"或"Normal"。slant取值中R代表"roman"(正常)，I代表"italic"，o代表团"oblique"（实际上等同于italic）。

size是字体的高度，以十分之一磅为单位。一英寸72磅，但是一些低分辩率的显示器的1磅较常规的大些，以便小字体能够清晰显示。charset（字符集）通常是ISO8859-1 (ISO Latin 1), 但一些字体也使用其它的值。

下面的描述的family取值是Times，weight取值是Bold，slant取值是R，size取值是120，charset取值是ISO8859-1：
-*-Times-Bold-R-*--*-120-*-*-*-*-ISO8859-1

如果你不关心charset（字符集），或你使用如Symbol的字体（这种字体类别有特定的字符集），那么你可以使用一个星号作为描述的最后部分：
-*-Symbol-*-*-*--*-80-*

典 型的X server至少支持Times, Helvetica, Courier等字体，size有8, 10, 12, 14, 18, 和 24 磅，weight有normal，bold、italic(Times)或oblique(Helvetica, Courier)。大多数的服务器都有 支持随意查看字体。你可以使用如xlsfonts和xfontsel来检查你所访问的服务器的字体。

这种类型的字体描述可以用在Windows 和Macintosh上。注意：如果你使用Tk4.2，你必须牢记字体类型必须是Windows所支持的一种。
```













