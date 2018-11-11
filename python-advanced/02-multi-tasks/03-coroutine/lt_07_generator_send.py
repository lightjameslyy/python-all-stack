def create_num(size):
    a, b = 0, 1
    cur_index = 0
    while cur_index < size:
        ret = yield a
        print(">>>ret:", ret)
        a, b = b, a + b
        cur_index += 1


obj = create_num(10)

# obj.send(None)  # send一般不会在第一次启动生成器的时候使用，如果非要用，传递None

ret = next(obj)
print(ret)

ret = next(obj)
print(ret)

ret = obj.send("hello")
print(ret)
