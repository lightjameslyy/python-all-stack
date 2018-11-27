# 下面的set_func是通用装饰器
def set_func(func):
    print("---开始进行装饰---")
    def call_func(*args, **kwargs):
        print("---权限验证1---")
        print("---权限验证2---")
        # func(args, kwargs)  # 错误，相当于传递了一个tuple和一个dict
        return func(*args, **kwargs)  # unpack
    return call_func

@set_func  # 等价于 test1 = set_func(test1)
def test1(num, *args, **kwargs):
    print("----test1---- %d" % num)
    print("----test1----", args)
    print("----test1----", kwargs)
    return "ok"

@set_func
def test2():
    pass


ret = test1(100)
print(ret)


ret = test2()
print(ret)



