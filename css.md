###  css计算容器的高度：

```css
只需设置样式使用calc() 函数，它支持 “+”, “-”, “*”, “/” 运算；
example： height: calc(100% - 50px)
```

#### 注意：

1. 运算符前后都需要保留一个空格，例如：width: calc(100% - 10px)；
2. 任何长度值都可以使用calc()函数进行计算；
3. calc()函数使用标准的数学运算优先级规则；
4. 它支持 “+”, “-”, “*”, “/” 运算

### 纯css固定表格表头，表头与表格对齐：

```css
//控制表格滑动

table tbody {
    display:block;
    height:450px;
    overflow-y:auto;
}

//固定表头

table thead, tbody tr {
    display:table;
    width:100%;
    table-layout:fixed;
}

//调节表头宽度

table thead {
    width: calc( 100% - 1.25em );
}
```

### animate:

```css
animation-fill-mode: none | forwards | backwords | both;
none: 不改变默认行为；
forwards: 当动画完成后，保持最后一个属性值（在最后一个关键帧中定义）；
backwards: 在animation-delay所指定的一段时间内，在动画显示之前，引用开始属性（在第一个关键帧中定义）；
both: 向前和向后填充模式都被应用。
```

#### object-fit属性：

- fill，默认值，替换内容拉伸填满整个content box，不保证原有的比例。
- contain， 保持原有尺寸比例，保证替换内容尺寸一定可以在容器里面放得下，因此此参数可能会在容器内留下空白。
- cover， 保持原有尺寸，保证替换内容尺寸一定大于容器尺寸，宽度和高度至少有一个和容器一致，因此此参数可能会让替换内容部分区域不可见。
- none，保持原有尺寸比例，同事替换内容原始尺寸大小。
- scale-down: 就好像一次设置了none或contain，最终呈现的是尺寸比较小的那个。

#### transform属性：

- rotate： 旋转
- skew：扭曲
- scale：缩放
- translate：移动
- matrix：矩阵变形

#### expression表达式解析：

- 可计算某个字符串，并执行其中的js代码；

- 语法： eval(string)参数

- 描述： string必需。要计算的字符串，其中含有要计算的js表达式或者要执行的语句；

- 返回值： 通过计算string得到的值（如果有的话）；

- 说明： 该方法只接受原始字符串作为参数，如果string参数不是原始字符串，那么该方法将不作任何改变的返回。因此请不要为eval()函数传递string对象来作为参数。如果试图覆盖eval属性或把eval()方法赋予另一个属性，并通过该属性调用它，则ecmascript实现允许抛出一个evalerror异常。

- 抛出： 如果参数中没有合法的表达式和语句，则抛出syntaxerror异常。

  如果非法调用eval(),则抛出evalerror异常

  如果传递给eval()的js代码生成了一个异常，则抛出syntaxerror,eval()将把该异常传递给调用者。

#### 移动端横屏和竖屏媒体查询：

```css
// 横屏展示：
@media screen and (orientation: landscape) {
    
}

// 竖屏展示：
@media screen and （orientation: portrait） {
    
}

// 客户端或大屏幕设备： 1280px至更大
@media screen and (min-width: 1280px) {
    
}
```

#### tofixed:

```
toFixed() 方法可把 Number 四舍五入为指定小数位数的数字。
Math.round() 四舍五入
```

#### 局部表格放大缩小功能：

```js
function setGesture(el){
    var obj={}; //定义一个对象
    var istouch=false;
    var start=[];
    el.addEventListener("touchstart",function(e){
        if(e.touches.length>=2){  //判断是否有两个点在屏幕上
            istouch=true;
            start=e.touches;  //得到第一组两个点
            obj.gesturestart&&obj.gesturestart.call(el); //执行gesturestart方法
        };
    },false);
    document.addEventListener("touchmove",function(e){
        e.preventDefault();
        if(e.touches.length>=2&&istouch){
            var now=e.touches;  //得到第二组两个点
            var scale=getDistance(now[0],now[1])/getDistance(start[0],start[1]); //得到缩放比例，getDistance是勾股定理的一个方法
            var rotation=getAngle(now[0],now[1])-getAngle(start[0],start[1]);  //得到旋转角度，getAngle是得到夹角的一个方法
            e.scale=scale.toFixed(2);
            e.rotation=rotation.toFixed(2);
            obj.gesturemove&&obj.gesturemove.call(el,e);  //执行gesturemove方法
        };
    },false);
    document.addEventListener("touchend",function(e){
        if(istouch){
            istouch=false;
            obj.gestureend&&obj.gestureend.call(el);  //执行gestureend方法
        };
    },false);
    return obj;
};
function getDistance(p1, p2) {
    var x = p2.pageX - p1.pageX,
        y = p2.pageY - p1.pageY;
    return Math.sqrt((x * x) + (y * y));
};
function getAngle(p1, p2) {
    var x = p1.pageX - p2.pageX,
        y = p1.pageY- p2.pageY;
    return Math.atan2(y, x) * 180 / Math.PI;
};

// 调用方法
var box=document.querySelector("#box");
    var boxGesture=setGesture(box);  //得到一个对象
    boxGesture.gesturestart=function(){  //双指开始
        box.style.backgroundColor="yellow";
    };
    boxGesture.gesturemove=function(e){  //双指移动
        box.innerHTML = e.scale+"<br />"+e.rotation;
        box.style.transform="scale("+e.scale+") rotate("+e.rotation+"deg)";//改变目标元素的大小和角度
    };
    boxGesture.gestureend=function(){  //双指结束
        box.innerHTML="";
        box.style.cssText="background-color:red";
    };
```

