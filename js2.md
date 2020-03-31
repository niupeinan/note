 

# 引入js:

- 外部引入方式

  ```css
  <script src=""></script>
  ```

- 嵌入式

  ```css
  在html页面中用script标签引入js.
  ```

- 事件后

  ```css
  <div onclick="alert"></div>
  ```

## 注意：

- js的几种引入方式是相互关联的，可以相互操作与访问。
- 外部js中不能添加script标签对。
- 嵌入式js不能添加src属性。

# 输出工具：

- 弹出框

  ```html
  alert(1);
  alert('a');
  ```

  

- 输出到控制台

  ```html
  console.log(1);
  ```

  

- 输出到页面中（识别标签对）

  ```html
  document.write("a");
  document.write("<i>倾斜</i>");
  ```

# 输入框：

```js
prompt(提示文本，[默认值])；
```

## 注释：

- 单行注释 ctrl+/
- 块级注释 ctrl+shift+/

# 变量：

> 一个容器，存储数据。

## 命名规范：

1. 不能以数字开头；
2. 区分大小写；
3. 不能以关键字（js中已经用到的）命名；
4. 不能以保留字命名；
5. 有意义
6. 首字母大写 Array String Object
7. 驼峰命名法 defFdssVklm

## 赋值：

1. 先声明，后赋值； var num;num=10;
2. 声明的同时赋值； var num=11;
3. 一次性先声明多个变量，再赋值； var a,b,c; a=1,b=2,c=3;  
4. 一次性声明多个变量并且赋值； var a=1,b=2,c=3;

## 注意事项：

- 变量要先声明后访问，变量的默认值为undefined；
- 新值覆盖旧值；
- 变量可以重复声明；
- 不用var关键字声明变量，但赋值，不会报错，此变量为全局变量；
- 不用var关键字声明变量，也不赋值，会报错；
- 先访问后声明变量，输出值为undefined,预解析（var .function）；

# 数据类型：

- 根据数据在内存中的存储位置划分，基本数据类型中存放在栈中，引用数据存放在堆中。（指针存放在栈中，内容存放在堆中）；

```js
let arr=[1,2,3,4];
let arr1=arr //传址
let arr2=[];
for(let i=1;i<arr.length;i++){
  arr2[i]=arr[i]; //浅拷贝  
}			 
// 遍历数组
for(let item of arr){arr2.push(item)}  // 返回数组里面的数值
for(let item in arr) // 返回数组中数值对应的下标
// 遍历对象
for(let i in obj)  // 返回对象的属性名；在使用for-in循环之前，先检测确认该对象的值不是null或underfined。
for(let i of obj)  // 浏览器报错
// 深拷贝
function deepCopy(p, c) {
　　　　var c = c || {};
　　　　for (var i in p) {
　　　　　　if (typeof p[i] === 'object') {
　　　　　　　　c[i] = (p[i].constructor === Array) ? [] : {};
　　　　　　　　deepCopy(p[i], c[i]);
　　　　　　} else {
　　　　　　　　　c[i] = p[i];
　　　　　　}
　　　　}
　　　　return c;
　　}

// 深拷贝
function copy(arr){
    var obj=arr.constructor==Array?[]:{};
　　//第二种方法 var obj=arr instanceof Array?[]:{}；在监测一个引用类型值和构造函数时，instanceof操作符始终会返回true，当然如果使用instanceof操作符监测基本数据类型，返回的值始终都是false。
    for(var item in arr){
        if(typeof arr[item]==="object"){
            obj[item]=copy(arr[item]);
        }else{
            obj[item]=arr[item];
        }
    }
    return obj;
}
```



## 基本数据类型：

- undefined
- null
- string
- boolean
- number

## 引用数据类型：

- object（属性与方法的集合）数组.   函数（function）.对象

# typeof:

用来判断变量的数据类型的。结果是字符串。

```js
console.log(typeof(null));
```





