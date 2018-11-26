import time


def task1():
    while True:
        print("task 1")
        time.sleep(0.5)
        yield


def task2():
    while True:
        print("task 2")
        time.sleep(0.5)
        yield


def main():
    t1 = task1()
    t2 = task2()
    while True:
        next(t1)
        next(t2)


if __name__ == '__main__':
    main()
