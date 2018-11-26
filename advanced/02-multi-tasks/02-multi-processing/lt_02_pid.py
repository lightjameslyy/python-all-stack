import multiprocessing
import os
import time


def test1():
    print("subprocess: pid=%d, ppid=%d" % (os.getpid(), os.getppid()))
    time.sleep(1)


def main():
    print("main process: pid=%d, ppid=%d" % (os.getpid(), os.getppid()))
    p1 = multiprocessing.Process(target=test1)
    p1.start()


if __name__ == '__main__':
    main()
