def create_num(size):
    a, b = 0, 1
    cur_index = 0
    while cur_index < size:
        # print(a)
        yield a  # 如果一个函数有yield语句，那么这个函数就是一个生成器模板
        a, b = b, a + b
        cur_index += 1
    return "ok"


obj2 = create_num(10)

while True:
    try:
        ret = next(obj2)
        print("obj2:", ret)
    except Exception as ret:
        print(ret.value)
        break
