import multiprocessing
import os
import time


nums = [11, 22, 33]

def test1():
    nums.append(44)
    print("nums in subprocess 1: %s" % str(nums))


def test2():
    print("nums in subprocess 2: %s" % str(nums))


def main():
    print("main process: pid=%d, ppid=%d" % (os.getpid(), os.getppid()))

    p1 = multiprocessing.Process(target=test1)
    p1.start()
    p1.join()

    p2 = multiprocessing.Process(target=test2)
    p2.start()


if __name__ == '__main__':
    main()
