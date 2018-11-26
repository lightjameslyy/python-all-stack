import re


def main():
    email = input("input email address: ")
    # ret = re.match(r"^[a-zA-z0-9]{4,20}@163\.com$", email)
    # |: 或, (): 分组
    ret = re.match(r"^([a-zA-z0-9]{4,20})@(163|126|gmail|sina)\.com$", email)
    if ret:
        print("变量名： %s 符合要求, 匹配结果： %s" % (email, ret.group()))
        print(ret.group(1), ret.group(2))
    else:
        print("变量名： %s 不符合要求" % email)


if __name__ == '__main__':
    main()
