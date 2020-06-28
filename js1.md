Javascript
node.js vue.js

shift+tab+delect:跳出当前页面(typora)

## 组成：

1.ECMAscript
 变量 数据类型 运算符 数组 函数 对象

2.BOM浏览器对象模型
 window对象 history对象 location对象

3.DOM文档对象模型
 元素获取 操作属性 操作样式 节点 事件 事件对象



## 作用：

1.数据验证

2.动态创建和删除元素

3.操作元素内容和样式

4.模拟动画

5.创建cookie

6.ajax

7.JSON格式的数据处理
....

## 特征：

客户端脚本语言，实现用户交互。

基于'对象'和'事件驱动'的'松散型''解释型'语言。

@import url('base.css'); 引入base。

## 移动端布局步骤：

> 视觉视口 布局视口 理想视口
>
> rem布局实现适配  rem.js      rem原理：root  em  html字体的倍率 
>
> em:当前字体的倍率   html{font-size:;} //设计稿和页面的倍率   

1. 修改视口

   ```html
   <meta name="viewport" content="width=device-width">
   ```

2. 引入rem.js

   ```html
   <script src=""></script>script>
   ```

3. 修改rem.js设计稿中的宽度

背景图片

```html
background:url() no-repeat bottom/contain,
//引入背景图片 禁止重复 位置（top bottom left right）
background-size：100% 100%；
//背景图片的大小
background-size：contain;
//按照宽高中的较大值进行缩放
background-size：cover;
//按照宽高中的较小值进行缩放
```

## 渐变

```css
background:linear-gradient(top,颜色1，颜色2，.....)
第一个参数：渐变开始的方向：top.left.bottom.right.25deg
颜色：red.#fff.rgb(0,0,0).rgba(0,0,0,0)
```

## 浏览器内核

- -webkit- 谷歌内核
- -moz- 火狐
- -ms- ie
- -o- 欧鹏

## 弹性布局

