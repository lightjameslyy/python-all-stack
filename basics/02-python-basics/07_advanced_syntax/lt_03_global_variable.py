num = 10


def demo1():
    # new local variable: num, not the global num
    global num
    num = 99
    print("demo1 --> %d" % num)


def demo2():
    print("demo1 --> %d" % num)


demo1()
demo2()
