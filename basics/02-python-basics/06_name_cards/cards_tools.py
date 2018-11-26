# all cards
card_list = []


def show_menu():
    """
    显示菜单
    :return:
    """
    print("*" * 50)
    print("欢迎使用【名片管理系统】 V 1.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)


def new_card():
    """
    新增名片
    :return:
    """
    print("-" * 50)
    print("新增名片")

    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入邮箱：")

    card_dict = {
        "name": name_str,
        "phone": phone_str,
        "qq": qq_str,
        "email": email_str,
    }

    card_list.append(card_dict)

    print(card_list)

    print("成功添加 %s 的名片" % name_str)


def show_all_cards():
    """
    显示全部名片
    :return:
    """
    print("-" * 50)
    print("显示全部名片...")

    if len(card_list) == 0:
        print("当前没有任何名片记录，请先添加名片")
        return

    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")
    print("")
    print("=" * 50)
    for card in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card["name"], card["phone"], card["qq"], card["email"]))


def search_card():
    """
    查询名片
    :return:
    """
    print("查询名片")

    find_name = input("请输入要查询的姓名：")

    for card in card_list:
        if card["name"] == find_name:
            print("找到了")
            for name in ["姓名", "电话", "QQ", "邮箱"]:
                print(name, end="\t\t")
            print("")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card["name"], card["phone"], card["qq"], card["email"]))
            break

    else:
        print("抱歉，没有找到 %s" % find_name)

