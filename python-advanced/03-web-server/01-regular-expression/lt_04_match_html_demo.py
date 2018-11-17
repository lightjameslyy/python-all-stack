import re


def main():
    html_strs = [
        "<h1>hahaha</h1>",
        "<h1>hahaha</h2>",
        "<body><h1>hahaha</h1></body>",
    ]

    for html_str in html_strs:
        # ret = re.match(r"<\w*>.*</\w*>", html_str)

        # 使用分组确保标签名一致
        # ret = re.match(r"<(\w*)>.*</\1>", html_str)

        # 多个标签
        # ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", html_str)

        # 对匹配命名
        ret = re.match(r"<(?P<p1>\w*)><(?P<p2>\w*)>.*</(?P=p2)></(?P=p1)>", html_str)

        if ret:
            print("变量名： %s 符合要求, 匹配结果： %s" % (html_str, ret.group()))
        else:
            print("变量名： %s 不符合要求" % html_str)


if __name__ == '__main__':
    main()
