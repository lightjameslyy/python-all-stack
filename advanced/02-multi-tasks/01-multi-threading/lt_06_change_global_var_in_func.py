num = 100
nums = [11, 22]


def test():
    global num

    num += 100


# 修改全局变量的指向需要加global，如果只修改内容，不用加global
def test2():
    nums.append(33)
    # num2 += [100, 200]


print(num)
print(nums)

test()
test2()

print(num)
print(nums)
