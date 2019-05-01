## python学习网站：

> http://looop.cn/?p=111 

## 注释：

> 单行注释 #

> 多行注释 """ """      '''  '''

> 批量注释 同多行

> 中文注释  coding=utf-8  或者：  #coding=gbk，如果开头不声明保存编码的格式是什么，那么它会默认使用ASKII码保存文件，这时如果你的代码中有中文就会出错了，即使你的中文是包含在注释里面的。所以加上中文注释很重要。 

> cls清空

## 内建函数

> print()   input()   type()  float()   int()   dir()

单个输出，多个输出，表达式

print("str",end="str")

### 格式化打印   

-  %d（整数） 
-  %f（浮点数）
-   %s（字符串）

```py
print ("He is %d years old"%25)
print("%d"%(10.4))
dir()内建函数查看当前python的一些内建的属性：包括了内建变量、内建函数等；
input内建函数的语法：input([prompt]) 参数说明：
prompt: 提示信息
input() 和 raw_input() 这两个函数均能接收 字符串 ，但 raw_input() 直接读取控制台的输入（任何类型的输入它都可以接收）。而对于 input() ，它希望能够读取一个合法的 python 表达式，即你输入字符串的时候必须使用引号将它括起来，否则它会引发一个 SyntaxError 。

除非对 input() 有特别需要，否则一般情况下我们都是推荐使用 raw_input() 来与用户交互。
eg:x = input("请输入您的名字：")
```

## 变量：

- 没有声明符
- 不需要声明
- 由数字 字母 下划线组成     不能使用$符号   不能以数字开头  区分大小写
- 不支持自增，自减   a+=1
- 不可以使用关键字，保留字

## 数据类型：

> 在Python中，按照对象是否会变，将类型分类为两类，分别是可变类型和不可变类型，可变类型，即对象的内容可以改变，主要包括list和dict；不可变类型，即对象的内容不可以改变，主要包括数值类型（int，float，复数），str和touple等。

### 数字   

- 整数（二进制  0b    八进制  0o    十六进制 0x   科学计数法8e2）

  ```python 
  int()    将数值或字符串转换为整数int，完整使用形式int(x,base),base用于指定x的进制
  long()   将数值或字符串转换为整数long，完整使用形式long(x, base),base用于指定x的进制
  ```

- 浮点数   print("%0.1f"%0.2)保留一位小数

  ```python
  float()  将数值或字符串转换为浮点数
  ```

- 复数    

  ```python
  complex()返回一个复数，完整使用形式 complex(real,imag)
  ```

### 浮点数，整数的转化

>  float()     int()

### 将十进制转化为二进制 八进制  十六进制

- bin() 
- oct()
	 hex()	

### 十六进制和二进制的相互转化

```py
十六进制 to 二进制: bin(int(str,16)) 
二进制 to 十六进制 : hex(int(str,2)) 

二进制 to 十进制 : int(str,n=10) 
def bin2dec(string_num):
    return str(int(string_num, 2))
 
十六进制 to 十进制
def hex2dec(string_num):
    return str(int(string_num.upper(), 16))
```

| ↓      | 2进制          | 8进制          | 10进制          | 16进制          |
| ------ | -------------- | -------------- | --------------- | --------------- |
| 2进制  | -              | bin(int(x, 8)) | bin(int(x, 10)) | bin(int(x, 16)) |
| 8进制  | oct(int(x, 2)) | -              | oct(int(x, 10)) | oct(int(x, 16)) |
| 10进制 | int(x, 2)      | int(x, 8)      | -               | int(x, 16)      |
| 16进制 | hex(int(x, 2)) | hex(int(x, 8)) | hex(int(x, 10)) | -               |

### 定义方式：

- 单引号  ‘ ’
- 双引号 “ ”
- 三引号 ‘’‘  ’‘’    “”“”  “”“

### 转义字符：

- r   之后写的为普通字符   \n  \r  \t
- b  后面的字符串是byte (二进制)  在python2中  print()函数操作的全部为byte型数据 在 python3中是Unicode数据
- u  为了python2兼容到python3

## 切片

> str[start: end: step]   step默认为1  可以为负数；（切片并不是只能切字符串，也可以切列表）