| 数据类型        |                              值                              | 情况 | typeof结果   |
| --------------- | :----------------------------------------------------------: | ---- | ------------ |
| undefined       |                          undefined                           |      | undefined    |
| null            |                           空占位符                           |      | object       |
| string 字符串型 | 1.带引号  ' '   " "2. (模板字符块（``,内部变量添加${};)   3.字符编码(ASCLL .utf-8 . gb2312 .unicode)4.转义字符（\' \" \t \\\ \r \n \f ） |      | string字符串 |
| boolean 布尔型  |                         true  false                          |      | boolean      |
| number 数值型   | 整数 小数 八进制(0o开头) 十六进制(0x)  负数 特殊值 二进制(0b开头) |      | number       |
| object          |                                                              |      |              |

NaN:not a number;本来期望返回数值的操作但并未返回数值的情况。

### 颜色的生成：

```js
取随机数 0~1之间的小数，不包括1；Math.floor 向下取整 Math.ceil 向上取整 Math.pow x的y次幂 Math.sqrt: 返回四舍五入的一个double值的正平方根.
 //随机生成颜色
var r=Math.random()*255;
	var g=Math.random()*255;
	var b=Math.random()*255;
	var rgb1=("rgb("+r+","+g+","+b+")");
	console.log(rgb1);
```

```js
var num=prompt("请输入鸡蛋数",10002);
	console.log(Math.ceil(num/20))
```



```
一、对于数字类型的操作数而言， typeof 返回的值是 number。比如说：typeof(1)，返回的值就是number。上面是举的常规数字，对于非常规的数字类型而言，其结果返回的也是number。比如typeof(NaN)，NaN在JavaScript中代表的是特殊非数字值，虽然它本身是一个数字类型。在JavaScript中，特殊的数字类型还有几种：
Infinity 表示无穷大特殊值
NaN　　　　　　　　　　　　特殊的非数字值
Number.MAX_VALUE　　　　　可表示的最大数字
Number.MIN_VALUE　　　　　可表示的最小数字（与零最接近）
Number.NaN　　　　　 　　　特殊的非数字值
Number.POSITIVE_INFINITY　表示正无穷大的特殊值
Number.NEGATIVE_INFINITY  表示负无穷大的特殊值
以上特殊类型，在用typeof进行运算进，其结果都将是number。
二、对于字符串类型， typeof 返回的值是 string。比如typeof("123")返回的值是string。
三、对于布尔类型， typeof 返回的值是 boolean 。比如typeof(true)返回的值是boolean。
四、对于对象、数组、null 返回的值是 object 。比如typeof(window)，typeof(document)，typeof(null)返回的值都是object。
五、 对于函数类型，返回的值是 function。比如：typeof(eval)，typeof(Date)返回的值都是function。
六、如果运算数是没有定义的（比如说不存在的变量、函数或者undefined），将返回undefined。比如：typeof(sss)、typeof(undefined)都返回undefined。
```

# 运算符：

表达式 ：能够求值的语句

## 算术运算符：

```js
+ - * / % ++var  var++  --var  var--

+：1.操作数都是数值型进行四则运算 
2.操作数中包含字符串，进行拼接。两面同时加+和“，变为变量，在加（）重新变为数值.或者模板字符块（``,内部变量添加${};
++var：先算++，在执行本行中的其他语句。
var++：先执行本行中的其他语句，再执行++。

```



## 关系运算符：

- 返回值为布尔值 true false

  ```js
  > < >= <= == === !== !=    ===（值相等，数据类型相同） ==（值相同）
  ```

  - 如果两个操作数都是字符串（数字型字符串），按照ASCLL码表进行比较大小。
  - 如果两个操作数都是数字，直接比较大小。
  - 如果一个操作数值字符串，另一个操作数是数字，先尝试将字符串转换为数字，如果转换成功，按照数值进行比较大小，如果不成功，则返回false。
  - 1\==true ，0\==false；
  - undefined=null；
  - 如果返回的值value是undefined或者null，!value返回的是true，!!value返回的是false。两个感叹号的作用就在于，如果明确设置了变量的值（非null/undifined/0/""等值),结果就会根据变量的实际值来返回，如果没有设置，结果就会返回false。

## 赋值运算符：

```js
= += -= *= /= %=
```



## 逻辑运算符：

### 测量值与变量之间的逻辑关系：

