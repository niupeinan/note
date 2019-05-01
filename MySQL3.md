# DQL:

## 查询语句

> MySQL 数据库使用SQL SELECT语句来查询数据,SELECT是数据库中最常用的语句，并且在SELECT语句后面通常会跟随众多的字句，来完成复杂的查询

- 语法

  ```mysql
  SELECT
    column_1, column_2, ...
    FROM
        table_1
    [INNER | LEFT |RIGHT] JOIN table_2 ON conditions
    WHERE
        conditions
    GROUP BY column_1
    HAVING group_conditions
    ORDER BY column_1
    LIMIT offset, length;
  ```

- SELECT语句由以下列表中所述的几个子句组成：

  - SELECT之后是逗号分隔列或星号(*)的列表，表示要返回所有列。
  - FROM指定要查询数据的表或视图。
  - JOIN根据某些连接条件从其他表中获取数据。
  - WHERE过滤结果集中的行。
  - GROUP BY将一组行组合成小分组，并对每个小分组应用聚合函数。
  - HAVING过滤器基于GROUP BY子句定义的小分组。
  - ORDER BY指定用于排序的列的列表。
  - LIMIT限制返回行的数量。 **语句中的SELECT和FROM语句是必须的，其他部分是可选的**

- 查询字段约束

  - 通配符

    ```mysql
    select * from table_name
    ```

  - 指定要查询的字段

    ```mysql
    select column1,column2,.... from table_name
    ```

  - 别名

    > 当我们要查询的表名太长，或者是有查询的字段有冲突的时候，就需要用到别名

    ```mysql
    select column as a from table_name
    ```

## 查询语句各种字句

> select语句通常会配合各种子句来完成复杂的查询

### WHERE

> 如果使用SELECT语句但不使用WHERE子句在表中查询数据，则会获取表中的所有行记录，这些行记录中大部分是不想要的行记录,WHERE子句允许根据指定的过滤表达式或条件来指定要选择的行

```
  SELECT
    column1, column1, ...
FROM
    table_name
WHERE
    condition1 AND condition2;
```

- WHERE子句中的比较运算符

 

| 操作符   | 描述                                    |
| -------- | --------------------------------------- |
| =        | 等于，几乎任何数据类型都可以使用它。    |
| <> 或 != | 不等于                                  |
| <        | 小于，通常使用数字和日期/时间数据类型。 |
| >        | 大于，                                  |
| <=       | 小于或等于                              |
| >=       | 大于或等于                              |

- WHERE子句中的逻辑运算符

| 操作符 | 描述 |
| ------ | ---- |
| or     | 或者 |
| and    | 并且 |
| not    | 非   |

- BETWEEN运算符
  - BETWEEN运算符允许指定要测试的值范围

    ```mysql
    expr [NOT] BETWEEN begin_expr AND end_expr;
    ```

  - 获取指定的时间范围

    ```mysql
    BETWEEN CAST('2013-01-01' AS DATE)
      AND CAST('2013-01-31' AS DATE);
    ```

- like 运算符

  > LIKE操作符通常用于基于模式查询选择数据。以正确的方式使用LIKE运算符对于增加/减少查询性能至关重要。

  - MySQL提供两个通配符，用于与LIKE运算符一起使用，它们分别是：百分比符号 - %和下划线 -

    - 百分比(%)通配符允许匹配任何字符串的零个或多个字符。
    - 下划线(_)通配符允许匹配任何单个字符。

  - 具有NOT运算符的LIKE

    > MySQL允许将NOT运算符与LIKE运算符组合，以找到不匹配特定模式的字符串

  - LIKE与ESCAPE子句

    > 您可以使用ESCAPE子句指定转义字符，以便MySQL将通配符解释为文字字符。如果未明确指定转义字符，则反斜杠字符\是默认转义字符
    >
    > ```
    > LIKE '%$_20%' ESCAPE '$';
    > ```

