def set_level(level_num):
    def set_func(func):
        def call_func(*args, **kwargs):
            if level_num == 1:
                print("===check point 1===")
            elif level_num == 2:
                print("===check point 2===")
            return func(*args, **kwargs)
        return call_func
    return set_func

@set_level(1)
def test1():
    print("===test1===")
    return "ok"

@set_level(2)
def test2():
    print("===test2===")
    return "ok"

test1()
test2()
