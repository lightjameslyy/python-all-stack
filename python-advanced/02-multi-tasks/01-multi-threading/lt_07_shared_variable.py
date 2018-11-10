import threading
import time

# define a global variable
g_num = 100


def test1():
    global g_num
    g_num += 1
    print("g_num in test1: %d" % g_num)


def test2():
    print("g_num in test2: %d" % g_num)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    print("g_num in main: %d" % g_num)


if __name__ == '__main__':
    main()
