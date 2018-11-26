def test1():
    print("*" * 50)


def test2():
    print("-" * 50)

    # 嵌套调用
    test1()

    print("-" * 50)

test2()
