# 数据库优化操作：

### MySQL优化

> 数据库优化维度有四个: 硬件、系统配置、数据库表结构、SQL及索引 优化成本: 硬件>系统配置>数据库表结构>SQL及索引 优化效果: 硬件<系统配置<数据库表结构<SQL及索引

### 运行机制原理和底层架构

> MySQL的查询优化，大家都了解一些最简单的技巧：不能使用SELECT *、不使用NULL字段、合理创建索引、为字段选择合适的数据类型….. 你是否真的理解这些优化技巧？是否理解其背后的工作原理？在实际场景下性能真有提升吗？我想未必。因而理解这些优化建议背后的原理就尤为重要

#### 1.MySQL逻辑架构

> 在头脑中构建一幅MySQL各组件之间如何协同工作的架构图，有助于深入理解MySQL服务器

- 最上层为客户端层，并非MySQL所独有，诸如：连接处理、授权认证、安全等功能均在这一层处理
- 中间这一层，包括查询解析、分析、优化、缓存、内置函数(比如：时间、数学、加密等函数)。所有的跨存储引擎的功能也在这一层实现：存储过程、触发器、视图等
- 第三层包括了存储引擎。通常叫做StorEngine Layer ，也就是底层数据存取操作实现部分，由多种存储引擎共同组成。它们负责存储和获取所有存储在MySQL中的数据。就像Linux众多的文件系统 一样。每个存储引擎都有自己的优点和缺陷

#### 2. MySQL逻辑模块组成

> 从上图看起来 MySQL 架构非常的简单，就是简单的两部分而已，但实际上每一层 中都含有各自的很多小模块，尤其是第二层 SQL Layer ，结构相当复杂的

1. Connectors

   > 指的是不同语言中与SQL的交互的接口,包括python,php,nodejs,java

2. Management Serveices & Utilities

   > 系统管理和控制工具,包括mysql的配置，权限，日志处理等

3. Connection Pool: 连接池

   > 管理缓冲用户连接，线程处理等需要缓存的需求,。每一个连接上 MySQL Server 的客户端请求都会被分配（或创建）一个连接线程为其单独服务。而连接线程的主要工作就是负责 MySQL Server 与客户端的通信

4. SQL Interface: SQL接口

   > 接受用户的SQL命令，并且返回用户需要查询的结果。比如select from就是调用SQL Interface

5. Parser: 解析器

   > SQL命令传递到解析器的时候会被解析器验证和解析,将SQL语句进行语义和语法的分析，分解成数据结构，然后按照不同的操作类型进行分类，然后做出针对性的转发到后续步骤,如果在分解构成中遇到错误，那么就说明这个sql语句是不合理的

6. Optimizer: 查询优化器

   > SQL语句在查询之前会使用查询优化器对查询进行优化。就是优化客户端请求的 query（sql语句） ，根据客户端请求的 query 语句，和数据库中的一些统计信息，在一系列算法的基础上进行分析，得出一个最优的策略，告诉后面的程序如何取得这个 query 语句的结果

7. Cache和Buffer： 查询缓存

   > 他的主要功能是将客户端提交 给MySQL 的 Select 类 query 请求的返回结果集 cache 到内存中，在解析查询之前，要查询缓存，这个缓存只能保存查询信息以及结果数据。如果请求一个查询在缓存 中存在，就不需要解析，优化和执行查询了。直接返回缓存中所存放的这个查询的结果

8. 存储引擎接口

   > 存储引擎接口模块可以说是 MySQL 数据库中最有特色的一点了。目前各种数据库产品中，基本上只有 MySQL 可以实现其底层数据存储引擎的插件式管理 

### 索引底层实现原理

> MySQL官方对索引的定义为：索引（Index）是帮助MySQL高效获取数据的数据结构。提取句子主干，就可以得到索引的本质：索引是数据结构

#### B树

> B树事实上是一种平衡的多叉查找树，也就是说最多可以开m个叉（m>=2），我们称之为m阶b树

