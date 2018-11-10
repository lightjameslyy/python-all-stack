import threading
import time

# define a global variable
g_num = 0

# create a mutex
mutex = threading.Lock()


def test1(num):
    global g_num
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()
    print("g_num in test1: %d" % g_num)


def test2(num):
    global g_num
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()
    print("g_num in test2: %d" % g_num)


def main():
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))

    t1.start()
    t2.start()

    time.sleep(2)

    print("g_num in main: %d" % g_num)


if __name__ == '__main__':
    main()
