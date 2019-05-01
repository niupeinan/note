## 安装mysql服务：

- 命令行
- 软件
- 程序存入数据
- mysql.server 存入数据
- mysql.client 命令行操作数据库
- 在sql里面#和--空格都代表注释。
- sql注入：“ or 1=1； -- 
- bootstrap网站
- 火狐开发者中心     MDN Web 文档
- uri 统一资源标识符，是一个资源在互联网上的唯一标识  uniform Resource Locator(定位)
- 代替window.onload事件的是document.addEventLicenter("DOMContentLoaded",function(){})
- http content-type 浏览器能识别的所有类型  

## mysql8.0.13版本：

>当navicat不能连接到mysql8.0.13版本，报错2059时，可以使用下面的命令去执行。
>
>```mysql
>出现2059这个错误的原因是在mysql8之前的版本中加密规则为mysql_native_password，而在mysql8以后的加密规则为caching_sha2_password。
>输入命令：第一条： ALTER USER 'root'@'localhost' IDENTIFIED BY 'password' PASSWORD EXPIRE NEVER;
>
>                    第二条： ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
>
>                    注意此处的password为你的登陆密码，本人的操作为：
>
>                    第一条： ALTER USER 'root'@'localhost' IDENTIFIED BY '123****' PASSWORD EXPIRE NEVER;
>
>                    第二条： ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123****';
>```

## 安装mysql8.0.15版本时出现current root password解决：

```mysql
1.首先在mysql的安装目录中remove；
2.清除mysql数据存放目录：一般在C:\Documents and Settings\All 
Users.windows\Application Data目录下 。
3.清除注册表mysql的信息：
删除注册表数据，通过regedit，删除以下几个文件： 
HKEY_LOCAL_MACHINE/SYSTEM/ControlSet001/Services/Eventlog/Applications/MySQL 
HKEY_LOCAL_MACHINE/SYSTEM/ControlSet002/Services/Eventlog/Applications/MySQL 
HKEY_LOCAL_MACHINE/SYSTEM/CurrentControlSet/Services/Eventlog/Applications/MySQL 
```

## navicat12版本的下载和安装：

```mysql 
参考下列网址：
https://jingyan.baidu.com/article/495ba841b239e638b20ede4a.html
```

## mysql命令行：

- ### 如何连接数据库：

  ```mysql
  mysql -hlocalhost -uroot -p 回车 密码 进入mysql 
  ```

- ### 查看所有库：

  ```mysql
  show databases ； 展示  
  ```

- ### 创建库

  ```mysql
  create database  stu(库的名字)；
  ```

- ### 使用库

  ```mysql
  use 库的名字
  ```

- ### 查看全局变量：

  ```mysql
  show global variable like "变量"
  ```

- ### 导出建表语句：

  ```mysql
  show create table 表名；
  ```

- ### 创建表

  ```my
  create table stu(id int(10) auto_increment primary key,name varchar(255),age varchar(10),sex varchar(10))default charset=utf-8 
  ```

- ## desc stu  

  > 预览

- ### 输入数据：

  ```mysql
  insert into stu(name,sex,age) values("张三"，“男”，“20”),(),() on duplicate key update sid=sid+1；        # 以更新的形式，插入多条数据到stu表中
  insert into 新表名 select * from 已经存在的表  #快速拷贝已经存在的表中的内容，但是新表名需要自己去建立。
  create table 新表名 like 已经存在的表   #快速拷贝已经存在的表，但内容不会复制过去。新表名不需要自己去建立。
  replace into 表名（sname,cid）values("",3);  #如果说插入的信息已经设置了主键或者unique，则用replace插入的内容替换掉原来的内容，效率慢。
  ```

- ### 查看数据：

  ```mysql
  select  *  from  stu;
  select * from stu limit 1;
  select  *  from  stu order by id asc;  #按照升序排列
  select  *  from  stu order by id desc;   #按照降序实现
  select  *  from  stu order by rand() limit 1;  #随机取一条信息
  ```

- ### 修改数据：

  ```mysql
  update [low_PRIRITY] [IGNORE] stu set sex="女"  where id=1; 修改数据内容 #low_PRIRITY：只要有人查询，当前操作延迟。
  update stu set tname=（select tname from  stu order by id rand() limit 1）where tname is null;
  ```

- ### 关联更新：

  ```mysql
  update table1，table2... set table1.attr=val1,table2.attr=val1 where table1.id=2 and table2.attr=val;
  update table1 join table2 set table1.attr=val1,table2.attr=val1 where table1.id=2 and table2.attr=val; #val:原来的值  val1:改后的值
  ```

- ### 关联删除：

  ```mysql
  delete table1,table2 from table1,table2 where table1.attr=val and table2.attr=val;
  ```

- ### 删除数据：

  ```mysql
  delete from stu where id=2; 
  delete from stu; # 清空数据，自增的值不会回到最初的状态，速度比较慢；
  truncate stu; # 清空数据，效率比较快。
  ```

- ### 修改数据库名的方法：

  ```
  在Innodb数据库引擎下修改数据库名的方式与MyISAM引擎下修改数据库的方式完全不一样，如果是MyISAM可以直接去数据库目录中mv就可以，Innodb如果用同样的方法修改会提示相关表不存在。
  第一种方法：
  rename database olddbname to newdbname
  这个是5.1.7到5.1.23版本可以用，但是官方不推荐，会有丢失数据的危险
  第二种：
  1.创建需要改成新名的数据库
  2.mysqldum到处要改名的数据库
  3.删除原来的旧库
  
  这种方法是安全的，但是如果数据量大，会很耗时
  
  3.第三种：
  #!/bin/bash
  # 假设将sakila数据库名改为new_sakila
  # MyISAM直接更改数据库目录下的文件即可
  mysql -uroot -p123456 -e 'create database if not exists new_sakila'
  list_table=$(mysql -uroot -p123456 -Nse "select table_name from information_schema.TABLES where TABLE_SCHEMA='sakila'")
  for table in $list_table
  do
      mysql -uroot -p123456 -e "rename table sakila.$table to new_sakila.$table"
  done
  这里用到了rename table更改表名的命令，但是如果新表名后面加数据库，将会将原来的数据库的表移动到新的数据库，所有这种方法既安全又快速。
  
  # mysqldump常用于MySQL数据库逻辑备份。 
  ```

- ### 使可以在Linux和window系统中互换的代码：

  ```linux
  sudo apt-get autoremove open-vm-tools
  sudo apt-get install open-vm-tools-desktop
  ```

- ### drop命令删除数据库：

  ```mysql
  drop database <数据库名>；
  drop table <表名>;
  ```

- ### mysqladmin删除数据库：

  ```mysql
  可以使用 mysql mysqladmin 命令在终端来执行删除命令。
  以下实例删除数据库 RUNOOB
  [root@host]# mysqladmin -u root -p drop RUNOOB
  Enter password:******
  执行以上删除数据库命令后，会出现一个提示框，来确认是否真的删除数据库：
  
  Dropping the database is potentially a very bad thing to do.
  Any data stored in the database will be destroyed.
  
  Do you really want to drop the 'RUNOOB' database [y/N] y
  Database "RUNOOB" dropped
  ```

## mysql添加数据：

> 1.直接在form下面添加id组件
>
> 2.如右：<form action="/editcon?id={{item.id}}" method=="post">

# mysql主要内容：

- DCL：数据控制语言
- DDL：数据定义语言
- DML：数据操纵语言
- DQL：数据查询语言
- TCL：事务控制语言
- 数据库锁
- 主从配置

# DCL：

### 访问控制和权限：