- 每个节点至多可以拥有m棵子树。
- 根节点，只有至少有2个节点（要么极端情况，就是一棵树就一个根节点，单细胞生物，即是根，也是叶，也是树)。
- 非根非叶的节点至少有的Ceil(m/2)个子树(Ceil表示向上取整，图中5阶B树，每个节点至少有3个子树，也就是至少有3个叉)。
- 非叶节点中的信息包括[n,A0,K1,A1,K2,A2,…,Kn,An]，，其中n表示该节点中保存的关键字个数，K为关键字且Ki<Ki+1，A为指向子树根节点的指针。
- 从根到叶子的每一条路径都有相同的长度，也就是说，叶子节在相同的层，并且这些节点不带信息，实际上这些节点就表示找不到指定的值，也就是指向这些节点的指针为空

#### MyISAM索引的原理图

- MyISAM引擎使用B+Tree作为索引结构，叶节点的data域存放的是数据记录的地址 


#### InnoDB索引的原理图

- 在InnoDB中，表数据文件本身就是按B+Tree组织的一个索引结构，这棵树的叶节点data域保存了完整的数据记录 


**了解不同存储引擎的索引实现方式对于正确使用和优化索引都非常有帮助，例如知道了InnoDB的索引实现后，就很容易明白为什么不建议使用过长的字段作为主键，因为所有辅助索引都引用主索引，过长的主索引会令辅助索引变得过大。再例如，用非单调的字段作为主键在InnoDB中不是个好主意，因为InnoDB数据文件本身是一棵B+Tree，非单调的主键会造成在插入新记录时数据文件为了维持B+Tree的特性而频繁的分裂调整，十分低效，而使用自增字段作为主键则是一个很好的选择**

### explain参数详解

> 查询语句是我们在使用MySQL的频率最高的语句，也是影响性能最重要的环节，我们用explain这个命令来查看一个这些SQL语句的执行计划和查询效率，该命令从SQL执行的执行顺序，执行效率，索引使用情况等方面都给出了相应的标准，让我们有据可查。

- SQL语句编写流程

  ```mysql
  SELECT DISTINCT
    < select_list >
  FROM
    < left_table > < join_type >
  JOIN < right_table > ON < join_condition >
  WHERE
    < where_condition >
  GROUP BY
    < group_by_list >
  HAVING
    < having_condition >
  ORDER BY
    < order_by_condition >
  LIMIT < limit_number >
  ```

- SQL执行流程

  ```
  FROM <left_table>
  ON <join_condition>
  <join_type> JOIN <right_table>
  WHERE <where_condition>
  GROUP BY <group_by_list>
  HAVING <having_condition>
  SELECT
  DISTINCT <select_list>
  ORDER BY <order_by_condition>
  LIMIT <limit_number>
  ```

- 使用方式

  ```
  explain select * from uek_table;
  ```

- 执行效果

  ```
  +----+-------------+---------+------+---------------+------+---------+------+------+-------+
  | id | select_type | table     | type | possible_keys | key  | key_len | ref  | rows | Extra |
  +----+-------------+---------+------+---------------+------+---------+------+------+-------+
  |  1 | SIMPLE      | uek_table | ALL  | NULL          | NULL | NULL    | NULL |    1 | NULL  |
  +----+-------------+---------+------+---------------+------+---------+------+------+-------+
  row in set (0.03 sec)
  ```

#### 案例代码

```
​```
# 信息表
create table if not exists info(
id int(10) auto_increment primary key,
con varchar(100) not null)default charset=utf8;

# 老师表
create table if not exists teach(
id int(10) auto_increment primary key,
tname varchar(20) not null,
iid int(10),
CONSTRAINT infoid foreign key (iid) REFERENCES info(id)
)default charset=utf8;


# 课程表
create table if not exists course(
id int(10) auto_increment primary key,
cname varchar(20) not null,
tid int(10),
CONSTRAINT teachid foreign key (tid) REFERENCES teach(id)
)default charset=utf8;

​```
```

#### 1. id

> id是SQL执行的顺序的标识

- id相同时，执行顺序由上至下(由于表的数据量的大小决定执行顺序)
- 如果是子查询，id的序号会递增，id值越大优先级越高，越先被执行
- id如果相同，可以认为是一组，从上往下顺序执行；在所有组中，id值越大，优先级越高，越先执行

#### 2. select_type

> 查询中每个select子句的类型

1. SIMPLE(简单SELECT,不使用UNION或子查询等)

