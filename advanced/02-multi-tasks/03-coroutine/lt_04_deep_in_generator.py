def create_num(size):
    a, b = 0, 1
    cur_index = 0
    while cur_index < size:
        # print(a)
        yield a  # 如果一个函数有yield语句，那么这个函数就是一个生成器模板
        a, b = b, a + b
        cur_index += 1


# 这里不是函数调用，而是创建生成器对象
obj = create_num(10)
obj2 = create_num(2)

ret = next(obj)
print("obj:", ret)

ret = next(obj)
print("obj:", ret)

ret = next(obj2)
print("obj2:", ret)

ret = next(obj)
print("obj:", ret)

ret = next(obj2)
print("obj2:", ret)

ret = next(obj)
print("obj:", ret)

ret = next(obj)
print("obj:", ret)

ret = next(obj2)
print("obj2:", ret)