> mysql实现了复杂的访问控制和权限系统，允许你创建用于处理客户端操作的全面的访问规则，并有效禁止未被授权的客户端访问数据库。

### 默认表：

- user表：包含用户账户和全局权限列
- db表：包含数据库级权限
- table_priv和columns_prive：包含表级和列级权限
- procs_priv:包含存储函数

### 创建用户账户：

- CREATE  USER user_account IDENTIFIED BY password(user_account:username@hostname) # 创建
- SHOW GRANTS FOR  用户名  #查看
- DROP USER user,[user]......    for example:DROP  user yueyingjun@localhost   #删除
- 通配符：%和[-]允许用户从任意地方连接

### 授予权限：

- 给用户授予权限，关键字GRANT

  - 命令：

    ```mysql
    GRANT privilege.[privilege],... ON privilege_leval   #privilege,[user] 权限 privilege leval 给该表
    To user[]  # 给那个用户
    
    WTTH GRAN OPIION  # 允许被修改
    ```

  - 设置指定权限：

    ```mysql
    CREATE USER rfc IDENTIFIED BY "mypasswd"  # 创建用户
    GRANT SELECT，UPDATE，DELETE ON alibaba.* TO rfc  #设置权限
    ```

  - 允许远程链接

    ```mysql 
    grants all privileges on *.* to 'root'@'%'  identified by 'mysql' with grant option;
    flush privileges  #刷新数据库
    ```


# DDL：

## 创建库：

```my
CREATE DATABASE[IF not exists] database_name
```

## 删除数据库：

```my
drop DATABASE[IF exists] database_name
```

## 创建表：

```mysql
create table [if not exists] table_name(
		column_list
		)engine=table_type，default charset=utf-8 ，comment="注释";

# null占空间，但是什么都没有   none:不占用空间，什么都没有
for example:
create table 数据库名.表名(
id int(11) auto_increment,  #假如一个数字占四个字节，在32位里面只显示11位
name varchar(10) unique,             #unique:唯一索引
sex enum("1“，”0“) not null,  # 枚举类型，不是空的则默认为1,default null 默认为null
primary key(id));      
```

## 修改表：

```mysql
alter table 表名 change [column] oldname newname varchar(100) not null;  #修改字段
alter table 表名 add [column] sex enum("男","女") not null after 列名; #添加字段
alter table 表名 drop jsp #删除字段
```

## 添加主键：

```mysql
alter table table_name add primary key(primary_key_column)
```

## 删除主键：

```mysql 
alter table 表名 drop primary key;
```

## 添加索引：

```mysql
alter table table_name add unique (column_list);    # 给某一列添加索引
alter table table_name add fulltext (column_list) ； # 添加全文索引
alter table table_name add index  index_name (column_list) ;  #添加普通索引
#table_name是要增加索引的表名，column_list指出对哪些列进行索引，
```

## 删除索引：

```mysql
alter table table_name drop index column_name;   #没有修改索引  
```

## 修改引擎：

```mysql
alter table my_table engine = InnoDB
show ENGINEs  # 查看mysql支持的所有引擎
show create table 表名  # 查看当前创建表的引擎
```

## 修改自增值：

```mysql
alter table table_name auto_increment = 1;
```

# DQL：

## 数据库查询语句：

- ```mysql
  select column_1,column_2, ...  from tbale_1 [inner | left | right] join 
  group by column_1 having group_condition order by column_1 limit offset,length
  
  for example:
  select count(tname) as num from 表名 #别名
  select count(tname)=num from 表名 #别名
  select distinct 地址 from 学生  #消除重复
  select top 3 * from 学生 --查询前3条记录 #top n（查询前N条）
  排序 select *from 学生 order by 年龄 asc  --按年龄进行升序排列  --desc降序   --asc升序
  
  ```

- distinct:查询时去掉重复的。

- where的操作符:

  > =  <>或 !=(代表不等于)   <  >  <=   >= !> !<

- where的逻辑运算符：

  > or and not；
  >
  > like “ 啊啊” 精准查询
  >
  > like “%aa ”  %表示所有的值
  >
  > like "_aa"    _代表内容前面只能有一个值。
  >
  > like “$aa“ escape "\$";  将\$变成转义字符。

- between and：

  ```mysql
  expr [not] between begin_erpr and end_expr;  #包含两边的值
  between cast('2013-01-01' as date) and cast('2014-01-01' as date) #获取指定的时间范围
  ```

- any,some

  > 小于其中的任何一个数据

- all

  > 小于其中的所有的数据

- in 

  ```mysql
  select * from 表名 where attr in ("val")
  ```

- find_in_set()函数：

  ```mysql
  select * from 表名 where find_in_set（"val",attr）
  ```

- group by

  ```mysql
  select 类别, sum(数量) as 数量之和
  from A
  group by 类别
  ```

- computer by:

  ```mysql
  select *
  from A
  where 数量>8
  order by 类别
  compute max(数量),min(数量),avg(数量) by 类别
  ```

- having

  ```mysql
  select sum(price*num) as tutal from goods where cid!=1 group by dt having tutal>100;
  ```

- order by

  ```mysql
  select column1,column2,...
  from tb1
  order by column1 [asc|desc],column2 [asc|desc],.. #多列排序，后面的列是在前面的列的基础上排序的。
  for example: select * from goods by field(gname,"童装","男装");
  ```

- 聚焦函数

  ```mysql
  avg()  计算平均值
  count()  行数
  instr() 第一次出现的位置
  sum()  总和
  min()  最小值
  max()  最大值
  ```

- limit

  ```mysql
  select
  	column1,colimn2...
  from 
  	table
  litmit offset,count(偏移量，长度)  先写order by再写limit，where总在最前面,group by紧跟。
  ```

- 关联查询：

  - 交叉连接

    ```mysql
    select cname,gname from 表名 cross join 表名；
    ```

  - 内连接

    ```mysql
    select cname,gname from 表名1 inner join 表名1.id=表名2.id；#交集
    ```

  - 左连接

    ```mysql
    select cname,gname from 表名1 left join 表名1.id=表名2.id；
    ```

  - 右连接

    ```mysql
    select cname,gname from 表名1 right join 表名1.id=表名2.id；
    ```

- 联合查询：

  ```mysql
  select cname from category union select gname from goods; #union all:去掉默认
  ```

- 子查询：

  - 标准子查询，返回单一值得标量

    ```mysql
    select * from article where uid = (select * from user where status=1 order by uid desc limit 1)
    ```

  - 列子查询，返回的结果是n行一列

    ```mysql
    select * from goods where cid in (select id from category where cname="食品" || cname="饮品")
    ```

    

  - 行子查询，返回的结果是一行n列

    ```mysql
    select * from orders where(oname,cid)=(select cname,cid from goods where gname="男装" and cid=1)
    ```

  - 表子查询,返回的结果是n行n列

    ```mysql
    select * from orders where(oname,cid) in (select cname,cid from goods where gname="男装" and cid=1)
    ```

  - explain:放在最前面，显示语句的效率高低。

# 数据类型

MySQL中定义数据字段的类型对数据库的优化是非常重要的。

MySQL支持多种类型，大致可以分为三类：数值、日期/时间和字符串(字符)类型。

------

## 数值类型

MySQL支持所有标准SQL数值数据类型。

这些类型包括严格数值数据类型(INTEGER、SMALLINT、DECIMAL和NUMERIC)，以及近似数值数据类型(FLOAT、REAL和DOUBLE PRECISION)。

关键字INT是INTEGER的同义词，关键字DEC是DECIMAL的同义词。

BIT数据类型保存位字段值，并且支持MyISAM、MEMORY、InnoDB和BDB表。