2. PRIMARY(查询中若包含任何复杂的子部分,最外层的select被标记为PRIMARY)

3. UNION(UNION中的第二个或后面的SELECT语句)

4. DEPENDENT UNION(UNION中的第二个或后面的SELECT语句，取决于外面的查询)

5. UNION RESULT(UNION的结果)

6. SUBQUERY(子查询中的第一个SELECT)

7. DEPENDENT SUBQUERY(子查询中的第一个SELECT，取决于外面的查询)

8. DERIVED(派生表的SELECT, FROM子句的子查询)

   ```
   select form.cname from (select * from course where tid in (1,2)) as form
   ```

#### 3. table

> 显示这一行的数据是关于哪张表的，看到的是derivedx的，说明这个结果是派生表的结果

#### 4. type

> 表示MySQL在表中找到所需行的方式，又称“访问类型”,代表性能的优劣 常用的类型有： ALL<index<range<ref<eq_ref<const<system<NULL

- ALL：Full Table Scan， MySQL将遍历全表以找到匹配的行,并且查找的内容不带索引

- index: Full Index Scan，index与ALL区别为index类型只遍历索引树,也就是查找有索引的列

- range:只检索给定范围的行，查找的内容不带索引，选择的行带索引，可以用between,>,<,但是不要用in，用in索引失效

- ref: 表示上述表的连接匹配条件，即哪些列或常量被用于查找索引列上的值，使用普通索引

- eq_ref: 类似ref，区别就在使用的索引是唯一引，对于每个索引键值，表中只有一条记录匹配，简单来说，就是多表连接中使用primary key或者 unique key作为关联条件

- const、system: 当MySQL对查询某部分进行优化，并转换为一个常量时，使用这些类型访问。如将主键置于where列表中，MySQL就能将该查询转换为一个常量。

- system: 在衍生查询中只有一条数据

  ```
  select form.cname from (select cname from course where id=1) as form
  ```

#### 5. possible_keys

> MySQL预测使用哪个索引在表中查找记录，如果是NULL说明MySQL找不到要使用的索引

#### 6. Key

> key列显示MySQL实际决定使用的键（索引），如果键是NULL，说明该语句性能堪忧，根据实际使用场景要添加索引，经常用来判断复合索引是否完整使用

#### 7. key_len

> 表示索引中使用的字节数，可通过该列计算查询中使用的索引的长度，不损失精确性的情况下，长度越短越好,尤其是使用InnoDB引擎

#### 8. ref

> 表示上述表的连接匹配条件，即哪些列或常量被用于查找索引列上的值，如果是 const的话说明效率较高

```
​```
select cname from course where id=1
​```
```

#### 9. rows

> 表示MySQL根据表统计信息及索引选用情况，估算的找到所需的记录所需要读取的行数

#### 10. Extra

> 该列包含MySQL解决查询的详细信息,有以下几种情况：

- Using index:指定索引的索引全部覆盖，代表性能不错

- Using where:代表语句性能一般，仅仅从where指定的索引不能找到全部信息，需要回表查询

- Using temporary：表示MySQL需要使用临时表来存储结果集，常见于排序和分组查询，说明在查询中需要用临时表存储，性能消耗较大，常见于在一个没有索引的表中进行运算

  ```
    explain select distinct name from abc;
  ```

- Using filesort：MySQL进行了多次排序，没有利用索引进行排序，说明性能很低

  ```
    创建一个复合索引的表
    create table demo(
    id int(10) auto_increment primary key,
    one varchar(100),
    two varchar(100),
    three varchar(100),
    index one (one),
    index two (two),
    index three (three)
    )
  
    创建sql语句
    select * from demo where one="" order by one
    select * from demo where one="" order by two
  ```

  **1. 对于单索引查找，排序不是同一个索引会出现重新排序。2.对于复合索引要遵循最佳左前缀，不要跨列**

- Using join buffer：改值强调了在获取连接条件时没有使用索引，并且需要连接缓冲区来存储中间结果。如果出现了这个值，那应该注意，说明你的sql语句写的太差了，需要mysql给你进行优化了，常见多表关联。

- Impossible where：这个值强调了where语句会导致没有符合条件的行。

  ```
    select * from demo where id=1 and id=2;
  ```

### mysql优化方法

#### 1. 优化工具

