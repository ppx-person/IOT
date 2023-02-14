
### 数据审计
数据审计是一个跟踪表内容随时间变化的系统

### 日志
PGDATA/log 运行日志
PGDATA/pg_wal 重做日志
PGDATA/pg_xact 事务提交日志
服务器日志，可以再启动的时候指定，比如pg_ctl start -l ./alert.log
select name,setting from pg_settings where name like ‘log%’;


# PostgreSQL 15 新特性 – MERGE 语句
MERGE 语句主要用于根据来自源的信息和条件，
在单个事务中并使用单个语句从目标表中添加、更新或删除行。
最显着的用途是当基于某些连接条件发现差异时，
通过更新、删除或插入新行来同步两个表。

# TOAST，全称是The Oversized-Attribute Storage Technique, 
超大属性存储技术，顾名思义，就是说Pg中超长字段在数据库中的存储方式。
block 8kb,不允许一行数据跨页存储
当数据超过TOAST_TUPLE_THRESHOLD(默认2KB)时，Postgres将压缩数据，以适应2KB的缓冲区大小

怎么修改表字段的TOAST策略？
alter table test_blob alter column column_name set storage EXTENDED;














