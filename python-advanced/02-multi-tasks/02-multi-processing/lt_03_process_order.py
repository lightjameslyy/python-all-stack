import multiprocessing
import os
import time


def test1():
    print("subprocess 1: pid=%d, ppid=%d" % (os.getpid(), os.getppid()))
    time.sleep(1)


def test2():
    print("subprocess 2: pid=%d, ppid=%d" % (os.getpid(), os.getppid()))
    time.sleep(1)


def main():
    # 主进程先运行，子进程顺序不确定
    print("main process: pid=%d, ppid=%d" % (os.getpid(), os.getppid()))
    p1 = multiprocessing.Process(target=test1)
    p1.start()

    p2 = multiprocessing.Process(target=test2)
    p2.start()


if __name__ == '__main__':
    main()