```py
str = "陕西优逸客"
print( str[2:5:] )
```

## 字符串

### 注意：

- 字符串是不可变的

### 字符串的内建函数：

- string.capitalize()  首字母变为大写

- string.lower()  小写

- string.upper() 大写

- string.center(len,"str") 扩充，以string为中心两边填充(len为字符串的总宽度)

- string.ljust(len,"str") 扩充，在string右边填充

- string.rjust(len,"str") 扩充，在string左边填充

- string.count("str",start,end) 在start到end之间str的次数

- string.encode(encoding="utf-8/gbk/gb2312",errors="ignore") 以指定格式编码   //encoding(编码方式)

- string.decode(encoding="utf-8/gbk/gb2312",errors="ignore") 以指定格式解码

- string.endswith(obj,start,end)  是否以obj(某一个字符)结尾

- string.find("str",start,end)  返回str的位置下标，找不到-1；

- string.rfind("str",start,end) 倒着寻找

- string.index("str",start,end)返回str的位置下标，找不到报异常

- string.rindex("str",start,end)倒着寻找

- string.isalnum() 至少有一个字符，并且所有字符都是字母数字，返回boolean值

- string.isalpha()  至少有一个字符，并且所有字符都是字母，返回boolean值

- string.isdecimal() 是否字符串都是十进制的数字

- string.isdigit() 是否字符串都是数字

- string.islower() 是否全部小写

- string.isupper() 是否 全部大写

- string.isspace() 至少为一个字符，string全为空,返回True，否则返回False；

- string.join(seq) 将序列中的元素以指定的字符连接生成一个新的字符串 

  ```py
  str = "-";
  seq = ("a", "b", "c")  #字符串序列
  print str.join(seq);
  ```

  

- string.split("str",num)将string通过str进行分割，num指定分割次数

- string.splitlines() 将string通过\n进行分割

- string.strip(["str"]) 在字符串前后删除空格，或者删除str

- lstrip 去掉左边的空格

- rstrip 去掉右边的空格

  | 转义字符    |                   描述                   |
  | ----------- | :--------------------------------------: |
  | \(在行尾时) |                  续行符                  |
  | \\          |                反斜杠符号                |
  | \’          |                  单引号                  |
  | \”          |                  双引号                  |
  | \a          |                   响铃                   |
  | \b          |             退格(Backspace)              |
  | \e          |                   转义                   |
  | \000        |                    空                    |
  | \n          |                   换行                   |
  | \v          |                纵向制表符                |
  | \t          |                横向制表符                |
  | \r          |                   回车                   |
  | \f          |                   换页                   |
  | \oyy        | 八进制数yy代表的字符，例如：\o12代表换行 |
  | \xyy        | 十进制数yy代表的字符，例如：\x0a代表换行 |
  | \other      |         其它的字符以普通格式输出         |

```py
str = "   山西   "
print(len(str))  获取字符串的长度
str1 = (str.strip())
print(len(str1))  
```