```html
display:flex;
//指定为弹性布局
justify-content:center;
//子元素在水平方向的对齐方式 居中对齐
align-items:center;
//子元素在垂直方向的对齐方式 居中对齐
```

   flex-shrink：0;即使空间不足，子元素不缩小。

   overflow-x:auto:超出部分在x方向的表现形式。

   auto：自动，如果超出自动以滚动条的形式显示。

  .recent-hours::-websit-scrolibar{height:0}去除滚动条  eg:.future ul::-webkit-scrollbar{
	height: 0;



## 组成：

 box-sizing ;

### 问题：

- 去除浏览器默认样式

  ```html
  *{
  margin:0;
  padding:0;
  }
  ```

- 页面中盒子的真实宽高。

- margic-top的BUG。

  - 用父元素的padding-top模拟子元素的margin-top
  - 给父元素添加overflow：hiddon；

- 行内标签只能设置左右，不能设置上下间距。

## flex布局：

### 注意点：

```css
父元素为flex布局时：
没有设置高度的子元素与父元素高度一致。
1，如果父元素设置固定高度，则子元素中没有设置高度的元素将继承父元素的高度；但是如果父元素的**align-items**设置以后那么子元素的高度则会有自身内容决定
2，如果父元素没有设置高度，其高度由最高的子元素决定。
```

### 容器的属性：

- flex-direction：决定主轴方向
  - row（默认值）：主轴为水平方向，起点在左端。
  - `row-reverse`：主轴为水平方向，起点在右端。
  - `column`：主轴为垂直方向，起点在上沿。
  - `column-reverse`：主轴为垂直方向，起点在下沿。

- flex-wrap：决定项目换行

  - wrap 项目换行
  - nowrap 项目不换行

- `flex-flow`属性是`flex-direction`属性和`flex-wrap`属性的简写形式，默认值为`row nowrap`。

- `justify-content`属性定义了项目在主轴上的对齐方式。
- flex-start`（默认值）：左对齐，主轴的起点`
  - flex-end`：右对齐，主轴的终点`
  - `center`： 居中，主轴的中心
  - space-between`：两端对齐，项目之间的间隔都相等。`
  - space-around`：每个项目两侧的间隔相等。所以，项目之间的间隔比项目与边框的间隔大一倍。
  
- `align-items`属性定义项目在交叉轴上如何对齐。 

  - flex-start`：交叉轴的起点对齐。
  - flex-end`：交叉轴的终点对齐。`
  - center：交叉轴的中点对齐。
  - baseline`: 项目的第一行文字的基线对齐。`
  - `stretch`（默认值）：如果项目未设置高度或设为auto，将占满整个容器的高度。

- `align-content`属性定义了多根轴线的对齐方式。如果项目只有一根轴线，该属性不起作用。 

  - `flex-start`：与交叉轴的起点对齐。
  - `flex-end`：与交叉轴的终点对齐。
  - `center`：与交叉轴的中点对齐。
  - `space-between`：与交叉轴两端对齐，轴线之间的间隔平均分布。
  - `space-around`：每根轴线两侧的间隔都相等。所以，轴线之间的间隔比轴线与边框的间隔大一倍。
  - `stretch`（默认值）：轴线占满整个交叉轴。

## 项目属性：

- order属性定义项目的排列顺序。数值越小，排列越靠前，默认为0。 
- flex-grow`属性定义项目的放大比例，默认为`0`，即如果存在剩余空间，也不放大。 `
- `flex-shrink`属性定义了项目的缩小比例，默认为1，即如果空间不足，该项目将缩小。 
- `flex-basis`属性定义了在分配多余空间之前，项目占据的主轴空间（main size）。浏览器根据这个属性，计算主轴是否有多余空间。它的默认值为`auto`，即项目的本来大小。
- flex`属性是`flex-grow`,?`flex-shrink`?和?`flex-basis`的简写，默认值为`0 1 auto`。后两个属性可选。`
- align-self`属性允许单个项目有与其他项目不一样的对齐方式，可覆盖`align-items`属性。默认值为`auto`，表示继承父元素的`align-items`属性，如果没有父元素，则等同于`stretch。
  - flex-start 交叉轴起点
  - flex-end交叉轴终点
  - center中心

## target：用来控制新页面中打开的位置

- ?    _self：在本窗口打开（默认值）
- _blank：在新窗口打开
- title:标题

### 阻止a标签页面刷新：

+ href = "javascript:void(0);"
+ href = "#",但是点击事见的函数需要返回false.

## 文本模型：

- ### 文本换行：

  ```css
  word-break:break-all;   //使非中日韩文本换行
  word-wrap:break-wrap;   //换行，但是和上面的区别是它会使整个单词换行
  ```

- ###  单行文本溢出:

  ```css
  // 进制换行
  white-space:nowrap;
  overflow:hidden;
  // 超出部分以省略号显示
  text-overflow:ellipsis;
  ```

- ### 多行文本溢出：

  ```css
  // 将盒子指定为弹性盒子
  display:-websit-box;
  // 在弹性盒模型中指定元素的排布顺序
  -websit-box-orient:vertical;
  // 指定文本溢出的行数
  -websit-line-clamp:3;
  height要是line-height的倍数
  line-height:70px;
  overflow:hidden;
  ```

## 表单控件：

- action:表单信息提交的位置 <form></form>

- method：提交的方式

  - ?	get:地址栏，信息少，安全性低
  - post:信息量多，比较安全

- 输入框 input

  ```css
  用户名：<input type=" text" placeholder="请输入用户名..." maxlength="10" value="" class="text" name="username" >
  placeholder:默认提示文本
  maxlength:规定输入的最大字符数
  name；和后台进行数据交互
  script:获取信息
  获取焦点：.text:focus{
    outline:none  //外边线消失
  }
  ```

- 密码框password 行内块标签

  ```css
  <br>
  密&nbsp;码<input type="password" placeholder="请输入密码" name=“psw”>
  <br>
  //单选按钮 name属性的值要相等
  请选择你的性别：
  <label for="man">
  男：<input type="radio" name="sex" id="man" checked//默认选择>
  </label>
  <label for="woman">
  女：<input type="radio" name="sex" id="woman">
  </label>
  // 多选按钮
  请选择你喜欢的音乐：
  摇滚<input type="checkbox" checked>
  // 下拉框
  请选择你的学历：
  <select name="" id="">
  	<option value="">硕士</option>
  </select>
  // 文件
  请上传照片：<input type="file">;
  // 留言板（）文本域
  <textarea name="" id="" cole="" rows=""></textarea>
  textarea{
    resize:none/both/vertical/horizontal;//是否允许用户重新设置大小。不允许/都可以/只能垂直方向/只能水平方向
  }
  //重置按钮
  <input type="reset">
  //提交按钮
  <input type="submit">
  //自定义按钮
  <input type="button" value="按钮">
  <button>搜索</button>
  //颜色
  <input type="color">
  //时间日期
  年月<input type="month">
  年周<input type="week">
  时分<input type="time">
  年月日<input type="data">
  年月日时分<input type="datatime-local">
  //音频视频
  <audio src="1.mp4" controls loop><audio>
  <video src="1.mp4" controls loop><video>
  controls:控件向用户显示
  loop:循环播放
  autoplay:当页面加载完成后自动播放
  //验证
  <input type="email">
  <input type="tel" autofocus>
   autofocus:自动获取焦点
  ```

##  h5语义化标签 块标签

- \<header>头部</header>

- \<nav>导航</nav>
- \<aside>侧导航</saide>
- \<section>页面中的某一部分</section>
- \<footer>底部</footer>
- \<main>主体</main>

## location.href总结:

```js
"top.location.href"是最外层的页面跳转
"window.location.href"、"location.href"是本页面跳转
"parent.location.href"是上一层页面跳转.
```

## window.location.href和window.open的区别:

```js
window.location是window对象的属性，而window.open是window对象的方法 
window.location是你对当前浏览器窗口的URL地址对象的参考！   
window.open是用来打开一个新窗口的函数！

window.open不一定是打开一个新窗口!!!!!!!!   
只要有窗口的名称和window.open中第二个参数中的一样就会将这个窗口替换，用这个特性的话可以在iframe和frame中来代替location.href。 
如<iframe name="aa"></iframe>   
  <input type=button   onclick="window.open('1.htm','aa','')">和   
  <input type=button   
   onclick="self.frames['aa'].location.href='1.htm'">的效果一样 

window.open 用来打开新窗口 
window.location 用来替换当前页，也就是重新定位当前页 
    可以用以下来个实例来测试一下。 
<input type="button" value="新窗口打开" onclick="window.open('http://www.google.com')"> 
<input type="button" value="当前页打开" onclick="window.location='http://www.google.com/'"> 
    
window.location或window.open如何指定target?
这是一个经常遇到的问题，特别是在用frame框架的时候
解决办法:
1.window.location 改为 top.location　即可在顶部链接到指定页  
2.window.open("你的网址","_top"); 

window.open 用来打开新窗口 
window.location 用来替换当前页，也就是重新定位当前页 

用户不能改变document.location(因为这是当前显示文档的位置)。 
window.location本身也是一个对象。 

但是,可以用window.location改变当前文档 (用其它文档取代当前文档),而document.location不是对象。 
服务器重定向后有可能使document.url变动,但window.location.href指的永远是访问该网页时用的URL. 
大多数情况下,document.location和location.href是相同的，但是，当存在服务器重定向时，document.location包含的是已经装载的URL，而location.href包含的则是原始请求的文档的URL.

window.open()是可以在一个网站上打开另外的一个网站的地址 
window.location()是只能在一个网站中打开本网站的网页 
```

