-- 账户的操作主要包括创建账户、删除账户、修改密码、授权权限等

-- 授予权限
    -- 1. 查看所有用户
    use mysql;
    select host,user,authentication_string from user;

    -- 2. 创建账户、授权
        -- 需要使用实例级账户登录后操作，以root为例
        -- 常用权限主要包括：create、alter、drop、insert、update、delete、select
        -- 如果分配所有权限，可以使用all privileges

        -- 创建账户&授权
        grant 权限列表 on 数据库 to '用户名'@'访问主机' identified by '密码';

        -- 示例1
            -- 创建一个laowang的账号，密码为123456，只能通过本地访问, 并且只能对jing_dong数据库中的所有表进行读操作
            grant select on jing_dong.* to 'laowang'@'localhost' identified by '123456';
            -- 查看用户有哪些权限
            show grants for laowang@localhost;
            -- 用laowang账户登陆mysql
            mysql -ulaowang -p123456 -A
            -- 尝试改数据
            use jing_dong;
            update goods set name="小霸王学习机" where id=25;  -- 失败
        
        -- 示例2
            -- 创建一个laoli的账号，密码为123456，可以任意电脑进行链接访问, 并且对jing_dong数据库中的所有表拥有所有权限
            grant all privileges on jing_dong.* to 'laoli'@'%' identified by '123456';
            -- 用laoli账户登录
            mysql -ulaoli -p123456 -A
            -- 尝试向goods_cates表插入数据
            insert into goods_cates (name) values ("卡车");  -- 成功

-- 账户操作
    -- 1. 修改权限
    grant 权限名称 on 数据库 to 账户@主机 with grant option;

        -- 示例1
            -- 给laowang添加insert权限
            grant select, insert on jing_dong.* to 'laowang'@'localhost' with grant option;
            flush privileges;
            -- 用laowang的账号登录，向jing_dong.goods_cates表插入数据
            insert into goods_cates (name) values ("自行车");  -- 成功


    -- 2. 修改密码
        -- 使用password()函数进行密码加密
    update user set authentication_string=password('新密码') where user='用户名';
    flush privileges;

    -- 3. 远程登登录
    
        -- 配置:
            -- sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
        -- 将下面这行注释掉
            -- bind-address = 127.0.0.1
        -- 重启mysql服务
            -- service mysql restart

    -- 4. 删除账户
        -- 方法1（prefered）
        drop user '用户名'@'主机';

        -- 方法2
        delete from user where user='用户名';
        flush privileges;

