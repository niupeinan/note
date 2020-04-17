####  1、标题设置 

```js
title: {
    		id: '',       // 默认不指定。指定则可用于在 option 或者 API 中引用组件。
            show: true,   // 布尔值，是否显示标题组件
            text: '学生生源地来源分布图',   // 主标题，支持使用/n换行
            link: 'www.baidu.com',      // 主标题文本超链接
            target: '',                 // 指定窗口打开主标题超链接。'self' 当前窗口打开,'blank' 新窗口打开
            subtext: '模拟数据',          // 副标题
            // x 设置水平安放位置，默认左对齐，可选值：'center' ¦ 'left' ¦ 'right' ¦ {number}（x坐标，单位px）
            left : 'center',
            // y 设置垂直安放位置，默认全图顶端，可选值：'top' ¦ 'bottom' ¦ 'center' ¦ {number}（y坐标，单位px）
            top: 'top',
            right: '',
            bottom: '',
            // itemGap设置主副标题纵向间隔，单位px，默认为10，
            itemGap: 30,
            backgroundColor: '#EEE',
            // 主标题文本样式设置
            textStyle: {
              fontSize: 26,
              fontStyle = 'normal',
              fontFamily = 'sans-serif',
              fontWeight: 'bolder',
              color: '#000080'
              lineHeight: 56,
              rich: {
                  a: {
                        // 没有设置 `lineHeight`，则 `lineHeight` 为 56
                    }
              },
              width: 200，   // 文本宽度
              height: 200,   // 文本高度
            },
            // 副标题文本样式设置
            subtextStyle: {
              fontSize: 18,
              color: '#8B2323'
            }
          },
```

####  2、图例设置 

```js
legend: {
            // orient 设置布局方式，默认水平布局，可选值：'horizontal'（水平） ¦ 'vertical'（垂直）
            orient: 'vertical',
            // x 设置水平安放位置，默认全图居中，可选值：'center' ¦ 'left' ¦ 'right' ¦ {number}（x坐标，单位px）
            left: 'left',
            // y 设置垂直安放位置，默认全图顶端，可选值：'top' ¦ 'bottom' ¦ 'center' ¦ {number}（y坐标，单位px）
            top: 'center',
            itemWidth: 24,   // 设置图例图形的宽
            itemHeight: 18,  // 设置图例图形的高
            textStyle: {
              color: '#666'  // 图例文字颜色
            },
            // itemGap设置各个item之间的间隔，单位px，默认为10，横向布局时为水平间隔，纵向布局时为纵向间隔
            itemGap: 30,
            backgroundColor: '#eee',  // 设置整个图例区域背景颜色
            data: ['北京','上海','广州','深圳','郑州']
          },
```

####  3、值域设置 

```js
 series: [
            {
              name: '生源地',
              type: 'pie',
              // radius: '50%',  // 设置饼状图大小，100%时，最大直径=整个图形的min(宽，高)
              radius: ['30%', '60%'],  // 设置环形饼状图， 第一个百分数设置内圈大小，第二个百分数设置外圈大小
              center: ['50%', '50%'],  // 设置饼状图位置，第一个百分数调水平位置，第二个百分数调垂直位置
              data: [
                  {value:335, name:'北京'},
                  {value:310, name:'上海'},
                  {value:234, name:'广州'},
                  {value:135, name:'深圳'},
                  {value:148, name:'郑州'}
              ],
              // itemStyle 设置饼状图扇形区域样式
              itemStyle: {
                // emphasis：英文意思是 强调;着重;（轮廓、图形等的）鲜明;突出，重读
                // emphasis：设置鼠标放到哪一块扇形上面的时候，扇形样式、阴影
                emphasis: {
                  shadowBlur: 10,
                  shadowOffsetX: 0,
                  shadowColor: 'rgba(30, 144, 255，0.5)'
                }
              },
              // 设置值域的那指向线
              labelLine: {
                normal: {
                  show: false   // show设置线是否显示，默认为true，可选值：true ¦ false
                }
              },
              // 设置值域的标签
              label: {
                normal: {
                  position: 'inner',  // 设置标签位置，默认在饼状图外 可选值：'outer' ¦ 'inner（饼状图上）'
                  // formatter: '{a} {b} : {c}个 ({d}%)'   设置标签显示内容 ，默认显示{b}
                  // {a}指series.name  {b}指series.data的name
                  // {c}指series.data的value  {d}%指这一部分占总数的百分比
                  formatter: '{c}'
                }
              }
            }
          ],
```

####  4、提示框设置 

```js
tooltip: {
            // trigger 设置触发类型，默认数据触发，可选值：'item' ¦ 'axis'
            trigger: 'item',
            showDelay: 20,   // 显示延迟，添加显示延迟可以避免频繁切换，单位ms
            hideDelay: 20,   // 隐藏延迟，单位ms
            backgroundColor: 'rgba(255,0,0,0.7)',  // 提示框背景颜色
            textStyle: {
              fontSize: '16px',
              color: '#000'  // 设置文本颜色 默认#FFF
            },
            // formatter设置提示框显示内容
            // {a}指series.name  {b}指series.data的name
            // {c}指series.data的value  {d}%指这一部分占总数的百分比
            formatter: '{a} <br/>{b} : {c}个 ({d}%)'
          },
```

####  5、默认色板 

```js
color: ['#7EC0EE', '#FF9F7F', '#FFD700', '#C9C9C9', '#E066FF', '#C0FF3E']
```

####  6、整个图形背景颜色设置 

```js
backgroundColor: 'pink',
```