作为SQL标准的扩展，MySQL也支持整数类型TINYINT、MEDIUMINT和BIGINT。下面的表显示了需要的每个整数类型的存储和范围.

| 类型         | 大小                                     | 范围（有符号）                                               | 范围（无符号）                                               | 用途            |
| ------------ | ---------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------- |
| TINYINT      | 1 字节                                   | (-128，127)                                                  | (0，255)                                                     | 小整数值        |
| SMALLINT     | 2 字节                                   | (-32 768，32 767)                                            | (0，65 535)                                                  | 大整数值        |
| MEDIUMINT    | 3 字节                                   | (-8 388 608，8 388 607)                                      | (0，16 777 215)                                              | 大整数值        |
| INT或INTEGER | 4 字节                                   | (-2 147 483 648，2 147 483 647)                              | (0，4 294 967 295)                                           | 大整数值        |
| BIGINT       | 8 字节                                   | (-9 233 372 036 854 775 808，9 223 372 036 854 775 807)      | (0，18 446 744 073 709 551 615)                              | 极大整数值      |
| FLOAT        | 4 字节                                   | (-3.402 823 466 E+38，-1.175 494 351 E-38)，0，(1.175 494 351 E-38，3.402 823 466 351 E+38) | 0，(1.175 494 351 E-38，3.402 823 466 E+38)                  | 单精度 浮点数值 |
| DOUBLE       | 8 字节                                   | (-1.797 693 134 862 315 7 E+308，-2.225 073 858 507 201 4 E-308)，0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308) | 0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308) | 双精度 浮点数值 |
| DECIMAL      | 对DECIMAL(M,D) ，如果M>D，为M+2否则为D+2 | 依赖于M和D的值                                               | 依赖于M和D的值                                               | 小数值          |

------

## 日期和时间类型

表示时间值的日期和时间类型为DATETIME、DATE、TIMESTAMP、TIME和YEAR。

每个时间类型有一个有效值范围和一个"零"值，当指定不合法的MySQL不能表示的值时使用"零"值。

TIMESTAMP类型有专有的自动更新特性，将在后面描述。

| 类型      | 大小 (字节) | 范围                                                         | 格式                | 用途                     |
| --------- | ----------- | ------------------------------------------------------------ | ------------------- | ------------------------ |
| DATE      | 3           | 1000-01-01/9999-12-31                                        | YYYY-MM-DD          | 日期值                   |
| TIME      | 3           | '-838:59:59'/'838:59:59'                                     | HH:MM:SS            | 时间值或持续时间         |
| YEAR      | 1           | 1901/2155                                                    | YYYY                | 年份值                   |
| DATETIME  | 8           | 1000-01-01 00:00:00/9999-12-31 23:59:59                      | YYYY-MM-DD HH:MM:SS | 混合日期和时间值         |
| TIMESTAMP | 4           | 1970-01-01 00:00:00/2038结束时间是第 **2147483647** 秒，北京时间 **2038-1-19 11:14:07**，格林尼治时间 2038年1月19日 凌晨 03:14:07 | YYYYMMDD HHMMSS     | 混合日期和时间值，时间戳 |

------

## 字符串类型

字符串类型指CHAR、VARCHAR、BINARY、VARBINARY、BLOB、TEXT、ENUM和SET。该节描述了这些类型如何工作以及如何在查询中使用这些类型。

| 类型       | 大小                | 用途                            |
| ---------- | ------------------- | ------------------------------- |
| CHAR       | 0-255字节           | 定长字符串                      |
| VARCHAR    | 0-65535 字节        | 变长字符串                      |
| TINYBLOB   | 0-255字节           | 不超过 255 个字符的二进制字符串 |
| TINYTEXT   | 0-255字节           | 短文本字符串                    |
| BLOB       | 0-65 535字节        | 二进制形式的长文本数据          |
| TEXT       | 0-65 535字节        | 长文本数据                      |
| MEDIUMBLOB | 0-16 777 215字节    | 二进制形式的中等长度文本数据    |
| MEDIUMTEXT | 0-16 777 215字节    | 中等长度文本数据                |
| LONGBLOB   | 0-4 294 967 295字节 | 二进制形式的极大文本数据        |
| LONGTEXT   | 0-4 294 967 295字节 | 极大文本数据                    |

CHAR 和 VARCHAR 类型类似，但它们保存和检索的方式不同。它们的最大长度和是否尾部空格被保留等方面也不同。在存储或检索过程中不进行大小写转换。

BINARY 和 VARBINARY 类似于 CHAR 和 VARCHAR，不同的是它们包含二进制字符串而不要非二进制字符串。也就是说，它们包含字节字符串而不是字符字符串。这说明它们没有字符集，并且排序和比较基于列值字节的数值值。

BLOB 是一个二进制大对象，可以容纳可变数量的数据。有 4 种 BLOB 类型：TINYBLOB、BLOB、MEDIUMBLOB 和 LONGBLOB。它们区别在于可容纳存储范围不同。

有 4 种 TEXT 类型：TINYTEXT、TEXT、MEDIUMTEXT 和 LONGTEXT。对应的这 4 种 BLOB 类型，可存储的最大长度不同，可根据实际情况选择。

## 存储引擎的概述：

（1）为什么要合理选择数据库存储引擎：

MySQL中的数据用各种不同的技术存储在文件（或者内存）中。这些技术中的每一种技术都使用不同的存储机制、索引技巧、锁定水平并且最终提供广泛的不同的功能和能力。通过选择不同的技术，你能够获得额外的速度或者功能，从而改善你的应用的整体功能。

这些不同的技术以及配套的相关功能在MySQL中被称作存储引擎(也称作表类型)。MySQL默认配置了许多不同的存储引擎，可以预先设置或者在MySQL服务器中启用。你可以选择适用于服务器、数据库和表格的存储引擎，以便在选择如何存储你的信息、如何检索这些信息以及你需要你的数据结合什么性能和功能的时候为你提供最大的灵活性。

（2）定义：

数据库引擎是用于存储、处理和保护数据的核心服务。利用数据库引擎可控制访问权限并快速处理事务，从而满足企业内大多数需要处理大量数据的应用程序的要求。 使用数据库引擎创建用于联机事务处理或联机分析处理数据的关系数据库。这包括创建用于存储数据的表和用于查看、管理和保护数据安全的数据库对象（如索引、视图和存储过程）。

（3）存储引擎作用：

1）设计并创建数据库以保存系统所需的关系或XML文档。

2）实现系统以访问和更改数据库中存储的数据。包括实现网站或使用数据的应用程序，还包括生成使用SQL Server工具和实用工具以使用数据的过程。

3）为单位或客户部署实现的系统。

4）提供日常管理支持以优化数据库的性能。

（4）如何修改数据库引擎：

#### 方式一：

修改配置文件my.ini

将mysql.ini另存为my.ini，在[mysqld]后面添加default-storage-engine=InnoDB，重启服务，数据库默认的引擎修改为InnoDB

#### 方式二：

#### 在建表的时候指定

```
create table mytbl(   
    id int primary key,   
    name varchar(50)   
)type=MyISAM;
```

#### 方式三：

#### 建表后更改

```
alter table table_name type = InnoDB;
```

（5）怎么查看修改成功？

#### 方式一：

```
show table status from table_name; 
```

#### 方式二：

```
show create table table_name
```

#### 方式三：

使用数据库管理工具啊。

------

## MySQL各大存储引擎：

存储引擎主要有： 1. MyIsam , 2. InnoDB, 3. Memory, 4. Blackhole, 5. CSV, 6. Performance_Schema, 7. Archive, 8. Federated , 9 Mrg_Myisam