- IN操作符介绍

  > IN运算符允许您确定指定的值是否与列表中的值或子查询中的任何值匹配

  ```mysql
    SELECT
        column1,column2,...
    FROM
        table_name
    WHERE
     (expr|column_1) [NOT] IN ('value1','value2',...);
  ```

  - IN的子查询 

    ```mysql
    SELECT
       column,....
    FROM
       table_name
    WHERE
    column IN (SELECT ....)
    ```

- find_in_set()函数

  > 提供了一个名为FIND_IN_SET()的内置字符串函数，允许您在逗号分隔的字符串列表中查找指定字符串的位置
  >
  > ```
  >   FIND_IN_SET(needle,haystack);
  >   SQLFIND_IN_SET()函数接受两个参数：
  >   第一个参数needle是要查找的字符串。
  >   第二个参数haystack是要搜索的逗号分隔的字符串列表。
  > ```

## GROUP BY

> GROUP BY子句通过列或表达式的值将一组行分组为一个小分组的汇总行记录。 GROUP BY子句为每个分组返回一行。换句话说，它减少了结果集中的行数,GROUP BY子句与聚合函数一起使用

```
​```
SELECT
    c1, c2,..., cn, aggregate_function(ci)
FROM
    table
WHERE
    where_conditions
GROUP BY c1 , c2,...,cn;
​```
```

**ROUP BY子句必须出现在FROM和WHERE子句之后。 在GROUP BY关键字之后是一个以逗号分隔的列或表达式的列表，这些是要用作为条件来对行进行分组** 

- GROUP BY中HAVING子句

  > having是分组（group by）后的筛选条件，分组后的数据 组内再筛选where则是在分组前筛选where子句中不能使用聚集函数，而having子句中可以，所以在集合函数中加上了HAVING来起到测试查询结果是否符合条件的作用。即having子句的适用场景是可以使用聚合函数

- avg()函数 - 计算一组值或表达式的平均值。

- count()函数 - 计算表中的行数。

- instr()函数 - 返回子字符串在字符串中第一次出现的位置。

- sum()函数 - 计算一组值或表达式的总和。

- min()函数 - 在一组值中找到最小值。

- max()函数 - 在一组值中找到最大值

### ORDER BY

> 当使用SELECT语句查询表中的数据时，结果集会按照表数据默认位置进行排序。要对结果集进行排序，请使用ORDER BY子句。 ORDER BY子句允许：对单个列或多个列排序结果集。按升序或降序对不同列的结果集进行排序

```
​```
SELECT column1, column2,...
FROM tbl
ORDER BY column1 [ASC|DESC], column2 [ASC|DESC],...
​```
```

- ASC表示升序，DESC表示降序，默认升序

- 可以指定多列排序，后面的列是在前一列的基础上进行的

  #### MySQL ORDER BY按表达式排序示例

  ```
     SELECT column1, column2,column1*column2 as exp...
     FROM tbl
     ORDER BY column1 [ASC|DESC], column2 [ASC|DESC],exp ...
  ```

  #### ORDER BY与自定义排序顺序

  ```
     SELECT column1 ...
     FROM tbl
     ORDER BY FIELD (column1,val1,val2... ) ...
  ```

### LIMIT子句简介

> 在SELECT语句中使用LIMIT子句来约束结果集中的行数。LIMIT子句接受一个或两个参数。两个参数的值必须为零或正整数

```
​```
SELECT
    column1,column2,...
FROM
    table
LIMIT offset , count;
​```
```

- offset参数指定要返回的第一行的偏移量。第一行的偏移量为0，而不是1

  ![img](file:///C:/Users/npn/Desktop/_book/part4/imgs/1.jpg) 

- count指定要返回的最大行数

### LIMIT获取前N行

```
SELECT
   column1,column2,...
FROM
   table
LIMIT n
```

- ### LIMIT获得最高和最低的值

- LIMIT子句经常与ORDER BY子句一起使用。首先，使用ORDER BY子句根据特定条件对结果集进行排序，然后使用LIMIT子句来查找最小或最大值