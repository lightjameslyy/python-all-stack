try:
    num = int(input("输入一个整数："))
    result = 8 / num
    print(result)
except ValueError:
    print("输入正确的整数")
except ZeroDivisionError:
    print("除0错误")
except Exception as result:
    print("未知错误 %s" % result)
else:
    print("正常执行")
finally:
    print("无论是否出错都会执行")

print("-" * 50)
