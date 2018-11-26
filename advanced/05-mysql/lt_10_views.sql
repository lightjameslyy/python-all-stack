-- 视图是对若干张基本表的引用，一张虚拟的表，查询语句执行的结果，不存储具体的数据（基本表数据发生了改变，视图也会跟着改变）；

-- 查询三张表的信息
select * from goods as g left join goods_cates as c on c.id=g.cate_id left join goods_brands as b on b.id=g.brand_id;

-- 只显示需要的字段，并将字段名改为合适的名称
select g.*, c.name as cate_name, b.name as brand_name from goods as g left join goods_cates as c on c.id=g.cate_id left join goods_brands as b on b.id=g.brand_id;

-- 创建视图
create view v_goods_info as select g.*, c.name as cate_name, b.name as brand_name from goods as g left join goods_cates as c on c.id=g.cate_id left join goods_brands as b on b.id=g.brand_id;

-- 查看视图
show talbes;

-- 使用视图
select * from v_goods_info;

-- 删除视图
drop v_goods_info;

-- 视图的作用（一般只用与查询）
    -- 1. 提高了重用性，就像一个函数
    -- 2. 对数据库重构，却不影响程序的运行
    -- 3. 提高了安全性能，可以对不同的用户，只提供公开的字段
    -- 4. 让数据更加清晰


