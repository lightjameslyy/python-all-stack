def sum_nums(*args):
    res = 0

    for num in args:
        res += num

    return res


result = sum_nums(1, 2, 3)
print(result)
