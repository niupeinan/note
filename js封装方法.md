#### 科学计数法修改数值：

```js
const scientificCounting = (num) => {
    if(!!num && !isNaN(num)){
                var p = Math.floor(Math.log(num)/Math.LN10);
                var n = num * Math.pow(10, -p);
                var number=new Number(n);
                if(p>=0){
                    p="+"+p;
                }
                return number.toFixed(2) + 'E' + p;
            } else {
                return 0;
            }
}
```

