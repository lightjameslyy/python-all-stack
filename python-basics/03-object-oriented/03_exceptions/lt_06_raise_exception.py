def input_password():
    pwd = input("请输入密码：")

    if len(pwd) >= 8:
        return pwd

    ex = Exception("密码长度不够")

    raise ex


try:
    user_pwd = input_password()
    print(user_pwd)
except Exception as result:
    print("发现错误 %s" % result)
