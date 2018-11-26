import threading
import time


def test1(tmp):
    tmp.append(33)
    print("tmp in test1: %s" % str(g_nums))


def test2(tmp):
    print("tmp in test2: %s" % str(tmp))


g_nums = [11, 22]


def main():
    t1 = threading.Thread(target=test1, args=(g_nums,))
    t2 = threading.Thread(target=test2, args=(g_nums,))

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    print("g_num in main: %s" % str(g_nums))


if __name__ == '__main__':
    main()
