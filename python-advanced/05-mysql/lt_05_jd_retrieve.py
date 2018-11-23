from pymysql import connect


class JD(object):
    def __init__(self):
        pass

    def show_all_items(self):
        """显示所有商品信息"""
        conn = connect(host='localhost', port=3306, user='root',
                       password='liutao123', database='jing_dong', charset='utf8')
        cs1 = conn.cursor()
        count = cs1.execute('select * from goods')
        print("查询到%d条数据:" % count)

        for i in range(count):
            result = cs1.fetchone()
            print(result)

        cs1.close()
        conn.close()

    def show_cates(self):
        """显示所有商品分类"""
        conn = connect(host='localhost', port=3306, user='root',
                       password='liutao123', database='jing_dong', charset='utf8')
        cs1 = conn.cursor()
        count = cs1.execute('select * from goods_cates')
        print("查询到%d条数据:" % count)

        for i in range(count):
            result = cs1.fetchone()
            print(result)

        cs1.close()
        conn.close()

    def show_brands(self):
        """显示所有商品品牌"""
        conn = connect(host='localhost', port=3306, user='root',
                       password='liutao123', database='jing_dong', charset='utf8')
        cs1 = conn.cursor()
        count = cs1.execute('select * from goods_brands')
        print("查询到%d条数据:" % count)

        for i in range(count):
            result = cs1.fetchone()
            print(result)

        cs1.close()
        conn.close()

    def run(self):
        while True:
            print()
            print("--------京东--------")
            print("1: 所有商品")
            print("2: 所有商品分类")
            print("3: 所有商品品牌")
            print("0: 退出")
            num = input("请输入功能序号：")
            print()

            if num == "1":
                # 查询所有商品
                self.show_all_items()
            elif num == "2":
                # 查询商品分类
                self.show_cates()
            elif num == "3":
                # 查询商品品牌
                self.show_brands()
            elif num == "0":
                break
            else:
                print("输入有误，请重新输入！")


def main():
    # 1. 创建京东商城对象
    jd = JD()

    # 2. 运行jd
    jd.run()


if __name__ == '__main__':
    main()
