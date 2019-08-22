

# DOM(文档对象模型)：

- window .onload =function(){}  事件源.事件=事件处理函数

## 获取元素：

- 获取id名的元素

```js
let box= document.getElementById("idName");
```

- 获取类名的元素  集合

```js
let obj= document.getElementsByClassName("className");   用-连接的style里面的属性值，第二个单词首字母大写。比如border-radius写成borderRadius.
```

- 获取标签名的元素  集合 下标 遍历

```js
let obj= document.getElementsByTagName("tagName");
```

- 指定范围获取元素

```js
let obj1=0bj.getElementsByClassName("");
```

- 获取选择器选中的第一个元素

```js
let obj=document.querySelector("选择器");
```



- 获取选择器选中的集合  下标 forEach

```js
let obj=document.querySelectorAll("选择器");
```



## 操作样式：

### 获取：

- 行内样式：obj.style.attr
- css样式和行内样式都可以：getComputedStyle(obj,null).attr

### 设置：

- 行内样式：

  ```js
  obj.style.属性名=属性值；
  ```

- 批量 样式：

  ```js
  obj.className="box"
  obj.classList.add("box")  添加新的类名，如已经存在，取消添加
  obj.classList.remove("box")  删除已经存在的类名
  obj.classList.toggle("box")  切换类名，即如果classList中存在给定的值，删除它，否则添加它。
  obj.classList.contains("box") 如果classList中存在给定的值，删除它，否则添加它。
  obj.id="box"
  ```

- 

### 操作内容：

- innerText：不能识别标签对
- innerHTML：识别标签对

### 操作属性：

- 标准属性：obj.attr
- 自定义属性：
  - 获取：obj.getAttribute(name)
  - 设置：obj.setAttribute(name,value)

# BOM(浏览器对象模型)

> 完成窗口与窗口之间的通信。window对象是 其核心对象。

- history
- location
- dom
- screen
- frames
- navigation

## window对象:

### 属性：浏览器宽高

- window.innerWidth 获取浏览器的宽度
- window.innerHeight获取浏览器的高度

### ie8浏览器以下

- document.documentElement.clientWidth 获取浏览器的宽度
- document.documentElement.clientHeight 获取浏览器的高度

### 浏览器左上角距离屏幕左上角的偏移量

- window.screenTop 垂直偏移量
- window.screenLeft 水平偏移量

### 方法：

- alert（）弹出框
- prompt（） 输入框
- confirm（）确定退出
- close（）关闭页面
- open（“url","","width=  height="） 打开页面
- setInterval（fn,1000） 隔一定时间重复不断地执行一个函数（fn，ms）
- clearInterval（t） 清除时间函数
- setTimeout（）隔一定的时间 只执行一次函数
- clearTimeout（t）清除时间函数

### 获取表单的值：

`obj.value`

## history对象：

### 属性：

- window.history.length 用来显示历史记录的长度

### 方法：

- history.forward() 前进
- history.back() 后退
- history.go(0)刷新

## location对象：

### 属性:

- location.href 设置或获取页面地址的。
- location.host 访问主机名加端口号。
- location.hostname 主机名
- location.port 端口号
- location.protocol 协议
- location.pathname 路径
- location.search 问号后的搜寻字段

### 方法：

- location.reload()  重新加载
- location.replace() 页面替换,不会增加历史记录
- location.assign("history.html") 页面替换，能够增加历史记录 

## 元素的尺寸和位置：

- obj.offsetWidth :获取元素的真实宽度（width+padding+border）
- obj.offsetHeight:获取元素的真实高度  
- obj.offsetLeft:当前元素的外边框到具有定位属性的父元素的内边框的水平距离。
- obj.offsetTop:当前元素的外边框到具有定位属性的父元素的内边框的垂直距离。
- obj.scrollTop:有滚动条的元素，浏览器滚动时在垂直方向的拉动距离；
- obj.scrollLeft:有滚动条的元素，浏览器滚动时在水平方向的拉动距离；