### （1）InnoDB：

**定义：**（默认的存储引擎）

InnoDB是一个事务型的存储引擎，有行级锁定和外键约束。

Innodb引擎提供了对数据库ACID事务的支持，并且实现了SQL标准的四种隔离级别，关于数据库事务与其隔离级别的内容请见数据库事务与其隔离级别这类型的文章。该引擎还提供了行级锁和外键约束，它的设计目标是处理大容量数据库系统，它本身其实就是基于MySQL后台的完整数据库系统，MySQL运行时Innodb会在内存中建立缓冲池，用于缓冲数据和索引。但是该引擎不支持FULLTEXT类型的索引，而且它没有保存表的行数，当SELECT COUNT(*) FROM TABLE时需要扫描全表。当需要使用数据库事务时，该引擎当然是首选。由于锁的粒度更小，写操作不会锁定全表，所以在并发较高时，使用Innodb引擎会提升效率。但是使用行级锁也不是绝对的，如果在执行一个SQL语句时MySQL不能确定要扫描的范围，InnoDB表同样会锁全表。

```
//这个就是select锁表的一种，不明确主键。增删改查都可能会导致锁全表，在以后我们会详细列出。
SELECT * FROM products WHERE name='Mouse' FOR UPDATE;
```

#### **适用场景：**

1）经常更新的表，适合处理多重并发的更新请求。

2）支持事务。

3）可以从灾难中恢复（通过bin-log日志等）。

4）外键约束。只有他支持外键。

5）支持自动增加列属性auto_increment。

### MySQL官方对InnoDB的讲解：

1）InnoDB给MySQL提供了具有提交、回滚和崩溃恢复能力的事务安全（ACID兼容）存储引擎。

2）InnoDB锁定在行级并且也在SELECT语句提供一个Oracle风格一致的非锁定读，这些特色增加了多用户部署和性能。没有在InnoDB中扩大锁定的需要，因为在InnoDB中行级锁定适合非常小的空间。

3）InnoDB也支持FOREIGN KEY强制。在SQL查询中，你可以自由地将InnoDB类型的表与其它MySQL的表的类型混合起来，甚至在同一个查询中也可以混合。

4）InnoDB是为处理巨大数据量时的最大性能设计，它的CPU效率可能是任何其它基于磁盘的关系数据库引擎所不能匹敌的。

5） InnoDB被用来在众多需要高性能的大型数据库站点上产生。

#### **补充：**什么叫事务？简称ACID

A 事务的原子性(Atomicity)：指一个事务要么全部执行,要么不执行.也就是说一个事务不可能只执行了一半就停止了.比如你从取款机取钱,这个事务可以分成两个步骤:1划卡,2出钱.不可能划了卡,而钱却没出来.这两步必须同时完成.要么就不完成.

C 事务的一致性(Consistency)：指事务的运行并不改变数据库中数据的一致性.例如,完整性约束了a+b=10,一个事务改变了a,那么b也应该随之改变.

