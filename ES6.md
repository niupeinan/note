### 变量let：

相对于传统的声明变量var来讲，主要存在以下的一些不同。

- let不存在预解析，即不存在变量提升。不然会报错。
- let不能在同一作用域下不能重复声明，不然会报错。
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
- 箭头函数本身没有arguments；
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
    constructor(a,b) {          // constructor方法是类的构造函数，是一个默认的方法，通过new命令创建对象实例时，自定调用该方法，每个类都必须要有这个方法。如果没有显示定义，一个默认的constructor方法会被默认添加。所以即使你没有添加构造函数，也还是会有一个默认的构造函数的。一般constructor方法默认返回实例对象this。也可以返回其他对象，让返回的对象不是该类的实例。
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

+ #### super

  + 当做函数使用

    ```js
    class A {}
    class B extends A {
      constructor() {
        super();  // ES6 要求，子类的构造函数必须执行一次 super 函数，否则会报错。
      }
    }
    
    // 在 constructor 中必须调用 super 方法，因为子类没有自己的 this 对象，而是继承父类的 this 对象，然后对其进行加工,而 super 就代表了父类的构造函数。super 虽然代表了父类 A 的构造函数，但是返回的是子类 B 的实例，即 super 内部的 this 指的是 B，因此 super() 在这里相当于 ```A.prototype.constructor.call(this, props)``。
    
    class A {
      constructor() {
        console.log(new.target.name); // new.target 指向当前正在执行的函数
      }
    }
     
    class B extends A {
      constructor() {
        super();
      }
    }
     
    new A(); // A
    new B(); // B
    
    // 可以看到，在 super() 执行时，它指向的是 子类 B 的构造函数，而不是父类 A 的构造函数。也就是说，super() 内部的 this 指向的是 B.
    
    ```

  + 当做对象使用

    ```js
    在普通的方法中，它指向父类的原型对象，在静态方法中，指向父类。
    class A {
      c() {
        return 2;
      }
    }
     
    class B extends A {
      constructor() {
        super();
        console.log(super.c()); // 2
      }
    }
     
    let b = new B();
    
    // 在上述代码中，子类B中的super当做一个对象使用。这是，super在普通方法中，指向A.prototype,所以super.c()就相当于A.prototype.c()
    
    通过super调用父类方法时，super会绑定子类的this。
    class A {
      constructor() {
        this.x = 1;
      }
      s() {
        console.log(this.x);
      }
    }
     
    class B extends A {
      constructor() {
        super();
        this.x = 2;
      }
      m() {
        super.s();
      }
    }
     
    let b = new B();
    b.m(); // 2
    
    // 上面代码中，super.s() 虽然调用的是 A.prototytpe.s()，但是 A.prototytpe.s()会绑定子类 B 的 this，导致输出的是 2，而不是 1。也就是说，实际上执行的是 super.s.call(this)。
    
    由于绑定子类的 this，所以如果通过 super 对某个属性赋值，这时 super 就是 this，赋值的属性会变成子类实例的属性。
    
    class A {
      constructor() {
        this.x = 1;
      }
    }
     
    class B extends A {
      constructor() {
        super();
        this.x = 2;
        super.x = 3;
        console.log(super.x); // undefined
        console.log(this.x); // 3
      }
    }
     
    let b = new B();
    
    // 上面代码中，super.x 赋值为 3，这时等同于对 this.x 赋值为 3。而当读取 super.x 的时候，调用的是 A.prototype.x，但并没有 x 方法，所以返回 undefined。
    ```

  + 使用super的时候，必须显示指定是否作为函数，还是作为对象使用，否则会报错。

    ```js
    class A {}
    class B extends A {
      constructor() {
        super();
        console.log(super); // 报错
      }
    }
    
    // 上面代码中，console.log(super); 的当中的 super，无法看出是作为函数使用，还是作为对象使用，所以 JavaScript 引擎解析代码的时候就会报错。这是，如果能清晰的表明 super 的数据类型，就不会报错。
    
    ```

  + 由于对象总是继承其他对象的，所以可以在任意一个对象中，使用 super 关键字。