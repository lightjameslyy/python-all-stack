class Test(object):
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("装饰器添加的功能")
        return "<h1>" + self.func() + "</h1>"
        

@Test  # get_str = Test(get_str)
def get_str():
    return "haha"

print(get_str())
