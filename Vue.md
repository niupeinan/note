##  VUE简介:

+ 缺点：首页的加载速度慢

+ 三大核心：组件 路由和状态管理，路由控制页面的渲染，页面由组件组成，数据由vuex进行管理和改变。

+ 敏捷开发  模块化开发   组件化开发

+ 组件：完整的结构，逻辑，数据

+ ```js
  <div class="app">
      <input v-model="one" type="text"/>+   /*v-model 指令 ，表单内部获取数据,它是表单上面的指定，双向数据绑定*/
      <input v-model="two" type="text"/>=   /*表单外部用{{}}获取数据或者用v-text代替*/
      <span v-text="result()"> </span>
  </div>
  </body>
  <script>
      new Vue({
          el:".app",  /*接管的范围*/
          data:{       /*json格式，接收数据*/
              one:0,
              two:0
          },
          methods:{   /*methods存放操作逻辑，前面result（）*/
              result(){
                  if(this.one>10){
                      return this.one*1+this.two*1
                  }else{
                      return this.one*1-this.two*1
                  }
              }
          },
          computed:{   /*computed,动态变化的数据，前面result，前面修改数据，只会运行修改过的内容*/
              result(){
                  if(this.one>10){
                      return this.one*1+this.two*1
                  }else{
                      return this.one*1-this.two*1
                  }
              }
          },
          watch:{   /*json格式，手动去实时监控数据的变化 */
              one(one,two){
                  this.result = this.one*1 + this.two*1  /*one修改后的值，two是修改后的值*/
              },
              two(one,two){
                  this.result = this.one*1 + this.two*1
              }
          }
      })
  ```

  ```js
  v-for 循环
      v-on：click或者@click="add"  点击事件
      v-show:开关的作用,true是返回display:block
      @keydow.13  回车的意思
      v-html
      ：代表v-bind的意思
      调用函数的三种方式：
      	1.自调用
      	2.直接调用
      	3.点击事件调用
      	eg：
      	function aa(){}
      		1.(function aa(){})()
      		2.aa()
      		3.div.onclick=aa
      localStorage存放的数据类型是字符串
      1.localStorage.aa = bb;	
      2.localStorage.setItem("aa","cc")
      3.localStorage.removeItem("aa","cc")
      4.localStorage.clear()清除所有
      JSON.stringify(value[, replacer [, space]])将对象、数组转换成字符串（系列化对象，将对象数据类型转化为数据类型）；
      1.布尔值、数字、字符串的包装对象在序列化过程中会自动转换成对应的原始值；
      2.undefined、任意的函数以及 symbol 值，在序列化过程中会被忽略（出现在非数组对象的属性值中时）或者被转换成 null（出现在数组中时）；
      3.不可枚举的属性会被忽略；
      4.
      JSON .parse()将字符串转成json对象。
      ///////自定义指令的创建//////////
      Vue.directive("focus",{
          inserted:function (val) {
              console.log(val)    /*val中存储了所有使用这个指令的页面元素 */
              val.focus();
          }
      });
     
  ```

  ```js
  <div class="table">
          <table>
              <tr>
                  <th>ID</th>
                  <th>姓名</th>
                  <th>年龄</th>
              </tr>
              <tr v-for="item in datas">
                  <td>
                      {{item.id}}
                  </td>
                  <td>
                      {{item.name}}
                  </td>
                  <td>
                      {{item.age}}
                  </td>
              </tr>
          </table>
          <div class="add">
              id:<input type="text" v-model="id">
              name:<input type="text" v-model="name">
              age:<input type="text" v-model="age">
              <button @click="add()">添加</button>
          </div>
      </div>
      <script>
          new Vue({
              el:".table",
              data:{
                  id:"",
                  name:"",
                  age:"",
                  datas:[
                      {id:1,name:"张三",age:20},
                      {id:2,name:"李四",age:20},
                      {id:3,name:"王五",age:21},
                      {id:4,name:"赵六",age:22}
                  ]
              },
              methods:{
                  add(){
                      var obj ={};
                      obj.id = this.id;
                      obj.name = this.name;
                      obj.age = this.age;
                      this.datas.push(obj)
                  }
              }
          })
      </script>
  ```

  

## 数据双向绑定：

```vue
//  四个选项，两个方法 

var temp;
    var obj={};
    Object.defineProperty(obj,"name",{
        value:100,
        writable:true,    //可以修改的，默认是false
        configurable:true,   //可以删除的
        enumerable:true,     //可以循环的
        set:function(val){ 
            if(temp!=val){
                document.querySelector("div").innerHTML=val;
            }//与value和writable冲突，不能同时出现，设置值执行set(),获取值执行get()
            temp = val;
        },
        get:function(){
            return temp;
        }
    })
    console.log(obj.name)
    obj.name=200
    console.log(obj.name)
```

