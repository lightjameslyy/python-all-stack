import re


def main():
    ret = re.split(r":| ", "info:hello light james")
    print(ret)


if __name__ == '__main__':
    main()