```js
document.body.scrollTop||document.documentElement.scrollTop
```



```js
eg:let box=document.querySelector(".box");
    let speedX=30;
    let speedY=20;
    let maxHeight=innerHeight-box.offsetHeight;
    let maxWidth=innerWidth-box.offsetWidth;
    setInterval(float,50);
    function float() {
        let newleft = box.offsetLeft + speedX;
        let newtop = box.offsetTop + speedY;
        box.style.top = newtop + "px";
        box.style.left = newleft + "px";
        if (newtop >= maxHeight) {
            speedY *= -1;
        }
        if (newleft >= maxWidth) {
            speedX *= -1;
        }
        if (newtop < 0) {
            speedY *= -1;
        }
        if (newleft < 0) {
            speedX *= -1;
        }
        window.onresize=function(){
            maxHeight=innerHeight-box.offsetTop;
            maxWidth=innerWidth-box.offsetLeft;
        }
    }
```

1.动态创建元素

```js
document.createElement('TagName');
```

2.添加类名

3.插入到页面

```js
父元素.appendChild（子元素）
document.body.appendChild(div);
```

# string类：

### 字符串常用属性：（查找对应字符和字符编码）

- charAt            字符串的位置

- charCodeAt 转换为字符编码

- Str.fromCharCode  利用字符编码找字符

- _proto_指向prototype原型

- test()   用于检验字符串是否符合某种规则

  ```js
  eg: var aa = /^[a-z]+$/
  	var bb = "fdsjf33"
      aa.test(bb)
  ```

### 字符串查找下标：

- str.indexOf("")        从前往后，查找对应字符的下标，如果有，返回下标，没有返回-1
- str.lastIndexOf("") 从后向前找，查找对应字符的下标，如果有，返回下标，没有返回-1
- str.search("")  同第一个，区别是正则
- str.match("")           正确返回数组，没找到null

### 字符串截取:

- str.substr(start,[length])
- str.substring(start,end)  从start开始截取，到end前结束
- str.slice(start,end)         数组的方法，同上
- str.trim()  去除字符串的头尾空格，不会改变原始字符串

### 字符串大小写转换：

- str.toLowerCase() 转化为小写
- str.toUpperCase()    转化为大写

### 字符串替换：

- str.replace("山"，”陕“)；

### 把字符串转换为数组：

```js
let str="1,2,3,4"  
arr=str.split(",")
```

# 节点：

> 文档节点  元素节点(标签)    属性节点 文本节点 注释节点

1.节点的信息属性

|          | nodeName   | nodeValue | nodeType |
| -------- | ---------- | --------- | -------- |
| 文档节点 | #document  | null      | 9        |
| 元素     | 大写标签名 | null      | 1        |
| 属性     | 大写属性名 | 属性值    | 2        |
| 文本     | #text      | 文本      | 3        |
| 注释     | #comment   | 注释内容  | 8        |

2.节点获取

1. document.childNodes 子节点
2. parentNode   父节点
3. previousSibling  获取上一个兄弟节点
4. nextSibling  获取下一个兄弟节点
5. previousElementSibling 上一个兄弟元素节点
6. nextElementSibling 下一个兄弟元素节点

### 创建节点：

```js
let div = document.createElement("div");
```

### 在最后插入节点：

>  appendChild()

```js
let box = documenet.querySelector(".box")
box.appendChild(div);
```

### 插入节点:

> insertBefore(要插入的元素，插入位置之后的元素)

```js
let span = document.createElement("span")
box.insertBefore(span,div)
```

### 创建文本节点：

```js
text1 = document.createTextNode("这是span标签")
span.appendChild(text1)
```

### 创建注释节点：

```js
let comment1 = document.creatComment("这是注释节点")
box.appendChild(comment1)
```

### 创建属性节点：

