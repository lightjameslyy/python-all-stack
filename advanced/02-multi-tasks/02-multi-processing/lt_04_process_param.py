import multiprocessing
import os
import time


def test(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


def main():
    # 主进程先运行，子进程顺序不确定
    print("main process: pid=%d, ppid=%d" % (os.getpid(), os.getppid()))

    p = multiprocessing.Process(target=test, args=(1, 2, 3, 4, 5, 6, 7, 8), kwargs={"name": "terryleo"})
    p.start()


if __name__ == '__main__':
    main()
