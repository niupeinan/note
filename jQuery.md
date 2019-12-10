# jQuery:

> 本质：JavaScript框架
>
> 宗旨：write  less        do   more  
>
> 作用：优化js操作，页面交互，事件，ajax , 动效
>
> 特性：隐式循环，链式调用

- 隐式迭代代码理解：

  ```js
  // 原生js代码
  var primary = document.getElementsByClassName('primary');
  for(var i = 0, len = primary.length; i < len; i++) {
      primary[i].style.color = '#188eee';
  }
   
  // jQuery
  $('.primary').css('color', '#188eee');
  ```

  

- 链式调用代码理解：

  ```js
  // 原始版
  $('div').hide(); //隐藏页面上所有的div元素
  $('div').text('new content'); //更新所有div元素内的文本
  $('div').addClass("updatedContent"); //在所有的div元素上添加值为updatedContent的class属性
  $('div').show(); //显示页面上所有的div元素
   
  // 重写版，链式
  $('div').hide().text('new content').addClass("updatedContent").show();
   
  // 缩进版
  $('div')
    .hide()
    .text('new content')
    .addClass("updatedContent")
    .show();
  
  // 这是应为每个方法都返回了this类。
  
  如果用原始的代码可以这样理解：
  // 定义类
  function Person(opt) {
      this.name = opt.name;
      this.age = opt.age
  }
   
  // 定义 getName 方法
  Person.prototype.getName = function() {
      console.log(this.name);
      return this; // 返回 this 对象
  }
   
  // 定义 sayHello 方法
  Person.prototype.sayHello = function() {
      console.log('hello the world');
      return this; // 返回 this 对象
  }
   
  // 新建一个叫 next 的 Person 类
  var next = new Person({
      name: 'next'
  });
   
  // 链式调用 getName 和 sayHello 方法
  next.getName().sayHello();
  ```

  

- 将原生的单个化操作变成批量操作

- 将原生的复杂查询方式（兼容），简单化

- 将原生逐步操作的方式，链式的操作

- 将原生操作复杂的逻辑，提供简单的接口

- 只专注于业务的逻辑，语法的问题

- 是单线程异步机制的语言

  > 单线程：程序同一时间只能执行同一件事情。
  >
  > 异步机制：把需要耗费时间以及不确定的时间的代码，放到异步执行，交替执行
  >
  > 先执行线程上的正常代码，把需要耗费时间的或者不确定时间的代码放到一个数组中，但是此时不执行，当线程上的正常代码执行完成后，在异步执行，在时间间隔内执行其他的，是交替执行的。
  >
  > 优点：极少的资源做更多的事情，单线程模拟多线程
  >
  > 回调地狱

- jquery三种队列：animate “fx”  "自定义队列"       级别从高到低，又分为入队和出队  

  animate会自己入队和出队

```js
$(function(){
  $("div")
  .css("background-color"："red")
  .animate("margin-left":100,1000)
})
```





# jQuery核心函数：

- 选择器，返回jQuery对象
- 函数，给document添加ready事件

```js
jQuery(function(){})
jQuery("document").ready(function(){})
jQuery().ready(function(){})
```

- 传入dom对象，返回jQuery对象
- 传入字符串“<div></div>”,创建新的节点

```js
$("<div></div>").appendTo();
```

- $可替代jQuery

## jQuery对象常用方法：

- .css("样式属性"，"样式值");

```js
$(function(){
  $(".box").css({
    "backgroundColor":"blue",
  })
})
```

- .css({})

## jQuery对象筛选方法：

- get  表示取得第几个匹配的元素，返回dom对象
- eq  表示取得第几个匹配的元素，返回的是jquery对象
- .first()
- .last()
- .hasClass("类名")  判断jQuery数组中是否有一个类名为***的对象
- .filter([ 选 择 器][ ,元素][,function])  筛选出符合对象的类名

```js
return $(this).attr("class", "box");//修改类名
```

- .is("选择器") 判断是否为某一个对象
- .map(fn) 遍历对象生成一个新的数组。
- .has("选择器") 返回一个选中的jQuery对象
- .not("选择器") 从jQuery数组中删除选中的元素
- .slice(start[,end])  截取指定位置的jQuery对象
- .each(index,item) 遍历jQuery数组，index在前，item在后
- .index() 返回jQuery对象在数组中的下标

## 操作属性的方法：

