import re


def main():
    # findall 返回所有匹配结果的列表，不需要再用group方法
    ret = re.findall(r"\d+", "阅读次数为 9999, 点赞数： 100, c++: 1000")
    print(ret)


if __name__ == '__main__':
    main()