- && 与
- || 或
- ！取反
- 0  false underfined null  NaN为false，其他情况为true。

### 逻辑运算符的真值表

|   A   |   B   |  A&&B  | A\|\|B |  !A   |
| :---: | :---: | :----: | :----: | :---: |
| true  | true  |  true  |  true  | false |
| true  | false | false  |  true  | false |
| false | true  | fallse |  true  | true  |
| false | false | false  | false  | true  |

### 返回值：

- &&
  - 同真为真，返回第一个假值/同真：第二个真值
- ||
  - 同假为假，返回第一个真值/同假：第二个假值
- ！
  - 取反  boolean值

## 三元运算符：

- 表达式？语句1:语句2；

- 如果表达式的结果为真，执行语句1，否则执行语句2.

  ```js
   var num=prompt("请输入一个数");
   num%2==0?alert(num+"为偶数"):alert(num+"为奇数");
   var bol=confirm("确定退出？");
   bol==1?alert("您已退出"):alert("您已取消退出");
   var num=prompt("请输入接受的值");
   num>Math.random()*99?alert("您赢啦"):alert("不好意思，您输啦");
  ```

## 一元运算符

```js
typeof + - new
```

## 特殊运算符

```js
() .
```



# 流程控制：

代码按照指定条件的执行顺序。

- 顺序结构
- 分支结构
- 循环结构

## 循环结构：

语句按照从上到下的顺序执行。

## 分支结构：

当条件成立时执行相应的语句。

- #### 单分支结构

  ```js
  if(条件){
    条件成立时，执行的语句
  }
  ```

- #### 双分支结构

  ```js
  if(条件){
    条件成立时，执行的语句
  }
  else{
    条件不成立时，执行的语句
  }
  ```

- #### 多分支结构

  ```js
  if(条件){
    条件1成立时，执行的语句
  }
  else if(条件){
    条件1不成立，但是条件2成立时执行的语句
  }
  ....
  else{
    以上条件都不成立，执行的语句
  }
  ```

- #### 嵌套分支

  ```js
  if(){
     if(){}else{}
     }
  else{
    if()else()
  }
  ```

- #### switch

  ```js
  switch(表达式){
      case 值1：语句1;break;
      case 值2：语句2;break;
      ...
      default:语句；
  }
  ```

## 循环结构：

当满足条件时，重复不断地执行语句。

### for循环(明确知道次数)

```js
for(初始条件；终止条件；步进值){
  循环体；
}
    eg:for(var i=0;i<10;i++){
					for(var j=0;j<10;j++){
						document.write("*   ")
					}
				document.write("*<br>")
				}
```

### 执行顺序

- 初始条件
- 终止条件
- 循环体
- 歩进值
- 重复以上；直到不满足终止条件，退出循环体。

### with语句：

> with语句的作用是将代码的作用域设置到一个特定的对象当中。

```js
example: var aa = bb.cc;
		var dd = bb.ee;
        
     with(bb) {
         var aa = cc;
         var dd = ee;
     }
// 严格模式下不允许使用with语句。	
```



### while循环

```js
while(中止条件){
  当满足条件时，执行的语句；
}
```

### do while循环：

```js
do{
  循环体
}while(中止条件)
```

## 终止循环的语句：

- break: 终止整个循环
- continue：终止本次循环，如果后面的语句仍然满足条件，继续执行。

# 数组：

> 按照顺序排列的一组相关数据。每个数组元素都有特定键名（下标）。

## 初始化数组元素：

- 先声明后赋值 

  ```js
  var arr=[]; arrr[0]="a";arr[1]="b";
  ```

- 声明的同时进行赋值

  ```js
  var arr=[1,2,3,4];
  ```

## 数组 的下标：

> 访问数组元素。

## 数组的长度：

> `arr.length`

> 清空数组：`arr.length=0;`

## 遍历数组元素：

1. 用for循环遍历数组；

   ```js
   for(var i=0;i<arr.length;i++){
     arr[i]
   }
   ```

   

