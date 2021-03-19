
---
title: redis url 格式
date: 2019-12-06 05:39:42.965281
Description: ""
Tags: []
Categories: []
DisableComments: false
---
Connections to a Redis Standalone, Sentinel, or Cluster require a
specification of the connection details. The unified form is `RedisURI`. You
can provide the database, password and timeouts within the `RedisURI`. You
have following possibilities to create a `RedisURI`:

  1. Use an URI:
    
        RedisURI.create("redis://localhost/");

  2. Use the Builder
    
        RedisURI.Builder.redis("localhost", 6379).auth("password").database(1).build();

  3. Set directly the values in `RedisURI`
    
        new RedisURI("localhost", 6379, 60, TimeUnit.SECONDS);

### URI syntax

 **Redis Standalone**

 _redis_   **://**  [ **:**   _password_ @]  _host_  [ **:**   _port_ ] [
**/**   _database_ ][ **?**  [ _timeout=timeout_ [ _d|h|m|s|ms|us|ns_ ]] [&
_database=database_ ]]

 **Redis Standalone (SSL)**

 _rediss_   **://**  [ **:**   _password_ @]  _host_  [ **:**   _port_ ] [
**/**   _database_ ][ **?**  [ _timeout=timeout_ [ _d|h|m|s|ms|us|ns_ ]] [&
_database=database_ ]]

 **Redis Standalone (Unix Domain Sockets)**

 _redis-socket_   **://**   _path_  [ **?** [ _timeout=timeout_ [
_d|h|m|s|ms|us|ns_ ]][& _database=database_ ]]

 **Redis Sentinel**

 _redis-sentinel_   **://**  [ **:**   _password_ @]  _host1_ [ **:**
_port1_ ] [,  _host2_ [ **:**   _port2_ ]] [,  _hostN_ [ **:**   _portN_ ]] [
**/**   _database_ ][ **?** [ _timeout=timeout_ [ _d|h|m|s|ms|us|ns_ ]] [&
_sentinelMasterId=sentinelMasterId_ ] [& _database=database_ ]]

 **Schemes**

  * `redis` Redis Standalone
  * `rediss` Redis Standalone SSL
  * `redis-socket` Redis Standalone Unix Domain Socket
  * `redis-sentinel` Redis Sentinel

 **Timeout units**

  * `d` Days
  * `h` Hours
  * `m` Minutes
  * `s` Seconds
  * `ms` Milliseconds
  * `us` Microseconds
  * `ns` Nanoseconds

Hint: The database parameter within the query part has higher precedence than
the database in the path.

RedisURI supports Redis Standalone, Redis Sentinel and Redis Cluster with
plain, SSL, TLS and unix domain socket connections.


