import threading
import time


def test1():
    for i in range(5):
        print("test1: %d" % i)
        time.sleep(1)


def main():
    # before creating thread
    print(threading.enumerate())
    t1 = threading.Thread(target=test1)

    # after creating thread
    print(threading.enumerate())
    t1.start()

    # after starting thread
    print(threading.enumerate())


if __name__ == '__main__':
    main()