1. 通过使用 explain命令分析sql语句的运行效率(查阅 explain章节)
2. 通过开启慢查询来查看运行效率慢的sql语句 (查阅日志章节)

#### 2. 索引优化

> 索引是我们提升sql查询效率的重要手段，同时索引的使用不当也会带来性能的问题，在使用索引的时候，应该注意一下问题

1. 不能将索引用作表达式的一部分，也不能是函数的参数

   ```
     select * from demo where id+1=2
   
     select max(id) from demo where id=1;
   ```

2. 索引不要进行类型转化，否则索引失效

   ```
     select * from demo where name=2
     # 如果name是字符串类型，就存在类型转换
   ```

3. 复合索引应该遵循左前缀策略，不要交叉使用

   ```
     alter table table_name add index a_b_c (a,b,c)
   
     select c from table_name where id=a order by b
   ```

4. 复合索引如果用"or"关键字，索引失效

   ```
     select * from table_name where a="" or b=""
   ```

5. 复合索引不要使用 != <> 或 is null (is not null)

   ```
     select * from table_name where a!=""
   ```

6. 尽量不要和in在一起使用，导致索引失效

   ```
     select * from table_name where id in ("","")
   ```

7. 及时删除冗余的和长期不使用的索引

8. like 查询时候尽量不要出现左 "%",否则索引失效，如果非得使用，请用索引覆盖提高性能,要使用独立索引，不要使用复合索引

   ```
     select * from table_name where con like "%内容%"
   ```

#### 3. 单、多表SQL优化手段

1. 单表案例

   > 有一个表用来记录书籍的名字(bookname)，出版号(publicid)，作者(authorid)，类型(typeid)。 然后查询其中两种类型并且属于同一个作者，然后按照出版号来进行排序

   ```
     create table book(
     id int(10) auto_increment primary key,
     bookname varchar(100) not null,
     authorid varchar(20) not null,
     publicid int(10) default 11111,
     typeid int(10)) default charset=utf8;
     select * from book where typeid in(1,2) and authorid=1 order by publicid;
   ```

   - 加索引(并且加在频繁使用的字段上)
   - 调整索引顺序(遵循最佳左前缀)
   - 删除多于(干扰)索引
   - 调整查询条件，对索引有干扰的语句放到条件的最后

2. 多表案例

   > 有一个试题类型表(testtype)记录了试题的类型，字段包含 tid ,试题类型名称 (name) 有一个试题内容表(testcon)记录了试题的题目(title)，选项(opts)，答案(result)和类型(tid)

   ```
     # 类型表
     create table testtype(
     tid int(5) auto_increment primary key,
     name varchar(100))default charset=utf8;
     # 内容表
     create table testcon(
     id int(5) auto_increment primary key,
     title varchar(100) not null,
     opts varchar(200) not null,
     result varchar(100) not null,
     tid int(5),
     CONSTRAINT testid foreign key (tid) REFERENCES testtype(tid))default charset=utf8;
   ```

   - 多表索引添加原则，小表驱动大表(小表在左边 where 小表.x=大表.y)
   - left join 给左表加索引，right join 给右边加索引

#### 4. 表级别锁优化(查阅锁章节)

#### 5. 系统级别优化

1. 主从复制
2. 读写分离
3. 负载均衡

#### 6. 其他优化总结

1. 通常来说把可为NULL的列改为NOT NULL不会对性能提升有多少帮助，只是如果计划在列上创建索引，就应该将该列设置为NOT NULL
2. 对于数据类型，一定要根据业务需求选择尽可能小的存储数据类型
3. UNSIGNED表示不允许负值，大致可以使正数的上限提高一倍，如果表示的是正数，那么要用非符号
4. 通常来讲，没有太大的必要使用DECIMAL数据类型。即使是在需要存储财务数据时，仍然可以使用BIGINT。
5. TIMESTAMP使用4个字节存储空间，DATETIME使用8个字节存储空间
6. 大多数情况下没有使用枚举类型的必要
7. 表的列不要太多，如果列太多而实际使用的列又很少的话，有可能会导致CPU占用过高 **选择数据类型只要遵循小而简单的原则就好，越小的数据类型通常会更快，占用更少的磁盘、内存，处理时需要的CPU周期也更少**