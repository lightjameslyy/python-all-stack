# 输入年龄
age = int(input("请输入年龄："))

# check if adult
if age >= 18:
    # if older than 18, allowed to go to Internet cafe
    print("您已成年，可以进网吧")
else:
    # 如果未成年，回家写作业
    print("你还没成年，回家写作业！")

print("这句代码肯定会执行")