```py

Python 的字符串常用内建函数如下：
1、
capitalize()
将字符串的第一个字符转换为大写
2、
center(width, fillchar)
 
返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
3、
count(str, beg= 0,end=len(string))
 
返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
4、
bytes.decode(encoding="utf-8", errors="strict")
 
Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。
5、
encode(encoding='UTF-8',errors='strict')
 
以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
6、
endswith(suffix, beg=0, end=len(string))
检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
7、
expandtabs(tabsize=8)
 
把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。
8、
find(str, beg=0 end=len(string))
 
检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
9、
index(str, beg=0, end=len(string))
 
跟find()方法一样，只不过如果str不在字符串中会报一个异常.
10、
isalnum()
 
如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
11、
isalpha()
 
如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
12、
isdigit()
 
如果字符串只包含数字则返回 True 否则返回 False..
13、
islower()
 
如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
14、
isnumeric()
 
如果字符串中只包含数字字符，则返回 True，否则返回 False
15、
isspace()
 
如果字符串中只包含空白，则返回 True，否则返回 False.
16、
istitle()
 
如果字符串是标题化的(见 title())则返回 True，否则返回 False
17、
isupper()
 
如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
18、
join(seq)
 
以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
19、
len(string)
 
返回字符串长度
20、
ljust(width[, fillchar])
 
返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。
21、
lower()
 
转换字符串中所有大写字符为小写.
22、
lstrip()
 
截掉字符串左边的空格或指定字符。
23、
maketrans()
 
创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
24、
max(str)
 
返回字符串 str 中最大的字母。
25、
min(str)
 
返回字符串 str 中最小的字母。
26、
replace(old, new [, max])
 
把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。
27、
rfind(str, beg=0,end=len(string))
 
类似于 find()函数，不过是从右边开始查找.
28、
rindex( str, beg=0, end=len(string))
 
类似于 index()，不过是从右边开始.
29、
rjust(width,[, fillchar])
 
返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
30、
rstrip()
 
删除字符串字符串末尾的空格.
31、
split(str="", num=string.count(str))
 
num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num 个子字符串
32、
splitlines([keepends])
 
按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
33、
startswith(str, beg=0,end=len(string))
检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。
34、
strip([chars])
在字符串上执行 lstrip()和 rstrip()
35、
swapcase()
将字符串中大写转换为小写，小写转换为大写
36、
title()
返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
37、
translate(table, deletechars="")
根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
38、
upper()
转换字符串中的小写字母为大写
39、
zfill (width)
返回长度为 width 的字符串，原字符串右对齐，前面填充0
40、
isdecimal()
```



## 列表：

### 语法：

> mylist = [1,2,3,4,5]

### 注意：

> 列表是有序的对象的集合，集合是无序的对象。

- 列表可以保存任意数据类型
- 列表可以使用切片
- 列表是可变的，字符串不可变
- 可以创建空列表，也可以创建只有一个元素的列表
- 可以创建多维列表

### 列表的遍历：

```py
for item in mylist:
print(item,end="")  下标
print(mylist,index(item)) 值
enumerate()   将列表转换为（index,value)or((0,1),(1,2),(2,3),(3,4),(4,5),(5,6))的序列(枚举法)
```

```[]py
mylist = [[1,2],[3,4]]
mylist1 = []
for item in mylist:
	mylist1.append(item)
print(mylist1)  //浅拷贝
import copy
arr = [[1,2],[3,4]]
arr1 = copy.copy(arr) #浅拷贝
arr2 = copy.deepcopy(arr) #深拷贝
一、浅拷贝
定义：浅拷贝只是对另外一个变量的内存地址的拷贝，这两个变量指向同一个内存地址的变量值。
浅拷贝的特点：
公用一个值；
这两个变量的内存地址一样；
对其中一个变量的值改变，另外一个变量的值也会改变；

二、深拷贝：
定义：一个变量对另外一个变量的值拷贝。
深拷贝的特点：
两个变量的内存地址不同；
两个变量各有自己的值，且互不影响；
对其任意一个变量的值的改变不会影响另外一个；

python中的函数，如果是传递的tuple，那么是值传递；如果传递的参数类型是list，那么是引用传递。
```

## 列表函数

- list.append(item)  在列表最后插入元素
- list.insert (index,item) 在指定位置插入item，如果没有index，默认最后插入
- list.extend(list1)  合并两个list数据
- arr + [4,5,6] 合并多个list数据
- list.count(item) 查看某元素在list的次数
- list.index(item) 查看某一元素在list的第一个下标,如果不存在，报异常
- list.pop(index)  默认删除最后一个元素，可以指定要删除的元素。
- list.remove(item) 删除list中的元素，有相同的删除第一个
- list.reverse() 将list反转
- list.sort(reverse=True) 排序  默认升序  reverse=True 降序
- list.copy() 浅拷贝
- list.clear() 清空数组

## 元组Tuple

> 定义：mytuple = (1,)

### 注意：

- 元组和列表相似，区别就是元组不能改变
- 元组通过圆括号定义
- 可以使用切片
- 元组可以定义只有一个元素的元组，mytuple=(1,) ,逗号不可缺少
- 空元组

### 操作list/tuple的内建函数

- len(list) 数组的长度
- max() 数组的最大数
- min() 数组的最小数
- list() 将元组转换为列表
- tuple() 将列表转换为元组
- enumerate() 返回下标和元素