```js
let attr = document.createAttribute("id")
attr.nodeValue = "box"
```

### 设置属性节点:

```js
box.setAttributeNode(attr)
div.innerText = "this is div"
div.innerHTML = "<a href=\"\">百度</a>"
div.setAttribute("attr","小明")
getAttribute()：返回属性值，是一个文本字符串
getAttributeNode("属性名"）:返回属性节点，是一个对象
```

### 删除节点：

```js
box.removechild(div)
```

### 删除属性节点：

```js
box.removeAttribute("id");
```



# 事件：

## 事件添加方式：

- 节点.onclick=function(){}
- 节点.addEventListenter（“事件”，事件处理程序，[事件类型]）

## 事件构成：

- 事件源：谁去触发事件谁就是事件源。
- 事件
- 事件处理程序
- 先执行touch事件后再执行鼠标事件
- window["one"]()

## 常用事件（web）:

- 移动端事件
  - ontouchstart   按下
  - ontouchmove 移动
  - ontouchend 抬起
- 移动端常用的事件库：
  - FastClick.js ：解决CLICK事件300MS的延迟
  - TOUCH.js：百度云移动手势库
  - HAMMER.js  多点触控插件
  - Zepto.js        被誉为移动端的小型jQuery  
- 鼠标事件：
  - onclick               单击  
  - ondblclick          双击
  - onmousedown 按下
  - onmouseup      抬起
  - onmousemove 鼠标移动
  - onmouseover   移入
  - onmouseout     移出
  - onmouseenter  移入
  - onmouseleave  移出
  - document.oncontextmenu=function(e){e.preventDefault}   右击事件//阻止浏览器默认
  - onmousewheel 滚动事件
  - 触发事件的顺序：move down  up  click
- 鼠标事件对象中常用的属性：
  - clientX 距离浏览器的X轴偏移  
  - clientY  距离浏览器的Y轴偏移
  - offsetX 距离事件源X轴偏移
  - offsetY  距离事件源Y轴偏移
  - screenX  距离屏幕X轴偏移
  - screenY 距离屏幕Y轴偏移
- 事件对象：用来保存事件触发时的信息 
  - w3c : 事件处理程序的形参中
  - ie:  window.event
- 键盘事件：
  - onkeydown 键盘按下
  - onkeyup 键盘抬起  
  - onkeypress 键盘按下  （当按下功能键 ctrl shift delete esc 等不会触发）
- 键盘事件对象常用属性;
  - keyCode 键盘码
  - ctrlKey 是否按下ctrl
  - shiftKey 是否按下shift
  - altKey 是否按下alt       
  - key 键盘名 (event.key (键盘值))
- 表单事件：
  - oninput 输入
  - onchange 内容发生改变，并且失去焦点
  - onblur 失去焦点
  - onfocus 获得焦点
  - onsubmit 提交表单
  - onselect 文本选中
  - onchecked 选中表单控件
- 窗口事件：
  - onscroll
  - onload
  - onresize

## 事件流：

> 当触发一个事件时，由这个事件的容器到整个文档都会按照特定的顺序进行依次触发。

## 事件的分类：

- 捕获型事件：true 从大往小，即从不具体的事件源到具体的事件源
- 冒泡型事件：false 从小往大，即从具体的事件源到不具体的事件源

## 阻止事件流：

```js
wc3：event.stopPropagation();写在冒泡里面
let event =event=event || window.event
event.returnValue=true
```

## 事件委派：

event.target   目标事件源  ie浏览器：e.srcElement  

