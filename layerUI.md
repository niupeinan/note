#### onchange在layui中失效解决方法：

```js
<select lay-filte='test'></select>

var form = layui.form;
form.on("select(test)", function(data) {
    console.log(data)
})
```