## 字典dict

- ### json格式创建

``` py
mydict = {"name":"a"}
json.dumps()  将python数据结构转化为json格式
json.loads()  将json格式转化为python数据结构

如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据。
```

- ### 工厂函数创建

```py
mydict1 = dict(name="小红",age=10) 传入关键字
mydict2 = dict(zip(["name","age"],["小艾"，"24"])) 映射函数方式来构造字典
dict()  创建空字典
mydict3 = dict([('one'),1,('two',2)]) 可迭代对象方式
```

- ### 字典内建方法

```py
mydict4 = dict.fromkeys(["name1","name2"],"小艾") 批量创建键值
```

- ### 字典访问方式

> mydict[键]

```
dict.get(key, default=None)
dict = {'a':"hello",'b':"how",'c':"you"}
print ("Value : %s" %  dict.get('a'))
```

- ### 删除字典属性和方法：

> del.mydict["name"]

- ### 字典的内建函数：

  - ​ dict.get("key","info")  返回key对应的value，没有为none  info指定没找到的错误信息

  - dict.keys() 返回字典中所有的key
  - dict.values() 返回字典中所有的value
  - dict.items() 返回字典中所有的key:value形式数据
  - dict.setdefault(key,value)添加数据
  - dict.pop(key) 删除key
  - dict.popitem() 删除最后一位的key:value
  - dict.clear() 清空dict

## 集合:

