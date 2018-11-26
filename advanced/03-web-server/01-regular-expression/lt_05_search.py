import re


def main():
    # search 匹配到第一个就退出
    ret = re.search(r"\d+", "阅读次数为 9999, 点赞数： 100")
    print(ret.group())


if __name__ == '__main__':
    main()