## 创建vue项目：

```vue
1.下载node.js,使用命令pip install node
2.下载vuecli,可以使用命令npm install -g @vue/cli
3.使用vue创建项目：vue create project-name
4.运行项目：npm run serve
```

## vuecli知识点:

```vue
卸载老版本：
npm uninstall vue-cli -g
yarn global remove vue-cli 
安装新版本：
npm install -g @vue/cli
yarn global add @vue/cli
创建项目：
vue init webpack project-name
vue create project-name

```

## export与export default区别：

- export与export default均可用于导出常量、函数、文件、模块等 
- 你可以在其它文件或模块中通过import+(常量 | 函数 | 文件 | 模块)名的方式，将其导入，以便能够对其进行使用 
- 在一个文件或模块中，export、import可以有多个，export default仅有一个 
- 通过export方式导出，在导入时要加{ }，export default则不需要 

## vue文件存放内容：

1. assets   用来存放静态资源   img ,css ,js

2. components   用来存放项目的组件 

3. app.vue:是项目入口文件 ,

4. App.vue相当于一个组件 ,

5. main.js是项目的核心文件 ,
   1. import Vue from ‘vue’     引入vue,
   2.   import App from ./App’  ./App   即App.vue文件‘ 
   3. import router from ‘./router ’   引入一段路由配置。 
   4. 然后是实例化new Vue .el:’#app’意思谁将所有的组件都放在id为app的元素中。components表明引入的文件，此处就是app.vue这个文件,这个文件的内容将以这样的标签写进#app中。 

6. static文件夹用来放置静态资源目录 

7. index.html是首页入口文件 

8. package.json是项目配置文件 