2. 用for in遍历

   ```js
   for(var i in arr){
     i;//下标
     arr[i] //元素
   }
   ```

   ### 去除空格：

   ```js
    console.log(max);
       var arr1=[23, ,25,54,65, , ,45,];
       var arr=[];
       for(var i=0;i<arr1.length;i++){
           if(arr1[i]!=undefined) {
               arr[arr.length] = arr1[i];
                   数组对象 push()方法 向数组的后面插入元素   arr.push(arr1[i]);
           }
       }
       console.log(arr);
   ```

## 增加删除：

1. arr.push() 在数组之后插入元素

2. arr.pop()  删除数组最后一位

3. arr.unshift()  在数组之前插入

4. arr.shift() 删除数组前面第一位

5. arr.splice(下标)  删除某一个位置  eg:arr.splice(3,1," ");  //万能的删除和增加  ，返回的参数是删除后的值。

6. arr.includes()   是否包含一个数，返回值boolean.

   ```js
   语法： arr.includes(value, start)
   value: 搜索的内容
   start： 开始搜索的位置，可以为负数
   ```

7. arr.concat(); 连接多个数组

8. arr.slice()  剪切

9. arr.reverse()  取反

10. arr.join(“-”) 将数组转换为字符串

11. arr.sort((x,y)=>x-y)   console.log(arr)  //x-y为升序   y-x为降序

12. arr.find((item)=>item>7(条件))  查找符合条件的第一个元素

13. arr.findIndex 查找符合条件的第一个元素的下标 

14. arr.some()  看数组里面是否有满足条件的值，有true，没就false

15. arr.every() 全部满足true，否则false

16. arr.filter() 返回一个筛选(过滤条件)后的新数组

    ```js
    语法：Array.filter(function(currentValue, indedx, arr), thisValue)
    其中，函数 function 为必须，数组中的每个元素都会执行这个函数。且如果返回值为 true，则该元素被保留；
    函数的第一个参数 currentValue 也为必须，代表当前元素的值。
    thisValue可选。对象作为该执行回调时使用，传递给函数，用作 "this" 的值。如果省略了 thisValue ，"this" 的值为 "undefined"
    ```

    

17. arr.foreach() 让数组中每一个元素都执行一个函数，不会影响原数组。

18. arr.map() 让数组中每一个元素都执行一个函数，返回一个新数组。

19. arr.indexOf()  用来查找某个元素的位置，如果不存在就返回-1 

    ```js
    	arr.indexOf(‘orange') 输出 0 因为 ‘orange' 是数组的第 0 个元素，匹配到并返回下标。
        arr.indexOf(‘o') 输出 -1 因为此方法不会在每一个元素的基础上再次执行 indexOf 匹配。
        arr.indexOf(‘2016') 输出 1 因为此方法从头匹配直到匹配到时返回第一个数组元素的下表，而不是返回全部匹配的下标。
        arr.indexOf(2016) 输出 -1 注意：这里不会做隐式类型转换。
        
        不足： 1.它会返回-1和元素的位置来表示是否包含，在定位方面是没问题，就是不够语义化。
        	  2.不能判断是否有NaN的元素。includes方法可以。
    ```

    

## 二维数组：

>  访问：`arr[i][j]`

遍历：

```js
for(var i=0;i<arr.length;i++){
  for(var j=0;j<arr[i].length;j++){
    console.log=var[i][j];
  }
}
```

## 注意事项：

- 数组元素默认值为undefined；
- 数组的长度是可变的；
- 数组元素可以是任意数据类型；



### 建立表单：

```js
(1)
document.write("<table border='1' cellspacing='0' cellpadding='0'>");
for (var i=0;i<10;i++){
	if(i%2==0){
		document.write("<tr bgcolor='green'>");
		for(var j=0;j<10;j++){
			document.write("<td>"+i+"-"+j+"</td>");
		}
		document.write("</tr>");
		}
	else{
		document.write("<tr bgcolor='red'>");
		for(var j=0;j<10;j++){
			document.write("<td>"+i+"-"+j+"</td>");
		}
		document.write("</tr>");
		}
}
document.write("</table>");
(2)
 var str="<table border='1'>";
 for(var i=0;i<10;i++){
 	str+="<tr>";
 	for(var j=0;j<10;j++){
 		str+="<td>"+i+"-"+j+"</td>";
 	}
 	str+="</str>";
 }
 str+="</taable>";
 document.write(str);
```