> 1.不同元素组成
>
> 2.无序
>
> 3.集合中的元素必须是不可变类型，set转换为集合。；直接创建：myset{1,2,5}
>
> **set**是[基本数据类型](http://www.iplaypy.com/jichu/data-type.html)的一种**集合**类型，它有可变集合(set())和不可变集合(frozenset)两种。 

- set.add("abc") 添加一项；“abc”看做参数        #是把要传入的元素做为整体添加到集合中 
- set.update() 更新集合       #是把要传入的元素拆分，做为个体传入到集合中   
- set.remove() 删除

### 集合的操作：

- 交集     &
- 并集     |
- 差集      -

## boolean：

- True
- False
- None

## 运算符：

### 算术运算符

> +-*/(浮点数) //( //来表示整数除法，返回不大于结果的一个最大的整数)  %  **(幂运算)

#### 注意：

- Python3中，除法无论有无复杂类型，结果都会精确到浮点型。
- +操作两个数字型数据=>加运算
- +操作一个数字型数据=>正数
- +操作的str list tuple =>连接作用
- -加法运算  负数
- *操作两个数字型数据=>乘法运算
- *操作的str list tuple =>重复

### 逻辑运算符：

- and  &
- or  ||
- not  !

### 关系运算符：

- ==
- \>=
- <=
- <
- \>
- js 动态类型  弱类型的语言
- python  动态类型 强类型语言

### 位运算符：

- & 按位与运算符  参与运算的两个值，如果两个 相应位都为1，则该位的结果为1，否则为0 // 源码  反码  补码   补码同源码一样，为负数时，加1
- |  按位或运算符  只要对应的两个二进位有一个为1时，结果为就为1.
- ^  按位异或运算符  当两个对应的二进位相异时，结果为1
- ~按位取反运算符  对数据的两个二进制位取反，即把1变为0，把0变为1
- << 左移位运算符   运算数的各二进位全部左移若干位，由<< 右边的数字指定了移动的位数，高位丢弃，低位补0，
- \>>右移位运算符 把“>>”左边的运算符的各二进位全部右移若干位，>>右边的数字指定了移动的位数。

### 赋值运算符：

- =
- +=
- -=
- *=
- /=
- %=
- **=   幂赋值运算符
- //=   取整除赋值运算符

### 成员运算符：

- in 如果在指定的序列中找到指定的值返回true，否则返回false
- not in  如果在指定的序列中没有找到指定的值返回true，否则返回false

### 身份运算符：

- is   按照地址判断两个标识符是否相等。
- is  not

### 运算符优先级：

1. **  幂运算符

2. -+  正负

3. */%//  关系运算符

4. +- 

5. \>>  <<

   > 幂运算  正负  算术运算符  关系运算符  赋值运算符  身份  成员 逻辑（米蒸酸罐，附身成洛）

## 选择结构：

**单分支格式:**

```
if 条件表达式:
    语句块。
```

**双分支结构**
格式：

```
if 条件表达式：
    语句块1
else：
    语句块2
```

**多分支语句**

```
if 条件表达式1:
    语句块1
elif 条件表达式2:
    语句块2
elif 条件表达式3:
   语句块3
[else:
    语句块n]
```

**条件运算符**

```py
python的条件运算符相当于一个三元运算符，有3个分量。
形式: 表达式1 if 条件表达式 else 表达式2

规则，先求条件表达式的值，如果其值为true，则求表达式1，并以表达式1的值为结果，如果条件表达式的值为flase，则求表达式2，并以表达式2的值为条件运算符的结果。
```

- range(start,end,step)  #创建序列，start开始下标，end结束，step代表歩进值

- while循环       while 循环条件：循环语句  

- for循环       for   变量  in   可迭代对象（in后面跟随的对象要求是可迭代对象，即可以直接作用于for循环的对象统称为可迭代对象（Iterable），如list、tuple、dict、set、str等。 

- ）

- 随机数   

  ```py
  import  random 
  num = random.randint(0,100)  
  ```

### 循环中干涉循环的语句：

- continue # 跳过本次循环的剩余代码，直接跳过进入下一个循环。
- break  # 直接跳过整个循环,即退出整个循环。

## 函数：

> 将完成某一特定功能的代码块集合起来，可以重复使用这些代码块。

### 参数：

- #### 缺省(默认)参数：

  >  默认参数必须指向不变对象

```py
def fn(name,age=18)
```

- #### 可变参数：

  >  可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。 

```py
def add(*arr):
	num = 0
	for i in arr:
		num+=i
	print(num)
```

- #### 关键字参数：

  > 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。 

```py
def person(name,age=13,**attr):
	print("name:%s"%name)
	print("age:%s"%age)
	print(attr)
person(name = "xn",age = 18,sex = "男"，tel = 45876654123)
```

- #### 参数组合：

> 必选参数>默认参数>可变参数> 关键字参数    （缺莫客观）

### 小结：

- Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
- 默认参数一定要用不可变对象，如果是可变对象，运行会有逻辑错误！
- 要注意定义可变参数和关键字参数的语法：
  - `*args`是可变参数，args接收的是一个tuple；
  - **kw`是关键字参数，kw接收的是一个dict。
- 调用函数时如何传入可变参数和关键字参数的语法：
  - 可变参数既可以直接传入：`func(1, 2, 3)`，又可以先组装list或tuple，再通过`*args`传入：`func(*(1, 2, 3))`；
  - 关键字参数既可以直接传入：`func(a=1, b=2)`，又可以先组装dict，再通过`**kw`传入：`func(**{'a': 1, 'b': 2})`。
- 使用`*args`和`**kw`是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

### 函数返回值：

> 场景：通过某个函数，处理好数据，想要在外界拿到的处理结果做不同的操作。

- return后续代码不会继续执行
- 值仅返回一次
- 要返回多个数据，整体返回

## 高阶函数：

- 实参高阶函数：把一个函数名当做实参传递给另一个函数

```py
def add(a,b):
    return a + b
def sub(a,b):
    return a - b 
def size(a,b,fn):
    return fn(a,b)
print(size(10,20,sub))
```



- 返回值高阶函数：返回值中包含函数名

```py
def fn1():
    def aa():
        print("this is you")
    return aa

bb = fn1()
bb()
```

## 匿名函数:

> lambda 参数 ：表达式
>
> 可以有多个参数
>
> 表达式不需要return，自动return

```py
1.num = (lambda a,b:a+b)(10,20)  自己调用自己
print(num)
2.fn = lambda a,b:a+b
print(fn(10,20))
匿名函数的调用方法：1.自调用 2.字面量
```

- ### map(函数，序列)

```py
arr = map(lambda x：x*2,range(1,19))
print(list(arr))
arr = map(lambda x,y：x+y,range(1,19),range(1,19))
print(list(arr))
```

- ### filter(函数，序列)

```py
filter(lambda x:x>5,range(1,11))
print(list(arr))
```

- ### import functools    functools.reduce(函数，序列)

```py
res = functools.reduce(lambda x,y:x+y,range(1,11))
print(res)
```

## global:

> 是python唯一看起来像声明语句的语句，但是它并不是一个类型或大小的声明，它是一个命名空间的声明。它告诉python函数打算生成一个或多个全局变量名。即存在于整个模块内部作用域(命名空间)的变量名。声明的同时不能修改。如果修改，必须在修改之前声明。global关键字用来在函数或其他局部作用域中使用全局变量。但是如果不修改全局变量也可以不使用global关键字。 

```py
aa = 123
def fn1():
	global aa,bb
	bb = 5
fn1()
```

## nonlocal:

> nonlocal适用于嵌套函数中内部函数修改外部变量的值 

```py 
num1 = 123
def aa():
	num1 = 456
	def bb():
		nonlocal num1
		num1 +=10
	bb()
	print(num1)
aa()
```

## 闭包函数：

>  在一些语言中，在函数中可以定义另一个函数时，如果内部的函数引用了外部作用域（但不是在全局作用域 )的局部变量，并且外部函数的返回值是内函数的引用。这样就构成了一个闭包。 闭包可以用来在一个函数与一组‘私有’变量之间创建关联关系。在给定函数被多次调用的过程中，这些私有变量能保持其永久性。  

```py
def aa():
    num1 = 123
    def bb():
        print(num1)
    return bb
 
dd = aa()
dd()
#加括号运行，就是在执行一个闭包函数
```

## 递归函数：

> 如果一个函数在内部不调用其他函数，只调用自己的时候，这个函数就是递归函数。

```py
def digui(num):
    if num == 1:
        return 1
    else:
        return num*digui(num-1)
print(digui(12))
```

## 装饰器：

> 定义：就是为了给某程序添加功能

> 使用场景：比如该程序已经上线或已经被使用，就不能大批量的修改源代码

> 原则：1.不能修改被装饰的函数的源代码 2.不能修改被装饰的函数的调用方式  3.满足1.2的情况下给程序添加新功能。

> 定义公式：<函数+实参高阶函数+返回值高阶函数+嵌套函数+语法糖=装饰器>  从内到外调用

```py
import time

def tester(fn);
	def newtest():
		start = time.time()
		fn()
		end = time.time()
		print("运行总时间："，end-sart)
	return newtest
	
def test()；
	time.sleep(1)
	print("test is running")
	
test = tester(test)
test()

or
import time

def tester(fn);
	def newtest():
		start = time.time()
		fn()
		end = time.time()
		print("运行总时间："，end-sart)
	return newtest

@tester	
def test()；
	time.sleep(1)
	print("test is running")
	
test()
```

## 函数的柯里化：

```py
def add(a):
	def fn(b):
		print(a+b)
	return fn
	
add(5)(4)
```

# 文件操作：

```py
f = open("filename",mode)
filename:操作文件地址
mode:打开文件模式
f:文件对象

流程如下：
f = open("file.txt","r",encoding = "utf-8", errors="ignore")
con = f.read()
f.close()  先保存(把缓存的内容写入硬盘)后关闭
print(con)

f = open("file.txt","w",encoding = "gb2312", errors="ignore")
for i in range(10):
    i = f.write("这是第%s行\n"%i)
f.close()


f = open("file.txt","a",encoding = "gb2312", errors="ignore")
for i in range(10):
    i = f.write("这是第%s行\n"%i)
f.close()

f = open("file.txt","r",encoding = "gb2312", errors="ignore")
con = f.read()
f.close()
d = open("file1.txt","w",encoding = "gb2312", errors="ignore")
arr = []
arr.append(con)
d.writelines(arr)
d.close()

添加文件夹：
import os,os.path
def copyFile(dir):
    if os.path.isfile(dir):
        f = open(dir,"r")
        con = f.readlines()
        f.close()
        f1 = open("副本"+dir,"w")
        f1.writelines(con)
        f1.close()
    else:
        os.mkdir("副本"+dir)
        for item in os.listdir(dir):
            copyFile(dir+"/"+item)
copyFile("dir")

```

- ### r 读操作

  - f.read([num])   num代表读取字符数量，默认为全部
  - f.readline([num]) 文件读取每一行，通过\r\nEOF(文件结束标识)来区别。num代表读取一行几个字符
  - f.readlines   返回列表，包括所有的行

- ### w 写操作  指针在开头

  > 每次执行都是从头开始写入，路径不对会创建新文件

  - f.write(str) 把str写入文件
  - f.writelines(seq)

- ### a 追加  指针在末尾

  > 每次执行都是从末尾开始写入，路径不对会创建新文件

- ### os 

  - os  操作文件.系统 
  - ​    os.path  文件路径
  - ​      os.system()     命令控制台 
  -    os.listdir()     显示目录下的内容
  - os.mkdir()   创建文件夹
  - ​      os.path.isfile()  是否为文件
  - ​    os.path.isdir  是否为路径 
  -   递归函数
  - ​    文件操作  

- ### b

  > 二进制模式

- ### +

  > 读写模式

  - r+   每次读写文件在文件的开头
  - w+ 创建新文件，每次读写都会覆盖原来的内容
  - a+ 创建新文件，每次读写追加

- ### seek

  > seek(): 移动文件读取指针到指定的位置

  - f.seek(p,0) 移动到文件第p个字节处，绝对位置
  - f.seek(p,1)  移动到相对于当前位置之后的p个字节
  - f.seek(p,2)  移动到相对文章尾之后的p个字节(文件以二进制方式打开)
  - f.tell():返回文件读取指针的位置 (文件以二进制方式打开)
  - f.flush() 把缓冲区的内容写入硬盘

- ### try

  ```py
  try:
  	f = open("note2.txt","r")
  except:
  	print("发生错误")     f对，则except不执行
  	
  try:
  	f = open("note1.txt","r")
  finally:
  	if f:
  		f.close()					f对，finally也执行
  		
  with open("notel.txt","r") as f:
  	f.read()
  ```

  ## pickle:

  > 默认存储方式是二进制的

  - pickle.dump(obj, file[, protocol]) 　　序列化对象，并将结果数据流写入到文件对象中。参数protocol是序列化模式，默认值为0，表示以文本的形式序列化。protocol的值还可以是1或2，表示以二进制的形式序列化。 
  - pickle.load(file) 　　反序列化对象。将文件中的数据解析为一个Python对象。 

  ## csv:

  > csv格式是电子表格和数据库最常用的导入和导出方式。newline="" 写在open后面

  - csv.writer(f,dialect="excel")  #创建写入对象
  - writer.writerow()
  - writer.writeheader()  #写表头
  - writer.writerows()
  - csv.DictWriter()
  - csv.reader(csvfile)
  - csv.DictReader(csvfile)

  ```py
  import csv
  with open("demo.csv","r") as f:
  #以列表形式读：
  	reader = csv.reader(f)
  	mylist = list(reader)
  	for i in mylist:
  		print(i)
  
  #以字典形式读：
  	reader = csv.DictReader(f)
    for item in list(reader):
         print(dict(item))
  
  with open("demo.csv","w") as f:
  #以列表方法写：
      writer = csv.writer(f,dialect="excel")
      writer.writerow(['id','name','sex','tel'])
      #写入多行
      writer.writerows([
        ['1','xb','n','5544478'],
        ['1','xb','n','5544478'],
        ['1','xb','n','5544478']
      ])
  #以字典的形式写：
  		writer = csv.DictWriter(f,['id','name','sex','tel'])
  		writer.writeheader()  #写表头
  		writer.writerow({'id':1,'name':xb,'sex':男,'tel':5455544})
  		writer.writerows([{'id':1,'name':xb,'sex':男,'tel':5455544,'id':1,'name':xb,'sex':男,'tel':5455544,'id':1,'name':xb,'sex':男,'tel':5455544}])
  ```

  ## 引用的规则：

  - 内置模块          python自己带的功能         import  ***   

  -   自定义模块    同一级目录，上一级目录，python的文件里面  

  - 第三方模块

  - pip  安装 第三方模块           一般放在/site-packages中 

    ```py
     import sys  
     sys.path.append(路径) 添加路径
     
    调用文件   import b
    调用文件及  import b.b   .代表文件夹下的
    ```

      