9. 安装完node之后，npm包含的很多依赖包是部署在国外的。所以我们要安装cnpm，cnpm是淘宝对npm的镜像服务器，这样依赖的包安装起来就快多了。
   安装命令为：npm install -g cnpm --registry=[https://registry.npm.taobao.org](https://registry.npm.taobao.org/)

    

## ajax解决跨域问题：

- jsonp  快捷一点  有着诸多限制   局限性：自己有权限操作的两个域名或者对方配合的服务
  - script  src="  " 通过script标签获取的内容，会当做js代码执行
- 代理   流程比较复杂 几乎没有限制 缺点：效率慢，开发慢 原理：python具有客户端的能力。  

## jsonp:

```py
概念：它是在文档中插入一个script标签，创建_callback方法，通过服务器配合执行_callback方法，并传入一些参数

 JSONP的优点是：它不像XMLHttpRequest对象实现的Ajax请求那样受到同源策略的限制；它的兼容性更好，在更加古老的浏览器中都可以运行，不需要XMLHttpRequest或ActiveX的支持；并且在请求完毕后可以通过调用callback的方式回传结果。

JSONP的缺点则是：它只支持GET请求而不支持POST等其它类型的HTTP请求；它只支持跨域HTTP请求这种情况，不能解决不同域的两个页面之间如何进行JavaScript调用的问题。

三种形式：
第一种形式：
1.HTML：
<script>
    function aaa(con){
        document.querySelector("div").innerHTML = con;
    }
</script>
<script src="http://127.0.0.1:9000/abc?callback=aaa"></script>
2.python:
@app.route("/abc")
def abc():
    fn = request.args.get("callback")
    return fn+"('ccc')"
 
第二种形式：
jquery:
$.ajax({
        url:"http://127.0.0.1:9000/abc?callback=callback",
        datatype:"jsonp",
        callback:"callback",
        success(e){
            $("div").html(e)
        }
    })
python:
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("ajax1.html")
@app.route("/abc")
def abc():
    return "ccc"

app.run(port=9000)

代理：
html:
var ajax = new XMLHttpRequest();
    ajax.onload = function(){
        console.log(ajax.response)
    };
    ajax.open("get","/ajax?http://127.0.0.1:9000/abc");
    ajax.send()
python:
from flask import Flask,render_template,request as request1
from urllib import request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("ajax2.html")
@app.route("/ajax")
def ajax():
    url = request1.args.get("vue");
    res = request.urlopen(url)
    con = res.read()
    con.decode("utf8")
    return render_template("ajax2.html")

app.run()
```

## this.$router.push.replace.go的区别：

1.this.$router.push()

描述：跳转到不同的url，但这个方法会向history栈添加一个记录，点击后退会返回到上一个页面。

2.this.$router.replace()

描述：同样是跳转到指定的url，但是这个方法不会向history里面添加新的记录，点击返回，会跳转到上上一个页面。上一个记录是不存在的。

3.this.$router.go(n)

相对于当前页面向前或向后跳转多少个页面,类似 `window.history.go(n)`。n可为正数可为负数。正数返回上一个页面。

## VUE创建组件：

```vue
var obj = {}
obj.install = function(Vue,params){
vue.prototype.abc=function("aa:"bb"){
	alert("params.aa")
}
}
如果创建组件时使用驼峰命名，调用组件的时候需要将驼峰改为横线-写法
```

## Vuex

- ### 什么是vuex？

  - 它是应用程序开发的状态管理模式；
  - 它采用集中式存储管理应用的所有组件的状态；
  - 并以相应的规则保证状态以一种可预测的方式变化。

- ### 什么是状态管理模式？

  - state:驱动应用的数据源。
  - view:以声明的方式将state映射到视图。、
  - actions:响应在view上的用户输入导致的状态变化。

## Vuex的小实例：

```js
1. 下载vuex的插件，使用命令npm install vuex --save;
2. 在main.js中引入插件，import Vuex from 'vuex',并且注册Vue.use(vuex),并且将它挂载到dom里面。
3. 使用vuex。store是仓库，用来存放关于vuex的数据源以及它的各种方法。
const store = new Vuex.Store({    // 是对象的形式
    state: {
        count: 0,    //数据源
    }，
    mutations: {
        increase(state) {
			state.count++
    	}
	}
})
4.在全局获取状态对象可使用this.$store.state.count;
5.在全局方法触发状态变更可以使用this.$store.commit('increase',v);v是可以传入的数据。
6.引入vuex中的mapState函数。该辅助函数是帮助我们生成计算属性 
import { mapState } from 'vuex'
computed：mapState({
    count:state => state.count,//使用箭头函数使代码更加简练
    countAlias:'count',  // 该字符串参数’count'等同于state => state.count
    countPlusLocalState （state）{
    	return state.count+this.count  // 使用常规函数，可以使用’this‘的局部状态
})
7.
	

```

## element:

```vue
注意点： <span v-if="data.type==1">文件夹：{{ node.label }}</span>
        <span v-else>文件<a href="">{{ node.label }}</a></span>
				<router-view to="/addcategory"></router-view>
export default {

        data() {
            return {}

    },
        computed:{
            data5(){
                return  this.$store.state.menus
            }
        },
        methods: {
          append(data) {
            const newChild = { id: id++, label: 'testtest', children: [] };
            if (!data.children) {
              this.$set(data, 'children', []);
            }
            data.children.push(newChild);
          },

          remove(node, data) {
            const parent = node.parent;
            const children = parent.data.children || parent.data;
            const index = children.findIndex(d => d.id === data.id);
            children.splice(index, 1);
          },


            submit(){
              return this.$router.push("/addcategory")
            }

        }
    }

<template>
    <div>
        <input type="text" v-model="cname">
        <el-radio v-model="type" label="1">文件夹</el-radio>
        <el-radio v-model="type" label="2">文件</el-radio>
        <el-button @click="temp()">提交</el-button>
    </div>
</template>
<script>
    export default {
        data(){
            return{
                cname:"",
                type:"1",
            };
        },
        methods:{
            temp(){
                this.$store.state.menus.push({"type":this.type,"label":this.cname})
            }
        },
    }
</script>
```

## ref属性：

```vue
比如：有时候我们想在父组件中调用子组件的方法或属性，这个时候该怎么做呢？可以通过为子组件设置ref，然后通过this.$refs.refName（refName为子组件的ref值）获取到子组件，然后就可以随意调用子组件的方法和属性了。又比如：有时候我们想操作子组件或HTML标签的DOM，在vue中我们几乎不使用class或id来获取元素的DOM，这个时候该怎么做呢？可以为子组件或想要操作的DOM标签添加ref属性，然后通过this.$refs.refName.$el或者this.$refs.refName来获取DOM。

那么在使用ref时要注意什么呢？

根据ref使用的对象不同，获取到的结果也是不一样的：

<1> 自定义组件使用ref属性，通过ref值可获取到该自定义组件；

<2> 普通HTML标签使用ref属性，通过ref值获取到的是该标签对应的DOM
    
    
```

## Promise:

Promise:一套处理异步情况的方法。先创建一个promise对象来注册一个委托，其中包括委托成功和失败后的处理函数。然后基于这种表述方式，；来讲promise应用到各种异步处理的情况下。
基本语法：var promise = getAsyncPromise('fileA.txt'); //创建promise对象
	  promise.then(function(trsult){
		// 成功时的处理函数
	}）.catch(function(error){
		// 失败时的处理函数
	}）
// 返回一个promise对象
Promise.all ([promise1,promise2..])
返回一个新的Promise对象，当该promise对象内的参数对象都成功的状态下才会触发成功，有一个失败则立即触发失败。

Promise.race ([promise1,promise2..])
当参数里的任意一个promise成功或失败后，该函数就会返回，并使用这个promise对象的值进行resolve或reject

### 指令：

+ v-cloak: 解决网速缓慢时的加载问题；
+ v-text
+ v-html:可以解析html标签；
+ v-bind:可以绑定属性事件或者方法，可缩写为：；
+ v-on:它可以缩写为@；

### 事件:

+ blur: 当元素失去焦点时触发的事件。

### 组件:

+ 父子组件

  + 注意事项：1.注意大小写；2.组件模块内部有且只能有一个顶级标签。3.data必须是函数，必须返回对象。4.局部注册的组件在其子组件不可用。

+ 如何确定两个组件是不是父子组件？

  + 在任何一个组件定义时是不是注册过另一个组件？

+ 父组件给子组件传值

  ```js
  const Banner = {
      props: ['content'],   
  }
  
   // 父组件给子组件传值，在调用子组件的位置，添加了自定义属性content，属性的值为你需要传递的值。如果需要传递的值是变量，则需要结合绑定属性完成（组件的属性越少越好）。
  
  // 在定义子组件的地方，添加一个选项props，值为数组，数组中添加一个元素（为调用子组件时自定义的属性）content。这样就可以在定义组件模板处直接通过content就可以拿到数据啦。
  
  // 注意：上面这种传值的方式是最简单的，假设如果需要验证父组件传递过来的数据类型，怎么办？
  
  const Banner = {
      props: {
          content:String,
      }
          
  }
   // props是一个对象，自定义属性为key,value为数据类型。但是假设用户忘记传递参数，或者需要忘记参数呢？
  
  const Banner = {
      props: {
          content: {  // 自定义的属性
              type: string, // 数据类型
              default: 'aa' // 默认值
          }
      }       
  }
   // value是一个对象，对象内部包含数据类型。
  
  假如传递的数据类型是一个数组或者一个对象，则应该这样子使用：
  const Banner = {
      props: {
          content: {  // 自定义的属性
              type: Array, // 数据类型为数组或者对象
              default: function() {
                  return [1.2.3]
              } // 默认值必须为函数，返回数组或者对象
          }
      }       
  }
  ```

+ 子组件给父组件传值(通过事件传值i)

  > ```js
  > // 在父组件调用子组件的地方绑定了一个自定义事件@my-event = "getData“(注意不要加括号)"。在父组件定义的地方，实现定义函数getData。然后在子组件定义的地方，可以通过声明周期钩子函数或者组件内部自定义的函数去触发，通过this.$emit('父组件自定义绑定的事件'，’传递给父组件的值‘)。或者被动的触发点击事件，在method中写入对应的点检事件需要使用的方法。
  > methods: {
  >  getData (data) {
  >      // data即为子组件传递过来的数据
  >  }
  > }
  > 
  > mounted() {
  >     this.$emit('my-event',`赚了两万块钱`)
  > }
  > 
  > ```
  >


- 非父子组件之间的传值/兄弟组件之间传值（通过第三方传值（服务器））

  ```js
  // 学名：利用中央时间总线传值
  // A组件传值bus.$emit('事件名称1’，‘传递数据’）
  // B组件接受bus.$on('事件名称1’，‘传递数据’）
  const bus = new Vue()  // vue的第三方就是bus,$on：监听
  
  
  <div class='banner'>
      <button @click='callmenu'>呼叫menu</button>
  </div>
  const banner = {
      methods: {
          callmenu() {
              bus.$emit('call-menu-event','你好menu')
          }
      }
  }
  
  const menu = {
      mounter () {
          bus.$on('call-menu-event',function(data) {
              console.log(data)
          })
      }
  }
  ```

- 子组件直接调用父组件的属性和方法

  ```js
  // 可以直接通过this.$parent.msg(msg代表属性或者方法)取父组件上的数据和方法。
  // this.$parent.props
  ```

- 父组件可以直接调用子组件的属性和方法

  ```js
  添加一个标识：ref = "test"，即在父组件调用子组件的地方，添加一个ref属性，属性值任何定义。
  // 可以通过this.$refs.test获取子组件，使用this.$refs.test.prop获取子组件的数据，可以通过this.$refs.test.fn()调用子组件的方法。
  ```

  

### element:

#### 	修改element-ui/view组件的样式：

- 在需要更改的组件里新增一个style标签**【重点：不加scoped】**，然后直接获取class设置样式。（注意：为避免污染全局样式，最好不把它放在公共的css里面 ，给父级组件样式添加类名）
- **使用  /deep/，**深度作用选择器