def sum_numbers(num):
    if num == 1:
        return 1

    tmp = sum_numbers(num - 1)

    return num + tmp


print(sum_numbers(4))
