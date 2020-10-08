
---
title: redis和memcached的区别（总结）
date: 2019-07-17 02:43:16.477122
Description: ""
Tags: []
Categories: []
DisableComments: false
---
转载:<https://www.cnblogs.com/457248499-qq-com/p/7392653.html>

  

观点一：

1、Redis和Memcache都是将数据存放在内存中，都是内存数据库。不过memcache还可用于缓存其他东西，例如图片、视频等等；

2、Redis不仅仅支持简单的k/v类型的数据，同时还提供list，set，hash等数据结构的存储；

3、[虚拟内存](https://www.baidu.com/s?wd=%E8%99%9A%E6%8B%9F%E5%86%85%E5%AD%98&tn=44039180_cpr&fenlei=mv6quAkxTZn0IZRqIHcvrjTdrH00T1Y4rjDYnju-
njb1nycLmW-b0ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6KdThsqpZwYTjCEQLGCpyw9Uz4Bmy-
bIi4WUvYETgN-
TLwGUv3EnHbzPHfYP10LPjDznWnkn1T3Ps)\--Redis当物理内存用完时，可以将一些很久没用到的value 交换到磁盘；

4、过期策略--memcache在set时就指定，例如set key1 0 0 8,即永不过期。Redis可以通过例如expire 设定，例如expire
name 10；

5、分布式--设定memcache集群，利用magent做一主多从;redis可以做一主多从。都可以一主一从；

6、存储数据安全--memcache挂掉后，数据没了；redis可以定期保存到磁盘（持久化）；

7、[灾难恢复](https://www.baidu.com/s?wd=%E7%81%BE%E9%9A%BE%E6%81%A2%E5%A4%8D&tn=44039180_cpr&fenlei=mv6quAkxTZn0IZRqIHcvrjTdrH00T1Y4rjDYnju-
njb1nycLmW-b0ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6KdThsqpZwYTjCEQLGCpyw9Uz4Bmy-
bIi4WUvYETgN-TLwGUv3EnHbzPHfYP10LPjDznWnkn1T3Ps)\--memcache挂掉后，数据不可恢复;
redis数据丢失后可以通过aof恢复；

8、Redis支持数据的备份，即master-slave模式的数据备份；





观点二：

# [Redis与Memcached的区别](http://www.cnblogs.com/wangkai1990/p/5212404.html)

  

 如果简单地比较Redis与Memcached的区别，大多数都会得到以下观点：  
1 Redis不仅仅支持简单的k/v类型的数据，同时还提供list，set，hash等数据结构的存储。  
2 Redis支持数据的备份，即master-slave模式的数据备份。  
3 Redis支持数据的持久化，可以将内存中的数据保持在磁盘中，重启的时候可以再次加载进行使用。  
  
在Redis中，并不是所有的数据都一直存储在内存中的。这是和Memcached相比一个最大的区别（我个人是这么认为的）。  
  
Redis 只会缓存所有的key的信息，如果Redis发现内存的使用量超过了某一个阀值，将触发swap的操作，Redis根据“swappability =
age*log(size_in_memory)”计算出哪些key对应的value需要swap到磁盘。然后再将这些key对应的value持久化到磁
盘中，同时在内存中清除。这种特性使得Redis可以保持超过其机器本身内存大小的数据。当然，机器本身的内存必须要能够保持所有的key，毕竟这些数据
是不会进行swap操作的。  
  
同时由于Redis将内存中的数据swap到磁盘中的时候，提供服务的主线程和进行swap操作的子线程会共享这部分内存，所以如果更新需要swap的数据，Redis将阻塞这个操作，直到子线程完成swap操作后才可以进行修改。  
  
可以参考使用Redis特有内存模型前后的情况对比：

VM off: 300k keys, 4096 bytes values: 1.3G used  
VM on: 300k keys, 4096 bytes values: 73M used  
VM off: 1 million keys, 256 bytes values: 430.12M used  
VM on: 1 million keys, 256 bytes values: 160.09M used  
VM on: 1 million keys, values as large as you want, still: 160.09M used

  
当 从Redis中读取数据的时候，如果读取的key对应的value不在内存中，那么Redis就需要从swap文件中加载相应数据，然后再返回给请求方。
这里就存在一个I/O线程池的问题。在默认的情况下，Redis会出现阻塞，即完成所有的swap文件加载后才会相应。这种策略在客户端的数量较小，进行
批量操作的时候比较合适。但是如果将Redis应用在一个大型的网站应用程序中，这显然是无法满足大并发的情况的。所以Redis运行我们设置I/O线程
池的大小，对需要从swap文件中加载相应数据的读取请求进行并发操作，减少阻塞的时间。  
  
redis、memcache、mongoDB 对比  
从以下几个维度，对redis、memcache、mongoDB 做了对比，欢迎拍砖  
  
1、性能  
都比较高，性能对我们来说应该都不是瓶颈  
总体来讲，TPS方面redis和memcache差不多，要大于mongodb  
  
  
2、操作的便利性  
memcache数据结构单一  
redis丰富一些，数据操作方面，redis更好一些，较少的网络IO次数  
mongodb支持丰富的数据表达，索引，最类似关系型数据库，支持的查询语言非常丰富  
  
  
3、内存空间的大小和数据量的大小  
redis在2.0版本后增加了自己的VM特性，突破物理内存的限制；可以对key value设置过期时间（类似memcache）  
memcache可以修改最大可用内存,采用LRU算法  
mongoDB适合大数据量的存储，依赖操作系统VM做内存管理，吃内存也比较厉害，服务不要和别的服务在一起  
  
4、可用性（单点问题）  
  
对于单点问题，  
redis，依赖客户端来实现分布式读写；主从复制时，每次从节点重新连接主节点都要依赖整个快照,无增量复制，因性能和效率问题，  
所以单点问题比较复杂；不支持自动sharding,需要依赖程序设定一致hash 机制。  
一种替代方案是，不用redis本身的复制机制，采用自己做主动复制（多份存储），或者改成增量复制的方式（需要自己实现），一致性问题和性能的权衡  
  
Memcache本身没有数据冗余机制，也没必要；对于故障预防，采用依赖成熟的hash或者环状的算法，解决单点故障引起的抖动问题。  
  
mongoDB支持master-slave,replicaset（内部采用paxos选举算法，自动故障恢复）,auto
sharding机制，对客户端屏蔽了故障转移和切分机制。  
  
  
5、可靠性（持久化）  
  
对于数据持久化和数据恢复，  
  
redis支持（快照、AOF）：依赖快照进行持久化，aof增强了可靠性的同时，对性能有所影响  
  
memcache不支持，通常用在做缓存,提升性能；  
  
MongoDB从1.8版本开始采用binlog方式支持持久化的可靠性  
  
  
6、数据一致性（事务支持）  
  
Memcache 在并发场景下，用cas保证一致性  
  
redis事务支持比较弱，只能保证事务中的每个操作连续执行  
  
mongoDB不支持事务  
  
  
7、数据分析  
  
mongoDB内置了数据分析的功能(mapreduce),其他不支持  
  
  
8、应用场景  
redis：数据量较小的更性能操作和运算上  
  
memcache：用于在动态系统中减少数据库负载，提升性能;做缓存，提高性能（适合读多写少，对于数据量比较大，可以采用sharding）  
  
MongoDB:主要解决海量数据的访问效率问题  


