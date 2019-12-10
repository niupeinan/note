### css计算容器的高度：

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
    overflow:scroll;
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