```js
eg1:
btn.onclick=function(){
		let div=document.createElement("div");
		div.className="con";
		box.appendChild(div);
	}
	box.onclick=function(event){
		if(event.target.className=="con"){
			event.target.style.background="red";
		}
	}
 eg2:
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>表单</title>
	<link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
</head>
<body>
	<table class="table table-bordered">
		<tr>
			<th>姓名</th>
			<th>联系电话</th>
			<th>操作</th>
		</tr>
		<tr>
			<td>011</td>
			<td>012</td>
			<td class="del"><button type="button" class="btn btn-danger">删除</button></td>
		</tr>
		<tr>
			<td>011</td>
			<td>012</td>
			<td class="del"><button type="button" class="btn btn-danger">删除</button></td>
		</tr>
		<tr>
			<td>011</td>
			<td>012</td>
			<td class="del"><button type="button" class="btn btn-danger">删除</button></td>
		</tr>
		<tr>
			<td>011</td>
			<td>012</td>
			<td class="del"><button type="button" class="btn btn-danger">删除</button></td>
		</tr>
	</table>
	<button class="add" type="submit">添加</button>
</body>
<script>
	let table=document.querySelector("table");
	let add=document.querySelector(".add");
	let del=table.querySelector(".del");
	table.ondblclick=function(event){
		let aa=event.target;
		if(aa.tagName=="TD" && aa.className!="del"){
			let input=document.createElement("input");
			input.className="form-control";
			input.value=aa.innerText;
			aa.innerText="";
			input.onblur=function(){
				aa.innerText=this.value;
			}
			aa.appendChild(input);
			input.focus();
		}
		if(aa.className=="btn btn-danger"){
			let row=aa.parentNode.parentNode;
			table.childNodes[1].removeChild(row);
		}
	}
	add.onclick=function(){
		let tr=document.createElement("tr");
		tr.innerHTML=`
			<td>011</td>
			<td>012</td>
			<td class="del">
				<button type="button" class="btn btn-danger">删除</button>
			</td>
			`
		table.childNodes[1].appendChild(tr);
	}

</script>
</html>
```

# 日期对象：

## 设置和获取时间：

```js
let ay = new date("2018/8/8 12:00:00")  
let ay2 = new date("12:00:00 2018/8/8")
let ay3 = new date("2018,0,8,12,0,0")  //月份从零开始
let now = new Date() //获取当前时间

now.setFullYear(2020)年  //设置格林尼尔时间,获取将set改为get
now.setMonth()月份
now.setDate() 日期
now.setHours()时
now.setMinutes()分
now.setSconds()秒
now.setMilliseconds()毫秒

now.setUTCFullYear();  //设置世界协调时,获取将set改为get
now.setUTCMonth()月份
now.setUTCDate() 日期
now.setUTCHours()时
now.setUTCMinutes()分
now.setUTCSconds()秒
now.setUTCMilliseconds()毫秒

now.getTime()   距离1970年1月一日零点零分零秒
```

```js
eg：时钟：setInterval(settime,1000);
	function settime(){
		let now = new Date();
		let hz = document.querySelector(".hz");
		let mz = document.querySelector(".mz");
		let sz = document.querySelector(".sz");
		h = now.getHours();
		m = now.getMinutes();
		s = now.getSeconds();
		console.log(h)
		hz.style.transform=`rotate(${30*h}deg)`
		mz.style.transform=`rotate(${6*m}deg)`
		sz.style.transform=`rotate(${6*s}deg)`
	}
	settime();
```

# 正则：

> 就是用来描述或者匹配一系列符合某种规则的字符串

## 作用：

- 数据验证
- 内容检索
- 内容替换
- 内容过滤

## 创建正则对象：

- 通过实例化对象

```js
let reg = new RegExp("正则表达式","模式修正符") //模式修正符包含： g 全局    i 不区分大小写   m 换行,多行
eg:let reg = new RegExp("uek","g")
```

- 通过字面量的方式：

```js
let reg = /正则表达式/模式修正符       //代表定界符
eg：let str = "ab1"
let reg = /\d/g
console.log(reg.exec(str))
```

## 正则中的数量：

### 贪婪原则:（尽可能多取）

- * 0个或多个       >=0  

```js
let phone = "12345678910";
let reg=/\d*/g
```

