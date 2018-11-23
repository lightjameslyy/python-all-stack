from pymysql import connect


class JD(object):
    def __init__(self):
        # 创建Connection连接
        self.conn = connect(host='localhost', port=3306, user='root',
                            password='liutao123', database='jing_dong', charset='utf8')
        # 获得Cursor对象
        self.cursor = self.conn.cursor()

    def __del__(self):
        # 关闭Cursor对象
        self.cursor.close()
        # 创建Connection连接
        self.conn.close()

    def sql_print_all(self, sql):
        """执行sql并逐行打印查询结果"""
        print()
        print("查询结果：")
        self.cursor.execute(sql)
        for line in self.cursor.fetchall():
            print(line)
        print()

    def add_brands(self):
        name = input("输入新的商品品牌名称：")
        sql = """insert into goods_brands (name) values("%s")""" % name
        self.cursor.execute(sql)
        self.conn.commit()

    def get_info_by_name(self):
        """根据名字查询商品，防止SQl注入"""
        find_name = input("输入要查询的商品的名字：")
        # SQL注入：find_name = ' or 1=1 or '1
        # sql = """select * from goods where name='%s';""" % find_name
        # print("----->%s<-----" % sql)
        # self.sql_print_all(sql)
        sql = "select * from goods where name=%s;"
        self.cursor.execute(sql, [find_name])
        print(self.cursor.fetchall())

    @staticmethod
    def print_menu():
        """打印菜单，获取功能序号"""
        print("--------京东--------")
        print("1: 所有商品")
        print("2: 所有商品分类")
        print("3: 所有商品品牌")
        print("4: 添加商品品牌")
        print("5: 根据名字查询商品")
        print("0: 退出")
        return input("请输入功能序号：")

    def run(self):
        while True:
            num = self.print_menu()

            if num == "1":
                # 查询所有商品
                self.sql_print_all("select * from goods;")
            elif num == "2":
                # 查询商品分类
                self.sql_print_all("select * from goods_cates;")
            elif num == "3":
                # 查询商品品牌
                self.sql_print_all("select * from goods_brands;")
            elif num == "4":
                # 添加商品品牌
                self.add_brands()
            elif num == "5":
                # 根据名字查询商品
                self.get_info_by_name()
            elif num == "0":
                break
            else:
                print()
                print("输入有误，请重新输入！")
                print()


def main():
    # 1. 创建京东商城对象
    jd = JD()

    # 2. 运行jd
    jd.run()


if __name__ == '__main__':
    main()
