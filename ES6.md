### 变量let：

相对于传统的声明变量var来讲，主要存在以下的一些不同。

- let不存在预解析，即不存在变量提升。不然会报错。
- let不能重复声明，不然会报错。
- let存在块级作用域。而var只有全局作用域和函数作用域，不存在块级作用域，容易造成变量泄露。

常量const同let相似，但是用常量声明的时候必须在声明时就赋值，不然会报错。

### 对象的解构赋值：

- #### 解构简单的JSON对象：

  ```js
  var object = {
      a:'a',
      b:'b',
  }
  let {a,b,c} = object
  console.log(a,b) //输出为字符串a和b
  console.log(c)   //输出为undefined
  
  let {a:A,b,c} = object     //自定义变量需要设置一个与json对象中已有值对应的名字。a:A就是相当于给object对象里面的a属性起了一个叫做A别名。
  console.log(A) //输出为字符串a
  console.log(a) //报错
  
  let a;
  let {a,b,c} = object
  console.log(a)   //报变量a已经被声明的错误
  console.log(c) 
  
  当声明的变量和从对象中引进的变量重复时，可以这样解决：
  let a;
  （{a,b,c} = object）
  ```

  

- #### 解构复杂的JSON对象

  ```js
  var obj = {
      arr: [
          'Yo.',
          {
              a: 1
          }
      ]
  }
  // Use Object Destructuring and Array Destructuring
  let {arr: [greet, a]} = obj;
  console.log("greet:", greet); // 输出为greet:Yo.
  console.log("a:", a);         //输出为a:1
  
  
  解构对象时处理默认值：
  let {a=4,b=10} = {a：5}
  console.log(a) //输出为5；这是因为后面初始化的值实际上是一个默认值，而对象中的值相当于给a赋值为5，后值覆盖前值，输出为5.相反如果对象中不含有变量c，但是对它进行赋值，能够打印初始化后的值，我理解的是相当于在该js文件里面声明了一个变量c。
  console.log(b) //输出为10
  ```

- #### 具体应用

  ```js
  //ES6语法
  let res = {
      status: 200,
      id: 12,
      data: [ {name: 'Bob'}, {name: 'EsunR'} ]
  }
  let {status, id, data} = res;
  if(status == 200){
      ...
  }
  
      
  //ES5语法
  let res = {
      status: 200,
      id: 12,
      data: [ {name: 'Bob'}, {name: 'EsunR'} ]
  }
  var status = res.status;
  var id = res.id;
  var data = res.data;
  if(status == 200){
      ...
  }
  
  ```

- #### 解构赋值（其他）

  ```js
  // 解构方法
  // ES5
  var len = 'yo.'.length;
  console.log(len);
  
  // ES6
  let {length} = 'yo.'
  console.log(length);
  
  // 将字符串转化为数组，数组结构赋值是按照顺序去进行的。
  let [a,b,c] = 'abc'
  
  // 参数的处理
  // ES5
  var arr = [1, 2];
  function test(a, b){
      console.log('a:', a);
      console.log('b:', b);
  }
  test(arr[0], arr[1])
  
  // ES6
  var arr = [1, 2];
  function test([a, b]){
      console.log('a:', a);
      console.log('b:', b);
  }
  test(arr);
  
  var obj = { b:2, a:1 }
  function test({a, b}){
      console.log('a:', a);
      console.log('b:', b);
  }
  test(obj);	
  ```


- #### 小结

  - {}  变量名必须和key值保持一致
  - []  名字的顺序和值的顺序要保持一致

### 将类数组转换为数组

- 使用Array.isArray(arr)函数判断传进去的arr是否是数组，返回布尔值。然后使用Array.from()方法可以将类数组转换为数组。
- 使用展开对象符，形式如...arr，可以将类数组转换为数组。

### 箭头函数

- 具有一个参数的简单函数；
- 没有参数的需要用在箭头前加上小括号；
- 多个参数需要用到小括号，参数间逗号间隔，例如两个数字相加；
- 函数体多条语句需要用到大括号；
- 返回对象时需要用小括号包起来，因为大括号被占用解释为代码块了；
- .直接作为事件handler；
- 作为数组排序回调；
- 指针this的指向，它一般指向上级对象。但是上级是比较龙笼统的说法。箭头函数this指向上级的级指的是函数作用域，是非箭头函数被function（）{}这个{}包裹的作用域，顶层是window。还有一个级指的是object对象嵌套层级。

### 模板字符串

+ 形式：`字符串${表达式}字符串`；
+ 支持换行；
+ 插值表达式：${表达式}，它并不接受if或者for语句等，它可以接受三元表达式，数组和函数的调用等。
+ repeat(): 该函数表示将某函数重复多少份，里面的参数代表份数。

### class构造函数

```js
class Fun {                     // class可以理解为一个语法糖，声明新的实例必须要使用new声明。
    constructor(a,b) {          // constructor，通过类的调用可以执行这个方法，每个类都必须要有这个方法。如果没有显示定义，则一个空的constructor被添加到类里面。constructor方法默认返回实例对象，即this。也可以返回其他对象。
        this.a = a;
        this.b = b;
    }
    showA() {
        console.log(this.a)
    }
}
var fun = new Fun(1,2);
fun.showA();
```

