def test(num):
    print("address of %d in test func: %d" % (num, id(num)))

    result = "hello"

    print("address of result: %d" % id(result))

    return result

a = 10

print("address of a: %d" % id(a))

test(a)

a = 12

r = test(a)
print("address of result outside func: %d" % id(r))