## 数学方法

- Math.random  随机
- Math.floor 向上取整
- Math.ceil 向下取整
- Math.pow x的y次幂
- Math.round 四舍五入取整

# 函数：

> 实现某一特定功能的代码块封装起来并且能够重复调用。  apply  cold  bind三种方法

## 函数在js里面的三层意思：

- 就是函数
- 对象
- 构造函数

调用函数：

- 基本语法（function关键字）

  ```js
  function functionName([形参1]，[形参2],...){
    函数体；
    [return 返回值；]
  }
  // 无需指定函数的返回值，因为ECMAScript函数可以在任何时候返回任何值。
  // 未指定返回值的函数返回的是一个特殊的undefined值。
  ```

- 对象的方式

## 函数的调用：

- 函数名+（）;   function name（）;
- 自变量+（）;

### 参数：

> 动态改变函数体的变量，使函数更加灵活。实际上，参数是函数的局部变量。

### 形参：

> 定义函数时，写在括号中的变量。作用是接受实参。

### 实参：

> 函数调用时写在括号中的值，作用是给形参传值。

### 对象的形式：

> 用字面量声明的函数必须先声明后调用，而关键字function声明的函数，调用时可以在声明前也可以在声明后，这是由于预解析。

```js
字面量，自变量 var variable=function(){
  函数体
}
variable();
```



## 返回值：

- 返回值可以是任意数据类型。
- return终止函数，return语句后面的代码不执行。
- 一个函数内部可以有多条return分支语句，最后只执行一条return语句。
- 如果函数没有返回值，返回undefined。

## 参数的传递：

- 参数可以是任意的数据类型。
- 参数的传递是按照顺序传递的。
- 形参=实参 ： 一 一对应
- 形参>实参 ：多余的形参会被赋值undefined
- 形参<实参：实参由arguments对象来接受。

### arguments对象：

- 用来接受参数的详细信息，他的长度是由传入参数的个数决定的。
- 每声明一个函数，在其内部自动生成arguments对象。arguments对象只在函数内部起作用。
- arguments[i]  arguments.length 遍历  类似数组但不是数组。

## 剩余参数：

- 声明；`...rest`

- rest参数与arguments对象的区别：
  - rest接受多余实参，arguments接受所有的实参。
  - rest是数组，能够使用数组的方法；`foreach(function(element){arr[arr.length]=element})`arguments对象是类似数组。

## 参数默认值：

- 分支结构
- 三元运算符
- 逻辑或||
- es6 给形参赋值，当形参为undefined时，给形参赋默认值。

## 回调函数(高阶函数)：

- 形参高阶函数 

- 返回值高阶函数

> ​	把一个函数的指针（函数名）作为一个参数传递给另一个函数，当指针调用函数时，这个函数叫做回调函数。

## 作用域：

> 变量起作用的范围。

- 全局作用域
- 局部作用域
- 块级作用域

### 全局作用域：

> 在整个js代码中都能访问的变量，凡是修改，变量的值都会改变。

- 在函数外部用var声明的变量，拥有全局作用域。
- 不用var声明，但赋值的变量，拥有全局作用域。

### 局部作用域：

- 形参是局部变量，拥有局部作用域
- 在函数内部用var关键字声明的变量，拥有局部作用域。
- 局部作用域优先于全局作用域。

### 三种作用域的区别：

+ if和for语句中定义的变量属于块级作用域，不属于局部作用域。
+ 子作用域可以访问到父作用域中定义的变量，父作用域也可以跨域访问到子作用域的变量。
+ var定义的变量，没有块的概念，可以跨块访问, 不能跨函数访问。
+ let定义的变量，只能在块作用域里访问，不能跨块访问，也不能跨函数访问。
+ const用来定义常量，使用时必须初始化(即必须赋值)，只能在块作用域里访问，而且不能修改。
+ 同一个变量只能使用一种方式声明，不然会报错。

## let:

- 声明变量，用法与var一致。
- 识别块级作用域，var不识别。
- 不能重复声明。
- 不存在变量提升（先访问后声明），会报错，var是undefined。
- let不会让变量泄露；而var会使变量发生泄露。

