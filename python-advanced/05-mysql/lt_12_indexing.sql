-- 问题：当数据库中数据量很大时，查找数据会变得很慢
-- 索引是一种特殊的文件(InnoDB数据表上的索引是表空间的一个组成部分)，它们包含着对数据表里所有记录的引用指针。
-- 建索引会占用空间，索引太多的会影响性能，因为更新数据的时候需要更新索引。

-- 索引的使用
    -- 查看索引
    show index from 表名;

    -- 创建索引
        -- 如果指定字段是字符串，需要指定长度，建议长度与定义字段时的长度一致
        -- 字段类型如果不是字符串，可以不填写长度部分
        -- 创建主键或外键时会自动创建索引
    create index 索引名称 on 表名(字段名称(长度))

    -- 删除索引：
    drop index 索引名称 on 表名;



-- 索引demo
    -- 1. 创建测试表test_index
    create table test_index(title varchar(10));

    -- 2. 使用python程序通过pymsql模块 向表中加入十万条数据
    -- set lt_13_test_index.py

    -- 3. 开启运行时间监测：
    set profiling=1;

    -- 4. 查找第1万条数据ha-99999
    select * from test_index where title='ha-9999';

    -- 5. 查看执行的时间：
    show profiles;

    -- 6. 为表title_index的title列创建索引：
    create index title_index on test_index(title(10));

    -- 7. 执行查询语句：
    select * from test_index where title='ha-9999';

    -- 8. 再次查看执行的时间
    show profiles;