I 独立性(Isolation）:事务的独立性也有称作隔离性,是指两个以上的事务不会出现交错执行的状态.因为这样可能会导致数据不一致.

D 持久性(Durability）:事务的持久性是指事务执行成功以后,该事务所对数据库所作的更改便是持久的保存在数据库之中，不会无缘无故的回滚.

### （2）MyIsam：

##### 定义：

MyIASM是MySQL默认的引擎，但是它没有提供对数据库事务的支持，也不支持行级锁和外键，因此当INSERT(插入)或UPDATE(更新)数据时即写操作需要锁定整个表，效率便会低一些。

MyIsam 存储引擎独立于操作系统，也就是可以在windows上使用，也可以比较简单的将数据转移到linux操作系统上去。

意味着：引擎在创建表的时候，会创建三个文件，一个是.frm文件用于存储表的定义，一个是.MYD文件用于存储表的数据，另一个是.MYI文件，存储的是索引。操作系统对大文件的操作是比较慢的，这样将表分为三个文件，那么.MYD这个文件单独来存放数据自然可以优化数据库的查询等操作。**有索引管理和字段管理**。MyISAM还使用一种表格锁定的机制，来优化多个并发的读写操作，其代价是你需要经常运行OPTIMIZE TABLE命令，来恢复被更新机制所浪费的空间。

#### **适用场景**：

1）不支持事务的设计，但是并不代表着有事务操作的项目不能用MyIsam存储引擎，可以在service层进行根据自己的业务需求进行相应的控制。

2）不支持外键的表设计。

3）查询速度很快，如果数据库insert和update的操作比较多的话比较适用。

4）整天 对表进行加锁的场景。

5）MyISAM极度强调快速读取操作。

6）MyIASM中存储了表的行数，于是SELECT COUNT(*) FROM TABLE时只需要直接读取已经保存好的值而不需要进行全表扫描。如果表的读操作远远多于写操作且不需要数据库事务的支持，那么MyIASM也是很好的选择。

#### **缺点：**

就是不能在表损坏后恢复数据。（是不能主动恢复）

### **补充**：ISAM索引方法–索引顺序存取方法

**定义：**

是一个定义明确且历经时间考验的数据表格管理方法，它在设计之时就考虑到 数据库被查询的次数要远大于更新的次数。

**特性：**

ISAM执行读取操作的速度很快，而且不占用大量的内存和存储资源。

在设计之初就预想数据组织成有固定长度的记录，按顺序存储的。—ISAM是一种静态索引结构。

#### **缺点：**

1.它不 支持事务处理

2.也不能够容错。如果你的硬盘崩溃了，那么数据文件就无法恢复了。如果你正在把ISAM用在关键任务应用程序里，那就必须经常备份你所有的实 时数据，通过其复制特性，MYSQL能够支持这样的备份应用程序。

# 索引类型：

### 一、简介

#### 索引是什么？

> 索引用于快速找出在某个列中有一特定值的行，不使用索引，MySQL必须从第一条记录开始读完整个表，直到找出相关的行，表越大，查询数据所花费的时间就越多，如果表中查询的列有一个索引，MySQL能够快速到达一个位置去搜索数据文件，而不必查看所有数据，那么将会节省很大一部分时间。 

#### 索引的优点和缺点：

> 优点：1.所有的MySql列类型(字段类型)都可以被索引，也就是可以给任意字段设置索引2.大大加快数据的查询速度。
>
> 缺点：1、创建索引和维护索引要耗费时间，并且随着数据量的增加所耗费的时间也会增加
>
> 　　　2、索引也需要占空间，我们知道数据表中的数据也会有最大上线设置的，如果我们有大量的索引，索引文件可能会比数据文件更快达到上线值
>
> 　　　3、当对表中的数据进行增加、删除、修改时，索引也需要动态的维护，降低了数据的维护速度。

#### MySQL目前主要有以下几种索引类型：

1.普通索引
2.唯一索引
3.主键索引
4.组合索引
5.全文索引

### 二、语句

```
CREATE TABLE table_name[col_name data type]
[unique|fulltext][index|key][index_name](col_name[length])[asc|desc]
```

1.unique|fulltext为可选参数，分别表示唯一索引、全文索引
2.index和key为同义词，两者作用相同，用来指定创建索引
3.col_name为需要创建索引的字段列，该列必须从数据表中该定义的多个列中选择
4.index_name指定索引的名称，为可选参数，如果不指定，默认col_name为索引值
5.length为可选参数，表示索引的长度，只有字符串类型的字段才能指定索引长度
6.asc或desc指定升序或降序的索引值存储

### 三、索引类型

1.普通索引
是最基本的索引，它没有任何限制。它有以下几种创建方式：
（1）直接创建索引

```
CREATE INDEX index_name ON table(column(length))
```

（2）修改表结构的方式添加索引

```
ALTER TABLE table_name ADD INDEX index_name ON (column(length))
```

（3）创建表的时候同时创建索引

```
CREATE TABLE `table` (
    `id` int(11) NOT NULL AUTO_INCREMENT ,
    `title` char(255) CHARACTER NOT NULL ,
    `content` text CHARACTER NULL ,
    `time` int(10) NULL DEFAULT NULL ,
    PRIMARY KEY (`id`),
    INDEX index_name (title(length))
)
```

（4）删除索引

```
DROP INDEX index_name ON table
```

2.唯一索引
与前面的普通索引类似，不同的就是：索引列的值必须唯一，但允许有空值。如果是组合索引，则列值的组合必须唯一。它有以下几种创建方式：
（1）创建唯一索引

```
CREATE UNIQUE INDEX indexName ON table(column(length))
```

（2）修改表结构

```
ALTER TABLE table_name ADD UNIQUE indexName ON (column(length))
```

（3）创建表的时候直接指定

3.主键索引
是一种特殊的唯一索引，一个表只能有一个主键，不允许有空值。一般是在建表的时候同时创建主键索引：

```
CREATE TABLE `table` (
    `id` int(11) NOT NULL AUTO_INCREMENT ,
    `title` char(255) NOT NULL ,
    PRIMARY KEY (`id`)
);
```

4.组合索引
指多个字段上创建的索引，只有在查询条件中使用了创建索引时的第一个字段，索引才会被使用。使用组合索引时遵循最左前缀集合

```
ALTER TABLE `table` ADD INDEX name_city_age (name,city,age); 
```

5.全文索引
主要用来查找文本中的关键字，而不是直接与索引中的值相比较。fulltext索引跟其它索引大不相同，它更像是一个搜索引擎，而不是简单的where语句的参数匹配。fulltext索引配合match against操作使用，而不是一般的where语句加like。它可以在create table，alter table ，create index使用，不过目前只有char、varchar，text 列上可以创建全文索引。值得一提的是，在数据量较大时候，现将数据放入一个没有全局索引的表中，然后再用CREATE index创建fulltext索引，要比先为一张表建立fulltext然后再将数据写入的速度快很多。
（1）创建表的适合添加全文索引

（2）修改表结构添加全文索引

```
ALTER TABLE article ADD FULLTEXT index_content(content)
```

（3）直接创建索引

```
CREATE FULLTEXT INDEX index_content ON article(content)
```

### 四、缺点

1.虽然索引大大提高了查询速度，同时却会降低更新表的速度，如对表进行insert、update和delete。因为更新表时，不仅要保存数据，还要保存一下索引文件。
2.建立索引会占用磁盘空间的索引文件。一般情况这个问题不太严重，但如果你在一个大表上创建了多种组合索引，索引文件的会增长很快。
索引只是提高效率的一个因素，如果有大数据量的表，就需要花时间研究建立最优秀的索引，或优化查询语句。

### 五、注意事项

> 使用索引时，有以下一些技巧和注意事项：
>
> 1.索引不会包含有null值的列
>
> 只要列中包含有null值都将不会被包含在索引中，复合索引中只要有一列含有null值，那么这一列对于此复合索引就是无效的。所以我们在数据库设计时不要让字段的默认值为null。
>
> 2.使用短索引
>
> 对串列进行索引，如果可能应该指定一个前缀长度。例如，如果有一个char(255)的列，如果在前10个或20个字符内，多数值是惟一的，那么就不要对整个列进行索引。短索引不仅可以提高查询速度而且可以节省磁盘空间和I/O操作。
>
> 3.索引列排序
>
> 查询只使用一个索引，因此如果where子句中已经使用了索引的话，那么order by中的列是不会使用索引的。因此数据库默认排序可以符合要求的情况下不要使用排序操作；尽量不要包含多个列的排序，如果需要最好给这些列创建复合索引。
>
> 4.like语句操作
>
> 
>
> 一般情况下不推荐使用like操作，如果非使用不可，如何使用也是一个问题。like “%aaa%” 不会使用索引而like “aaa%”可以使用索引。
>
> 5.不要在列上进行运算这将导致索引失效而进行全表扫描，例如

```
SELECT * FROM table_name WHERE YEAR(column_name)<2017;

```

> 6.不使用not in和<>操作

### 六. 外键：

> 一个副表的非主键字段和主表的主键字段进行关联的话，那么这个非主键字段我们叫做是外键。

- 如果在副表当中添加一个主键里面不存在的数据，插入操作会报错。

- 如果是在主表当中进行删除和修改的时候，当附表里面有对应的数据，name主表会阻止。

- myisam不支持外键。InnoDB支持外键。

- 创建外键：

  ```my
  [CONSTRAINT constraint_name]
  FOREIGN  KEY  [foreign_key_name] (columns)
  REFERENCES 主表名（字段）
  on delete action
  on update action
  action有四种格式：district默认  cascade关联  set null 将关联的数据设置为null  no action什么也不做
  for example:CONSTRAINT aaa foreign key (id) references classes(id))default charset=utf8;
  ```

- 删除外键：

  ```my
  alter table table_name drop foreign key 外键名
  ```

- 添加外键：

  ```,y
  alter table table_name  #约束名
  add foreign key (columns)  #外建名
  references 主表名（column）
  on delete action
  on update action
  ```

  

# 关系型数据库：

## python：

- python打包成模块分享到PyPi上面
- 升级pip:pip install -U(--upgrade) pip3
- 利用虚拟环境运行文件。
  -  python3 -m  venv myvenu 创建虚拟环境
  - source bin/activate  进入虚拟环境
  - deactivate  退出虚拟环境

### http协议内容：

- link  css z主动发起请求
- script  js 
- img 图片
- background：url
- audio video
- form   a链接 被动发送请求



### 传递方式：

```ajax
post      seo(搜索引擎优化)
get 
@app.route("/show/<id>")
def show(id):
	return str(id)

```

### 连接3306端口号：

```mysql
mysql -h58.64.217.120 -ushop -p123456  
```

### 连接其他端口号：

```mysql
mysql -h58.64.217.120 -P3308 -ushop -p123456
```

### pymysql:

```py
import pymysql
import time
import datetime
# 打开数据库连接
db = pymysql.connect("localhost","root","aaaaaa","getlist" )
cursor = db.cursor()
sql="INSERT INTO t_mall VALUES (0,%s,%s,%s)"

# 提交到数据库执行
db.commit()
# 关闭数据库连接
db.close()

URI标记了一个网络资源，仅此而已；  URL标记了一个WWW互联网资源（用地址标记），并给出了他的访问地址。
协议：//（用户名：密码@）主机：端口/路径/文件名？查询字符串#锚链接
锚链接：不会向服务器发起请求，在本地里面寻找内容，会形成历史记录。1、同一个web页面链接首先设计书签、<a name=”top”></a> 在不同位置定义，<a href=”#top”>返回到top位置</a>。

2、不同的页面之间转接，如果是在不同的页面之间链接时要在href属性中加上网页名称，First.html中定义了书签，<a name=”top”>Top的位置</a>。

3、现在要从Second.html中转入First.html并且将位置定到top所在的位置，可以设置，<a href=”first.html#top”>return first Top</a>。

location.href  获取地址栏
location.hash.slice  就是锚链接
```

## 查表的语句：

```mysql
rom 表一 inner join 表二 on 表一.id=表二.id (inner join表示两个表所在的交集,还有left join和right join他们分别代表着以左边的表和以右边的表为标准)
select 表一.id,cname,GROUP_CONCAT(step),GROUP_CONCAT(part)
GROUP BY cname

```

## sql语句的函数：

```mysql
date_format   group_concat()  where  group by limit
```

## 富文本编辑器(CKEditor)：

```eidtor
node.js下载的内容会放在根目录的node_modules，不在根目录中，则放在次目录中。
pip下载的内容胡放再site-packages中作为依赖来安装。
CDN：内容分发网络，CDN的关键技术主要有内容存储和分发技术。
ckedit 操作流程
1.npm init  创建一个包说明文件  package.json
2.把编辑器功能的组件放在package.json中
3.安装webpack以及一些webpack的依赖项
4.配置webpack的选项
5.写配置文件
6.写自己的入口文件
7.运行webpack命令
8.按照webpack指定的output路径和文件名，输入相应的编译好的文件
9.按照规范写HTML文件，并且引入js文件。
10.动态的添加或者删除相应的功能。删除：把相应的组件和依赖删掉；添加：在特性里面找到相应的组件，按照步骤进行安装和配置。
```

# 日志管理：

## 日志种类：

- 错误日志，记录启动.运行或者停止的问题，一般也会记录警告信息。

  ```mysql
  show global variables like "log_error"; #查询错误信息的地址
  show global variables like "log_warnings"; #启用警告信息
  ```

- 一般查询日志

  ```mysql
  show global variables like "general_log"; #启动开关
  show global variables like "general_log_file"; #日志文件变量
  全局日志开关
  ```

- 慢查询日志

  - 查询超时时间：long_query_time
  - 启动慢查日志：log_slow_queries={yes|no}
  - 启动慢查日志：slow_query_log
  - 日志记录文件：slow_query_log_file[=file_name]

- 二进制日志

  - 目录：

    ```mysql
    show variables like 'log_bin'
    show variables like 'datadir'
    show variables like '%log_bin%'
    ```

  - 查看当前服务器所有二进制：

    ```mysql
    show binary logs;
    show master logs;
    ```

  - 查看当前使用的二进制文件：

    ```mysql
    show master status;
    ```

  - 删除

    - 删除某个二进制文件：

      ```mysql
      purge binary logs to ***
      ```

    - 清除所有的二进制文件：

      ```mysql
      reset master
      ```

    - 自动清除：

      ```mysql
      show variables like 'expire_days'  #查看默认
      set expire_logs_days=7  #每七天清理一次
      ```

      

- 中继日志

- 事务日志

  > 事务性存储引擎用于保证（ACID）原子性，一致性，隔离性和持久性；其不会立即写到数据文件中，而是写到事务日志中。

## mysql全局变量查询与修改：

- 查询变量

  ```my
  show global variables [like "%log%"]
  ```

- 修改

  ```my
  set global variable_name=val
  ```

  

# 常用内置函数：

- ## 聚合函数

- ## count函数

  > 统计数据量

- ## AVG函数

  > 统计平均值，NULL会忽略

- ## SUM函数

  > 统计总值

- ## MAX函数

  > 统计最大值

- ## MIN函数

  > 统计最小值

- ## group_contact

  > 连接

- ## 字符串函数

  - ### concat()和concat_ws()函数

    > 将字符串连接

  - ### LEFT()函数

    > 截取，返回具有指定长度的字符串的左边部分。

  - ### replace()函数

    > 允许使用新的字符串替换原表中列的字符串。

  - ### SUBSTRING()函数

    > 从特定位置开始的字符串截取字符串,下标从一开始

  - ### TRIM()函数

    > both leading  trailing

  - ### FORMAT(N,D,locale)函数

    > 格式化数据，n是要格式化的数字，d是小数后面的部分

- ## 日期和事件函数

  - ## curdate()函数

    > 只输入日期

  - ## now()函数

    > 具体到时间

  - ## sysdate() 函数

    > 具体到时间

  - ### sleep()函数

- ## 返回指定日期的函数：

  - ### day()函数

  - ### month()函数

  - ### year()函数

  - ### week()函数

    > 返回一年中的第几周

  - ### weekday()函数

  - ### dayname()函数

  - ### set @@lc_time_names = "zh_CN";

    > 以中文的形式输出

- ## 日期计算函数：

  - ### datediff()函数

    > 计算两个时间的差

  - ### timediff()函数

    > 计算带有时间的差别，单位是时

  - ### timestampdiff(unit,begin,end)函数

  - ### date_add(start_date,interval,expr,unit)函数

    > interval:关键字    expr：数值  unit:单位   

  - ### date_sub()函数

# 视图：

> 视图是从一个或几个基本表（或者视图）导出的表。它与基本表不同，是一个虚表。 在mysql里面，经常会有一些复杂的查询，对于复杂的查询，每一次查询都会造成内部的消耗，尤其是在多次使用后，维护时间非常麻烦的事，利用视图可以有效解决这种问题。

## 创建视图：

```mysql
create view viewname as select....
```

## 修改视图：

```mysql
alter view viewname as select...
```

## create or replace view

## 删除视图

## 查看视图

## 视图的优点：

- 视图能够简化用户的操作
- 视图是用户能够从不同的角度看待同样的数据。
- 视图能够对及其数据进行安全保护。

# 临时表：

## 创建mysql临时表

```mysql
create temporary table tablename
```



## 删除mysql临时表

# 事务

> 事务是数据处理操作，其中执行就好像它是一个单一的一组有序的工作单元。换言之在在组内的每个单位的操作是成功的那么一个事务才是完整的，如果事务中的任何操作失败，整个事务将失败。

## 事务性质

- 原子性：确保了工作单位中的所有操作都成功完成，否则，事务被中止，在失败时会被回滚到事务操作以前的状态。
- 一致性：可确保数据库在正确的更改状态在一个成功提交事务。
- 隔离：使事务相互独立的存在
- 持久性：确保了提交事务的结果或系统故障情况下仍然存在作用

## 事务控制语句

- BEGIN或START TRANSACTION ；  显示的开启一个事务
- COMMIT；也可以使用COMMIT WORK，不过二者是等价的，COMMIT会提交事务，并使已对数据库进行的修改成为永久性的。
- ROLLBACK;事务中间有错误，将回退到原始的状态。
- SET AUTOCOMMIT=0  禁止自动提交
- SET AUTOCOMMIT=1  开启自动提交

## 事务支持的表类型：

- 有许多支持的，但最流行的一种是InnoDB

# 锁：

锁是计算机协调多个进程或线程并发访问某一资源的机制。在数据库中，除传统的计算资源（如CPU，ram,i/o等）的争用以外，数据也是一种供许多用户共享的资源。如何保证数据并发访问的一致性.有效性是所有数据库必须解决的一个问题。锁冲突也是影响数据库并发访问性能的一个重要因素。从这一个角度来说，锁对数据库来说显得尤为重要，也更加复杂。我们着重讨论mysql索结构的特点，常见的锁问题，以及解决mysql锁问题的一些方法和建议。mysql用到了很多这种锁机制，比如行锁，表锁，读锁，写锁等，都是在操作之前先上锁，这些所同城为悲观锁,数据库乐观锁:乐观锁并不是真实存在的锁，而是在更新的时候判断此时的库存是否是之前查询出的库存，如果相同，表示没人修改，可以更新库存，否则表示别人抢过资源，不再执行库存更新 

## mysql锁概述：

> 相对于其他数据库而言，mysql的锁机制比较简单，其最显著的特点是不同的存储引擎支持不同的锁机制。比如，myisam和memory存储引擎采用的是表级锁，BDB存储引擎采用的是页面锁，但也支持表级锁。InnerDB存储引擎即支持表级锁，又支持行级锁，但默认情况下是采用行级锁。

- 表级锁：开销大，加锁快，不会出现死锁(因为MyISAM会一次性获得SQL所需的全部锁) ,锁定粒度大，发生锁冲突的概率最高，并发度最低。
- 行级锁：开销小，加锁慢，会出现死锁，锁定粒度小，发生锁冲突的概率最低，并发度最高。
- 页面锁：开锁和加锁时间界与表锁和行锁之间，会出现死锁，锁定粒度界与表锁与行锁之间，并发度一般。
- 综合以上特点，表级锁使用与并发性不高，以查询为主，少量更新的应用，比如小型的web应用；而行级锁适用于高并发环境下，对事务完整性要求较高的系统，如在线事务处理系统。 

## 表级锁：

- 两种模式：表共享读锁（读锁）和表独占写锁（写锁或排它锁或写锁）

- 表级锁的存储引擎：myisam引擎   memory引擎

  ### 表级锁特点：

  - 作用范围在表的级别
  - 如果加了读锁，对mysql表的读操作，不会阻塞其他用户对同一表的读请求，但会阻塞对同一表的写请求
  - 如果加了读锁，可以查询锁定表中的记录，但更新或访问其他表都会提示错误
  - 如果加了写锁，对myisam表的写操作，则会阻塞其他用户对同一表的读和写操作。
  - 如果加了写锁，可以读写表中的内容，但更新偶访问其他表都会提示错误。

  ### 如何加表锁：

  > myisam在执行查询语句(select)前，会自动给涉及的所有表加读锁。在执行更新操作(update,delete,insert等)前，会自动给涉及的所有表加写锁。这个过程并不需要用户干预，因此，用户一般不需要直接用lock table命令给mysql表显示加锁。给mysql显示加锁，一般是为了在一定程度模拟事务操作，实现对某一时间点多个表进行读写操作。

  - 加锁

    ```mysql
    lock tables table_name read [local],lock tables table_name write [local]
    ```

  - 解锁

    ```mysql
    unlock tables;
    ```

  - 多表加锁

    ```mysql
    lock tables table_name [table_name] read [local],lock tables table_name [table_name] weite [local];
    ```

### 查询表级锁的争用情况：

```mysql
show status like 'table%';
或者
show status like '%lock%';
或者
show processlist;  #查看哪些sql语句正在被等待。
或者
show open tables  #当前被锁住的表以及锁住的次数
```

### 并发插入：

> MyISAM存储引擎有个系统变量 concurrent_insert，专门用来控制并发插入的行为，可以取 0 ， 1 ， 2。
>
> 一般如果对并发要求比较高的情况下，可以设置为2，总是可以插入，然后定期在数据库空闲时间对表进行optimize（优化）。

-  当concurrent_insert设置为0时，不允许并发插入。

- 当concurrent_insert设置为1时。如果myisam表中没有空洞（即标的中间没有被删除的行），允许在一个进程读表的同时，另一个进程从表尾插入记录，这也是mysql的默认设置。

- 当concurrent_insert设置为2时，无论myisam表中有没有空洞，都允许在表尾并发插入记录。

  ```mysql
  set global variables like "concurrent_insert"  #还能进行插入。
  ```

### 读写锁优先级：

```mysql
默认情况下，写操作的优先级要高于读操作的优先级，即便是先发送的读请求，后发送的写请求，此时也会优先处理写请求，然后再处理读请求。这就造成一个问题，一旦我发出若干个写请求，就会堵塞所有的读请求，直到写请求全部处理完，才有机会处理读请求，两种方式解决优先级的问题。
```

- 设置写锁的最多次数

  ```mysql
  max_write_lock_count=val;
  ```

- 降低写操作的优先级，给读操作更高的优先级

  ```mysql
  low_priority_updates=1 #默认关闭，等于一为打开。
  for example:insert low_priority into 表名(字段）values （‘000’）；
  在用update，insert，delete时，要加上[low_priority]关键字
  ```

### 设置写内存：

> 可以根据具体的业务设置读写内存。

```mysql
max_allowed_packet=1m #限制接受的数据包大小
net_buffer_length=2k#insert语句缓存值 2k~16m
bulk_insert_buffer_size=8m#一次性insert语句插入的大小
```

### 如何优化：

- 可以利用myisam存储引擎的并发插入特性，来解决应用中对同一表查询和插入的锁争用，例如current_insert系统变量设为2，总是允许并发插入。
- 同时，通过定期在系统空闲时段执行OPTIMIZE TABLE语句来整理空间碎片，收回因删除记录的中间空洞。
- 是否设置写的优先级，视场景而定，解决查询相对重要的应用（入用户登录系统）
- 是否设置写内存，视场景而定，解决批量插入数据场景中。

## 行级锁：

共享锁（X）

排他锁（S）

意向共享锁（IS）

意向排他锁（IX）：事务打算给数据行加行排他锁，事务在给一个数据行加排他锁IX锁。

| 请求锁模式   是否兼容   当前锁模式 |  X   |  IX  |  S   |  IS  |
| :--------------------------------: | :--: | :--: | :--: | :--: |
|                 X                  | 冲突 | 冲突 | 冲突 | 冲突 |
|                 IX                 | 冲突 | 兼容 | 冲突 | 兼容 |
|                 S                  | 冲突 | 冲突 | 兼容 | 兼容 |
|                 IS                 | 冲突 | 兼容 | 兼容 | 兼容 |

### 行级锁的存储引擎：

- InnoDB

## 间隙锁：

> InnoDB支持事务，为了满足隔离级别的要求，InnoDB有个间隙锁，当使用范围查找时，InnoDB会给满足key范围要求，但实际并不存在的记录加锁。例如：select * from user where id > 100 for updata 会给ID>100的记录加排他锁，满足这个范围，但不存在的记录，会加间隙锁，这样可以避免幻读，避免读取的时候插入满足条件的记录。 

## 隔离级别与锁：

> 一般来说，隔离级别越高，加锁就越严格。这样，产生锁冲突的概率就越大，一般实际应用中，通过优化应用逻辑，选用可提交读级别就够了。对于一些确实需要更高隔离级别的事务，再通过set session transaction isolation level+"级别" 来动态改变满足需求。 

## 死锁：

> MyISAM是没有死锁问题的，因为他会一次性获得所有的锁。InnoDB发生死锁后一般能自动检测到，并使一个事务释放锁并回退，另一个事务获得锁，继续完成事务。
>
> 在应用中，可以通过如下方式来尽可能的避免死锁：
>
> (1) 如果不同的程序会并发的存取多个表，应尽量约定以相同的顺序来访问表，这样可以大大降低产生死锁的机会。
>
> (2) 在程序以批量方式处理数据时，如果事先对数据排序，保证每个线程按固定的顺序来处理记录，也可以大大的降低出现死锁的可能。

### 行级锁的特点：

- InnoDB行级锁是通过给索引上的锁引项加锁来实现的，只有通过索引条件检索数据，InnoDB才使用行级锁，否则，InnoDB将使用表锁

- 即使是访问不同行的记录，如果使用的是相同的索引键，会发生锁冲突。

- 如果数据表建有多个索引时，可以通过不同的索引锁定不同的行。 

- 意向锁是InnoDB自动加的，不需用户干预。对于update，delete，insert语句，InnoDB会自动该涉及数据集加排他锁（X）,对于普通select语句，InnoDB不会添加任何锁。

- 在研究行级锁的时候，需要将自动提交关闭，默认为开启。

  ```mysql
  set autocommit = 0
  ```

- 注意：多个客户端都要设置set autocommit = 0

## 如何加行级锁：

> 加行级锁主要用在需要数据依存关系是来确认某行几率是否存在，并确定没有人对这个记录进行update操作。在InnoDB默认的隔离方式中， 当给某一条数据加（update，delete，insert）上排他锁时，其他人不能操作该数据，但是可以查询，查询到的是以前的值。只有当该条数据提交后，才可以进行操作。但是并不影响客户端去操作其他行数据。如果该字段加了索引，但在使用的时候将类型改变，索引失效，此时将变为行级锁。

```mysql
lock in share more  #加共享锁,在语句的末尾添加
for update #加排他锁，在语句的末尾添加
```

释放行级锁：

```mysql
commit;
rollback;
```

## 查询行级锁的争用情况

```mysql
show status like "innodb_row_lock%"
```

## 事务并发的问题：

- 脏读：事务A读取了事务B更新的数据，然后B回滚操作，那么A读取到的数据是脏数据，更新丢失，可以完全避免，应用对访问的数据加锁即可。 
- 不可重复读：事务A多次读取同一数据，事务B在事务A多次读取的过程中，对数据作了更新并提交，导致事务A多死读取同一数据时，结果不一致。
- 幻读：（读取结果集条数的对比）一个事务按相同的查询条件查询之前检索过的数据，却发现检索出来的结果集条数变多或者减少（由其他事务插入、删除的），类似产生幻觉 。

### 事务隔离级别：

- Read Uncommitted 读未提交：不允许第一类更新丢失。允许脏读，不隔离事务。

- Read Committed 读已提交（不可重复读）：不允许脏读，允许不可重复读。

- Repeatable Read 可重复读：不允许不可重复读。但可能出现幻读。

- Serializable 串行化：所有的增删改查串行执行。

  #### 读未提交

  事务读不阻塞其他事务读和写，事务写阻塞其他事务写但不阻塞读。
   可以通过写操作加“持续-X锁”实现。

  #### 读已提交

  事务读不会阻塞其他事务读和写，事务写会阻塞其他事务读和写。
   可以通过写操作加“持续-X”锁，读操作加“临时-S锁”实现。

  #### 可重复读

  > mvcc机制（multiversion  concurrency control）

  事务读会阻塞其他事务事务写但不阻塞读，事务写会阻塞其他事务读和写。
   可以通过写操作加“持续-X”锁，读操作加“持续-S锁”实现。

  #### 串行化

  “行级锁”做不到，需使用“表级锁”。

  | 事务隔离级别 | 回滚覆盖 | 脏读     | 不可重复读 | 幻读     | 提交覆盖 |
  | ------------ | -------- | -------- | ---------- | -------- | -------- |
  | 读未提交     | x        | 可能发生 | 可能发生   | 可能发生 | 可能发生 |
  | 读已提交     | x        | x        | 可能发生   | 可能发生 | 可能发生 |
  | 可重复读     | x        | x        | x          | 可能发生 | x        |
  | 串行化       | x        | x        | x          | xxxx     | x        |

  

### 查看隔离级别：

```mysql
select @@session.tx_isolation;
```

### 设置隔离级别：

```mysql
set session transaction isolation level read uncommitted(read committed)
```

## 如何优化行级锁？

- 尽量使用较低的隔离级别
- 选择合理的事务大小，小失误发生冲突的几率也更小
- 给记录集显示加锁时，最好一次性请求足够级别的锁。
- 尽量用相等条件访问数据，这样可以避免间隙锁对并发插入的影响。
- 对于一些特定的事务，可以用表锁提高处理速度以及减少死锁的概率 。

# 主从复制

> 在实际的生产环境中，由单台Mysql数据库是完全不能满足实际需求无论安全性，高可用性以及高并发等各个方面的要求。MySQL 主从(MySQL Replication)复制是满足这些要求的基础，它主要用于 MySQL 的实时备份、高可用、读写分离等场景。

## 1. 主从复制原理

- master服务器将数据的改变记录二进制日志，当master上的数据发生改变时，则将其改变写入二进制日志中。

- salve服务器会在一定时间间隔内对master二进制日志进行探测其是否发生改变，如果发生改变，则开始一个I/OThread请求master二进制事件

- 同时主节点为每个I/O线程启动一个dump线程，用于向其发送二进制事件，从节点保存至中继日志。

- 从节点将启动SQL线程从中继日志中读取二进制日志，在本地重放，使得其数据和主节点的保持一致。

- 最后I/OThread和SQLThread将进入睡眠状态，等待下一次被唤醒。

  ![img](file:///C:/Users/npn/Desktop/_book/part6/imgs/1.jpg) 

## 2.主从复制配置过程:

- 基本要求
  - 两台服务器(windows,linux,mac)
  - 双方mysql版本需一致，如不一致，只要主节点低于从节点
  - 两台服务器防火墙关闭
  - 双方数据库所用的用户，要具有远程访问的权限

- 主服务器配置

  - 修改主服务器的MySQL配置文件，window(my.ini),linux(my.cnf)

    ```mysql 
    #mysql唯一id
    server-id = 1
    #二进制日志文件，此项为必填项，否则不能同步数据；
    log-bin = "mysql-bin"
    #指定二进制错误文件
    log-error="mysql-error"
    #需要同步的数据库，如果需要同步多个数据库；
    binlog-do-db = uek_demo
    #binlog-do-db = slaveDB1
    #binlog-do-db = slaveDB2
    #不需要同步的数据库
    binlog-ignore-db = mysql
    ```

  - 授权给从数据库服务器 

    ```mysql
    GRANT REPLICATION SLAVE ON *.* to 'root'@'172.16.168.142' identified     by '123456';
    flush privileges;
    ```

  - mysql8.0版本授权 

    ```mysql
    CREATE USER 'root'@'172.16.168.142' IDENTIFIED WITH
    mysql_native_password BY '123456';
    GRANT REPLICATION SLAVE ON *.* TO 'root'@'172.16.168.142';
    ```

  - 重启主服务器

    ```mysql
    service mysqld restart
    ```

  - 查看主服务器BIN日志的信息（执行完之后记录下这两值，然后在配置完从服务器之前不要对主服务器进行任何操作，因为每次操作数据库时这两值会发生改变） 

    ```mysql
    show master status
    ```

- 从服务器配置要求：

  - 修改从服务器的MySQL配置文件，window(my.ini),linux(my.cnf)，配置server-id 的值，并确保这个ID没有被别的MySQL服务所使用 

    ```mysql
    server-id=2    #默认是1改成2
    log-bin="mysql-bin"    #这行本身有
    replicate-do-db=uek_demo    #需要同步的数据库
    replicate-ignore-db=mysql    #不同步系统数据库
    read_only     #设只读权限
    ```

  - 启动mysql服务

  - 执行同sql语句

    ```mysql
    change master to
    master_host='172.16.168.1',
    master_user='root',
    master_password='123456',
    master_log_file='mysql-bin.000002',
    master_log_pos=1041;
    ```

    - MASTER_HOST : 设置要连接的主服务器的ip地址
    - MASTER_USER : 设置要连接的主服务器的用户名
    - MASTER_PASSWORD : 设置要连接的主服务器的密码
    - MASTER_LOG_FILE : 设置要连接的主服务器的bin日志的日志名称
    - MASTER_LOG_POS : 设置要连接的主服务器的bin日志的记录位置。

  - 启动slave同步进程

    ```mysql
    start slave
    ```

- 主从同步检查 

  - 查看状态

    ```mysql
    show slave status\G
    ```

    **其中Slave_IO_Running 与 Slave_SQL_Running 的值都必须为YES，才表明状态正常** 

  - 如果之前从服务器启动过需要先停止，再运行 

    ```mysql
    stop slave;
    ```

    