- +一个或多个     >=1
- ？0个或一个
- {11}
- {15,18}  15到18
- {6，}  至少为6个

### 吝啬原则:（尽可能少取）

- *？
- +？
- ？？
- {11，}？



```js
let str = "123456789741258"
let str1 = "1111111111111111111"
let reg = /[0-9]{15}/g
```

## 边界判断：

- ^ 开始
- $ 结束

```js
let str = "0351-541236"
let reg = /^0351-\d{6}$/g
```





## 正则对象的常用方法：

- test(str)      检测正则对象是否能够匹配str   返回值  true||false
- js中的正则是单行处理
- exec(str)     检测正则对象是否能够匹配str返回值  能匹配，返回一个拥有特殊属性的数组，不能匹配，返回null  

```js
let bool = reg.test("www.sxuek.com")
```

## 正则表达式：

> 使用场景:  1.正则对象   2.str.split(正则表达式)3.str.replace(正则对象，替换的内容) 4.str.search(正则表达式)

-  	原子 ：正则表达式中最小的内容
  - \d  0-9
  - \b 单词边界
  - \w 数字 字母 下划线
  - \s 空白       \n(空格)  \r(换行)  \t(制表符)
  - \D  除了0-9以外的字符
  - \B  非单词边界
  - \W 除了字母数字下划线以外的字符
  - \S   除了空白以外的字符

- 原子表：

  - [a-c]  a-c
  - [a-z] 小写字母
  - [a-zA-Z] 英文字母
  - [a-zA-Z0-9] 数字字母下划线

- 原子组：

  - ()默认存储到内存中，可以使用\1 \2等方式调用
  - （?:）可以使原子组不在内存中存储，不可以调用

  ```js
  let str1 = "陕西优逸客"
  let str1 = "山西优逸客"
  let reg = /(陕西|山西)优逸客/g
  
  let str1 = "<div>hello</div>"
  let reg = /<div>hello<\/div>/g
  or let reg = /<(div)>hello<\/\1>/g
  
  let str1 = "山西优逸客"
  let reg = /（?:(陕西|山西)优逸客）/g    ？：表示不能被引用
  ```

  

- 元字符：

  - . 点代表所有字符
  - | 或

```js
let str = "abcdef";
let reg = /[a-c]/g
```

## 留言板禁止内容：

```js
let con = document.querySelector("[name=con]");
	let reg = /毒品|枪支|法轮功/g
	con.oninput = function(){
		let bool = reg.exec(this.value);
		if(bool){
			this.value = bool[0].length>2?this.value.replace(bool[0],"***"):this.value.replace(bool[0],"**")
		}
	}
```

## 手机身份证邮箱正则：

```js
phone.oninput = function(){
		let reg = /^1[3587]\d{9}$/g
		let arr1 = reg.exec(this.value)
		if(!arr1){
			this.style.border="2px solid red"
		}else{
			this.style.border="2px solid green"
		}
	}
	card.oninput = function(){
		let reg1 = /^(\d{15}|\d{18}|(\d{17}[xX]))$/g
		let arr2 = reg1.exec(this.value)
		if(!arr2){
			this.style.border="2px solid red"
		}else{
			this.style.border="2px solid green"
		}
	}
	email.oninput = function(){
		let reg2 = /[a-zA-Z0-9][a-zA-Z0-9\.-_]{3,17}@(qq|163|Gmail)\.(com|cn)/g
		let arr3 = reg2.exec(this.value)
		if(!arr3){
			this.style.border="2px solid red"
		}else{
			this.style.border="2px solid green"
		}
	}
```

## 正则算法去除字符串空格：

```js
去除所有空格:
str   =   str.replace(/\s+/g,"");    
去除两头空格:
str   =   str.replace(/^\s+|\s+$/g,""); 
去除左空格：
str=str.replace( /^\s*/, ''); 
去除右空格：
str=str.replace(/(\s*$)/g, ""); 
```