- attr()
- removeAtrr()
- prop()
- removeProp()

## 常用方法：

- .toArray 将jQuery对象转换为原生数组对

## 操作类名的方法:

- addClass()   
- removeClass()
- toggleClass()  有就删除，没有就添加 

##  操作内容的方法：

- .text()   设置或返回被选元素的文本内容
- .html()   返回或设置被选元素的内容 (inner HTML)，包括标签。（识别标签对）
- .val()   表单控件,返回或设置被选元素的值。

## jQuery对象元素信息：

- .offset  返回一个位置信息的对象（top:**,left:）**相对于浏览器位置
- .position 返回一个位置信息的对象（top:**,left:*）相对于定位的祖先元素的位置
- .scrollTop()
- .scrollLeft(c)

## 事件对象：

- e.offsetX
- e.offsetY
- e.pageX
- e.pageY
- e.target
- e.currentTarget
- e.stopPropagation()
- e.preventDefault()

## 事件：

- one()
- on()   如果是通过动态添加的元素，需要绑定到它的父级或者body绑定on方法。
- trigger() 自动触发事件
- triggerHandler 自动触发事件，并且清除浏览器行为

## ajax:

> dataType:"jsop",

```js
$(".btn").click(function(){
        $.ajax({
            url:"https://www.toutiao.com/stream/widget/local_weather/city/",
            dataType:"jsonp",
            success:function(data){
                console.dir(data.data["山西"])
            },
            error:function(){
                console.log("no")
            }
        })
    })

```

### $()里面传入元素：

- 字符串
  - 选择器    要将选择器指向的内容放到jQuery对象里面
  - 标签      创建一个新的元素  
- underfined    返回个空的jQuery 对象
- 函数          这个函数在页面加载完成后执行  
- dom         将这个原生的对象放入到jquery对象中  

## 队列：

- queue

- dequeue

- clearQueue

- stop() 结束当时正在进行的进程

- stop(true) 结束正在进行的所有进程

- finish

- 实现队列的原生代码：

  ```js
  var div = document.querySelector("div");
      animate(div,{
          width:400,
      },2000,function(){
          animate(div,{height:400},1000,function(){
          })
      });
      function animate(obj,attrobj,duration,callback){
          var starts = {};
          var changes = {};
          for(var i in attrobj){
              starts[i] = parseInt(getComputedStyle(obj,null)[i]);
              changes[i] = attrobj[i] - starts[i];
              console.log(changes[i])
          }
          var time = 0;
          var t = setInterval(function(){
              time += 40;
              if(time>=duration){
                  clearInterval(t)
                  for(var i in attrobj){
                      obj.style[i] = attrobj[i] + "px";
                      if(callback){
                          callback()
                      }
                  }
              }else{
                  for(var i in attrobj){
                      obj.style[i] = changes[i] * time/duration + starts[i] + "px";
                  }
              }
          },40)
      }
  ```

## jquery扩展方法

- 类级别的扩展方法

  - 添加一个新的全局函数

    ```js
    $.foo = function() {
        alert("foo")
    }
    
    调用方法： $.foo();
    ```

  - 使用jquery.extend(obj);

    ```js
    $.extend({
        foo: function() {
            alert("foo")
        },
        bar: function() {
            alert("bar")
        }
    })
    
    调用方法： $.foo()
    		 $.bar()
    ```

  - 使用命名空间

    ```js
    $.myPlugin = {
       foo: function() {
            alert("foo")
        },
        bar: function() {
            alert("bar")
        } 
    }
    
    调用方法： $.myPlugin.foo();
    		 $.myPlugin.bar();
    ```

- 对象级别的扩展方法

  ```js
  $.fn.foo = function(){
  			alert("hello jquery");
  		}
  		$(‘#myF‘).foo()
            
  
   (function($){   
  			$.fn.extend({   												   							pluginName:function(opt,callback){   
  					alert("foo");   
  				}   
  			})   
  		})(jQuery);  
  		$("#myF").pluginName();
  
  
  
  (function (jq) { 
  			jq.fn.foo = function (obj) { 
  				alert(obj);
  			}; 
  		})(jQuery) 
  		$("#myF").foo("hello jquery");
  ```


### $(...)[0].css is not a function报错？

```js
解决： 直接获取到的$(".box")是dom对象，并不是jquery对象，所以无法调用jquery的方法。
```

