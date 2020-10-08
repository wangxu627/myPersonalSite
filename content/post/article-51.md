
---
title: Python PEP249
date: 2019-10-26 00:35:24.882086
Description: ""
Tags: []
Categories: []
DisableComments: false
---
在项目开发中，数据库应用必不可少。[PEP 249](https://www.python.org/dev/peps/pep-0249/)
即定义了使用Python访问数据库的一组通用规范，统一了不同数据库系统的访问模型。该规
范使得数据库访问模块更易于理解，在提供广泛的数据库连接支持的同时，也增强了应用在 不同数据库之间的可移植性。

在Python Database API 2.0规范中，定义了API接口的各个部分，如模块接口，连接对象， 游标对象，类型对象和构造器，DB
API的可选扩展以及可选的错误处理机制等。

## 标准模块接口

根据PEP 249规范，做了一个简单的示意图，根据不同类型做了简单的划分，并不一定与 Python对象一一对应。

![pep249](http://dylanninin.com/assets/images/2012/pep249.jpg)

## 1.模块接口

Module Interface Python代码与数据库交互的模块接口，必须提供获取数据库连接的构造方法。

通过调用connect(parameters.. )即可返回数据库连接对象Connection Object，

  * connect(parameters… )：获取数据库连接。其中parameters为数据源、用户、密码、数 据库等，根据不同数据库可选不同参数。

## 2.数据库连接对象

Connection Object 数据库连接对象主要提供获取数据库游标对象、并提交/回滚事务的方法，以及关闭数据库 连接。

  * close()：关闭数据库连接
  * commit()：提交事务
  * rollback()：回滚事务
  * cursor()：获取游标对象，操作数据库，如执行DML操作，调用存储过程等

## 3.全局常量

Gobals Constants 定义一些DB API相关的全局常量，在标准接口中，主要如下：

  * apilevel：当前DB API版本，如”1.0”，或”2.0”
  * threadsafety：整型常量，定义支持的线程安全类型，主要是是否可以在线程之间共享模块、连接对象以及游标对象。

    * 0 不可共享该模块
    * 1 可共享该模块，但不能共享连接对象
    * 2 可共享该模块和连接对象
    * 3 可共享该模块、连接对象和游标独享
  * paramstyle：接口参数占位符所支持的样式。因易读性和灵活性，推荐使用numeric，named，pyformat
  * qmark 问号符样式，如 …WHERE name=?
  * numeric 数字序号样式，如 …WHERE name=:1
  * named 命名参数样式，如 …WHERE name=:name
  * format ANSI C语言printf格式化编码样式如 e.g. …WHERE name=%s
  * pyformat Python扩展编码样式如 …WHERE name=%(name)s

## 4.异常体系

Exceptions 异常体系主要用于定义DB API相关的异常，包括警告，错误，数据相关的异常，接口相关的 异常等等。

  * Warning ：数据在执行插入操作时被截断，等等
  * Error ：这里提到的除 Warning 外的所有异常的基类
  * InterfaceError ： 数据库接口而非数据库本身故障
  * DatabaseError ： 严格意义上的数据库问题
  * DataError ： 包含如下结果数据的问题除数为 0，值超出范围等
  * OperationalError ： 与编程人员无关的数据库错误：连接丢失、内存分配错误、事务处理错误等
  * IntegrityError ： 数据库的关系完整性受到了影响，例如，外键约束失败
  * InternalError ： 数据库遇到内部错误，例如，游标无效、事务不同步
  * ProgrammingError ： 未找到表、SQL 语句中的语法错误、指定参数的数量错误等
  * NotSupportedError ： 调用的 API 部件并不存在

## 5.游标对象

Cursor Object 游标对象代表数据库中的游标，用于指示抓取数据操作的上下文。主要提供执行SQL语句、 调用存储过程、获取查询结果等方法。

  * description：数据库列类型和值的描述信息
  * rowcount：回返结果的行数统计信息，如SELECT,UPDATE,CALLPROC等
  * callproc(procname,[, parameters])：调用存储过程，需要数据库支持
  * close()：关闭当前游标
  * execute(operation[, parameters])：执行数据库操作，SQL语句或者数据库命令
  * executemany(operation, seq_of_params)：用于批量操作，如批量更新
  * fetchone()：获取查询结果集中的下一条记录
  * fetchmany(size)：获取指定数量的记录
  * fetchall()：获取结构集的所有记录
  * arraysize：指定使用fetchmany()获取的行数，默认为1
  * setinputsizes(sizes)：设置在调用`execute*()`方法时分配的内存区域大小
  * setoutputsize(sizes)：设置列缓冲区大小，对大数据列入LONGS，BLOBS尤其有用

## 6.数据类型和构造器

Type and Constructor

1）Type Type定义了Python的数据类型和数据库中表列类型的转换和对应关系。

  * STRING： 对应数据库中基于字符串的数据类型，如char，varchar
  * BINARY： 对应数据库中的二进制类型，如long, row, blob
  * NUMBER： 对应数据库中的数字类型，如number
  * DATETIME： 对应数据库中的时间类型，如date, time
  * ROWID：对应数据库中的row id
  * None：对应数据库中的NULL

2）Constructor

Constructor是一组用于构造特殊数据类型的构造器，可以通过指定参数构造并返回预期对 象。

  * Date(year, month, day)：构造日期对象
  * Time(hour, minute, second)：构造时间对象
  * Timestamp(year, month, day, hour, minute, second)：构造时间戳对象
  * DateFromTicks(ticks)：通过从计算机计时开始经过的秒数构造日期对象；即从1970年1月1日0时0分0秒起计算
  * TimeFromTicks(ticks)：同上，用于构造时间对象
  * TimestampFromTicks(ticks)：同上，用于构造时间戳对象
  * Binary(string)：从字符串构造二进制对象 扩展模块接口

扩展模块可以参考官方文档，这里暂不提及。

## 参考

  * [PEP 249](https://www.python.org/dev/peps/pep-0249/)
  * [PEP 248](https://www.python.org/dev/peps/pep-0248)
  * [DatabaseInterfaces](https://wiki.python.org/moin/DatabaseInterfaces)