## const:

- 声明常量，一旦声明，就不能被改变。
- 声明常量的同时必须赋值，否则会报错。
- 可以识别块级作用域。
- 不能重复声明，不存在变量提升。

## 闭包函数：

> 两个发生嵌套的函数，内部函数引用外层函数的变量，外层函数调用内层函数。
>
> 闭包函数的用处：
> 1.可以读取函数内部的变量；
> 2.始终让这些变量的值保存在内存中，不会被外部函数调用后自动清除（即被垃圾机制进行回收）；
> 3.由于闭包会使得函数中的变量都被保存在内存中，内存消耗很大，在IE中可能导致内存泄露。解决方法是，在退出函数之前，将不使用的局部变量全部删除；
> 4.闭包会在父函数外部，改变父函数内部变量的值。所以，如果你把父函数当作对象（object）使用，把闭包当作它的公用方法（Public Method），把内部变量当作它的私有属性（private value），这时一定要小心，不要随便改变父函数内部变量的值。

```js
1.for(var i=0;i<divs.length;i++){
  (function(i){
    divs[i].onclick=function(){
      alert(i)
    }
  })(i)
  
  2.1.(for(var i=0;i<divs.length;i++){
    divs[i].onclick=(function(i){
      return fuction(){
        alert(i)
      }
    })(i)
  }

```



## 递归函数：

```js
function fn(num){
        if(num==1){
            return 1;
        }else{
            return num*fn(num-1);
        }
    }
```

## 匿名函数：

```js
function(){}
调用：1.自调用（function(){})() 2. let aa=function(){}
```

## 箭头函数：

```js
let aa=()=>console.log(123) 单行
let aa=()=>console.log{} 多行
```

## 内置底层函数：

> 内置：ECMAscript自带的函数，只要知道如何使用，不用关心如何封装。
>
> 顶层：在代码中任意位置均能使用。

- Escape():

> 将输入的字符串进行编码。

- Unescape():

> 将编码的字符串进行解码。

- Boolean():

> 将其余数据类型转换为布尔型。
>
> 0 undefined null NaN false " "都为false

- String();

> 将任意数据类型转化为字符串型。

- Number():

> 将其余数据类型转化为数值型。
>
> - null:0   " ":0  "    "=0  false:0   true:1
> - undefined:NaN  
> - 进制转换为十进制
> - 去掉没有意义的后导0
> - 字符串：规范的浮点数，数字型字符串。

- parseInt();

> 将字符串转化为整形。
>
> 第一个字母是数字，+，-， &nbsp，转换不成功，则为NaN。

- parseFloat();

> 将字符串转化为浮点数。
>
> 仅能转化规范的浮点数。转化不成功，返回NaN

- isNaN():

> 判断值是否能够转化为数值型，能转化为数值型返回false，不能转化为数值型的返回true。

## 数据类型转换：

- 强制类型转换。
- 隐式数据类型转换：算术运算符.逻辑运算符.条件if（）while（）

# 对象：

## 概念：

- 类：一群具有相同特征的对象集合的描述
- 对象：具体存在的对象个体
- 属性：对象基础信息的描述
- 方法:对象功能的描述

## 定义对象：

- 构造函数，实例化对象

```js
function Computer(){
   this.color=color；
  this.play=function(){
    console.log("上网")
  }
}
// 实例化对象
let ASUS=new Computer();

c.call("c") 括号里面是什么，指针指向谁
c.prototype={
  方法
}方法放在原型里面运行效率高

function each(num,callback){
            for (let i=0;i<num;i++){
                callback(i)
            }
        }


        each(10,function (index){
            console.log(index)
        })
```



- JSON

- class定义类，实例化对象

  

# URI和URL区别：

- url一般有三个部分组成，他们分别是服务类型+IP地址（有时有端口号）+主句资源的具体路径；
- uri也由三个部分组成，他们分别是访问资源的命名机制+资源存在的主机名+资源存放的路径；
- url是uri具体的子集，uri是一个抽象的概念，可以是绝对的，也可以是相对的，但是url必须是绝对的地址。