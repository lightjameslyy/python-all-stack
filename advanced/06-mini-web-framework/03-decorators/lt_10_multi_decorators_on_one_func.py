def add_privilege(func):
    print("---开始进行装饰权限1---")
    def call_func(*args, **kwargs):
        print("---权限验证1---")
        return func(*args, **kwargs)  # unpack
    return call_func

def add_xx(func):
    print("---开始进行装饰xx---")
    def call_func(*args, **kwargs):
        print("---xx的功能---")
        return func(*args, **kwargs)  # unpack
    return call_func

@add_privilege  # test1 = add_privilege(test1)
@add_xx  # test1 = add_xx(test1)
def test1():
    print("---test1---")


test1()
