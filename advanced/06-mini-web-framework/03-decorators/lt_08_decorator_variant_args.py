def set_func(func):
    print("---开始进行装饰---")
    def call_func(*args, **kwargs):
        print("---权限验证1---")
        print("---权限验证2---")
        # func(args, kwargs)  # 错误，相当于传递了一个tuple和一个dict
        func(*args, **kwargs)  # unpack
    return call_func

@set_func  # 等价于 test1 = set_func(test1)
def test1(num, *args, **kwargs):
    print("----test1---- %d" % num)
    print("----test1----", args)
    print("----test1----", kwargs)


test1(100)
test1(100, 200)
test1(100, 200, 300, mm=100)