### tableLayout属性：

```js
// 固定表格布局
table-layout: fixed; //水平布局仅仅取决于表格宽度、列宽度、表格边框宽度、单元格间距，而与单元格的内容无关。

// 自动表格布局
table-layouy: automatic; // 列的宽度是由列的单元格中没有折行的最宽的内容决定的。
```

### position: sticky属性：

```css
它是position: relative和position：fixed的结合体。当元素在屏幕内，表现为relative,当就要滚出显示器屏幕时，表现为fixed.

sticky元素效果完全受制于父级元素们。
1. 父级元素不能有overflow：hidden设置，否则就没有粘滞效果。
2. 父级元素也不能设置固定的height高度值，否则也没有粘滞效果。
3. 同一个父容器中的sticky元素，如果定位值相等，则会重叠，如果属于不同父元素，则会鸠占鹊巢，挤开原来的元素，形成依次占位的效果。
4. sticky定位，不仅可以设置top,基于滚动容器上边缘定位；还可以设置bottom, 也就是响度底部粘滞。如果是水平滚动，也可以设置left和right值。
5. 当sticky元素的父元素已不再完整占据sticky元素的固定区域时，sticky元素不再固定
因此，
(1)父级元素的height必须超过sticky元素的height，这样在height范围内有粘滞效果。
(2)同一个父容器中的sticky元素，如果定位值相等，则会重叠；如果属于不同父元素，则会随着父元素不再完整占据sticky元素的固定区域以后，再由其他父元素的sticky子元素占据固定位置

```

#### @media screen和@media的区别？

```css
@media screen的css在打印设备里是无效的，而@media在打印设备是有效的。
@media only screen and关键词解析：
    only: 限定某种设备。
    and 被称为关键字，其他关键字还包括not(排除某种设备）
    braille 盲文
    enbossed 盲文打印
    handheld 手持设备
    print    文档打印或打印预览模式
    screen   彩色电脑屏幕
    try      固定字母间隔的网络的媒体，比如电传打字机
    tv       电视
    
  
```

#### 3D效果：

```css
1. 先设置旋转的容器： perspective属性设置透视距离就可以让里面的一张图片设置在后面而且不会被覆盖;要注意的是设置perspective属性的时候只能比盒子的大，不然盒子会变形，设置个100000px都没问题。
				   transform-style属性来设置成3D样式不然到时候设置里面小盒子的旋转平移的时候就会要在每个形变函数后面加上3D;这样就很麻烦;
2. translate正负值区分，x轴向右为正值， y轴向下为正值， z轴向外为正值；
   rotate正负值区分，x轴顺时针为正值， y轴逆时针为正值， z轴顺时针为正值；
					
```

```css
3D代码展示：
 <div id="box">
    <div class="box1" style="background: red;">帅</div>
    <div class="box2" style="background: blue;">帅</div>
    <div class="box3" style="background: pink;">帅</div>
    <div class="box4" style="background: purple;">帅</div>
    <div class="box5" style="background: yellow;">帅</div>
    <div class="box6" style="background: green;">帅</div>
    <div class="box7" style="background: #ff6700;">帅</div>
    <div class="box8" style="background: yellowgreen;">帅</div>
</div> 

 #box {
            width: 200px;
            height: 200px;
            position: relative;
            top: 200px;
            left: 500px;
            perspective: 100000;   /* 观察者的距离 */ 
            transform-style: preserve-3d;
            animation: name 8s linear infinite; 
      }

      #box div {
            position: absolute;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            text-align: center;
            line-height: 200px;
            font-size: 50px;
            color: white;
      }

      .box1 {
            transform: translate3d(-100px,0,200px);
      }  

      .box2 {
            transform: translate3d(100px,0,200px);
      }

      .box3 {
            transform: translate3d(200px,0,100px)rotateY(90deg);
      } 

      .box4 {
            transform: translate3d(200px,0,-100px)rotateY(90deg);
      } 

      .box5 {
            transform: translate3d(100px,0,-200px);
      } 

      .box6 {
            transform: translate3d(-100px,0,-200px);
      } 

      .box7 {
            transform: translate3d(-200px,0,-100px)rotateY(-90deg);
      } 

      .box8 {
            transform: translate3d(-200px,0,100px)rotateY(-90deg);
      } 

      @keyframes name {
            0%{
                  transform: rotateY(0deg);
            }
            33%{
                  transform: rotateY(120deg);
            }
            66%{
                  transform: rotateY(240deg);
            }
            100%{
                  transform: rotateY(360deg);
            }
      }
```

#### css实现三角形：

```css
<div class="trangle">

</div>

.trangle {
    width: 0px;
    height: 0px;
    border-top:200px solid transparent;
    border-right:200px solid transparent;
    border-bottom:200px solid green;
    border-left:200px solid transparent;
}
```

#### overflow:

```css
// 使用overflow时，height必须是固定的；如果设置height： auto；滚动调试条失效。
```

#### placholder样式：

```css
::-webkit-input-placeholder{
    color: #fff;        /* 使用webkit内核的浏览器 */
}    
:-moz-placeholder{
    color: #fff;        /* Firefox版本4-18 */
}                  
::-moz-placeholder{
    color: #fff;        /* Firefox版本19+ */
}                  
:-ms-input-placeholder{
    color: #fff;        /* IE浏览器 */
} 
```

#### margin: 百分比形式

```css
margin 的值是百分百的时候，其值是基于父元素的宽度来计算的，并非是自身的宽度，padding 百分比的取值也是一样的.
```

