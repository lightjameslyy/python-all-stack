# 累加求偶数和

i = 0
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1

print("sum of even numbers in [0, 100]: %d" % sum)
