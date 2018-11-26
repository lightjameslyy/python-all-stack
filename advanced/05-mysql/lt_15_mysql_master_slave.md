#  MySQL主从同步

主从同步使得数据可以从一个数据库服务器复制到其他服务器上，在复制数据时，一个服务器充当主服务器（master），其余的服务器充当从服务器（slave）。

作用：
- 读写分离
- 数据备份
- 负载均衡

## 主从同步配置步骤

环境：

|  role  |       os       |      ip      | name    |
| :----: | :------------: | :----------: | ------- |
| master | ubuntu 16.04.5 | 192.168.56.4 | ubuntu1 |
| slave  | ubuntu 16.04.5 | 192.168.56.5 | ubuntu2 |
| slave  | windows 10     | 192.168.56.1 | windows |

### 1. 备份主服务器原有数据到从服务器

1. 在 ubuntu1 上执行命令：

   ```shell
   mysqldump -uroot -p --all-databases --lock-all-tables > ~/master_db.sql
   ```

2. 在 slave 上进行数据还原：

   ```shell
   mysql –uroot –p < master_db.sql
   ```

   如果不行就先 root 登录然后执行命令：

   ```sql
   source master_db.sql
   ```

### 2. 配置 master 服务器（ubuntu1）

1. 编辑设置 mysqld 的配置文件，设置 log_bin（二进制日志文件）和 server-id：

   ```shell
   sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
   ```
   将 `server-id` 和 `log_bin` 这两行的注释去掉。

2. 重启 mysql 服务：

   ```shell
   sudo service mysql restart
   ```

3. 登入主服务器 ubuntu 中的 mysql ，创建用于从服务器同步数据使用的帐号：

   ```shell
   mysql –uroot –p
   ```

   ```sql
   GRANT REPLICATION SLAVE ON *.* TO 'slave'@'%' identified by 'slave';
   FLUSH PRIVILEGES;
   ```

4. 获取主服务器的二进制日志信息：

   ```sql
   SHOW MASTER STATUS;
   ```

   File 为使用的日志文件名字，Position 为使用的文件位置，这两个参数须记下，配置从服务器时会用到。

### 3. 配置 slave 服务器（windows 10）

1. 编辑配置文件 `C:\app\mysql-5.7.24-winx64\my.ini` ，在 `[mysqld]` 中添加设置 `server-id=2` 。

2. 按键 `Win + R` ，输入 `service.msc`，重启 `MySQL` 服务。

3. `root` 登录到 mysql，设置连接到 master 服务器：

   ```sql
   change master to master_host='192.168.56.4', master_user='slave', master_password='slave',master_log_file='mysql-bin.000001', master_log_pos=590;
   ```

4. 开启同步，查看同步状态

   ```sql
   start slave;
   show slave status \G;
   ```
   看到下面两行表示同步已正常运行：
   ```
   Slave_IO_Running: Yes
   Slave_SQL_Running: Yes
   ```

5. 测试主从同步

   在 ubuntu1（主服务器）的 mysql 中创建一个数据库：
   ```
   create database dailyfresh default charset=utf8;
   ```

   在 windows（从服务器）的 mysql 中查看新建的数据库是否存在：
   ```
   show databases;
   ```