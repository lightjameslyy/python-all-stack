import time
import threading


def sing():
    """sing for 5 seconds"""

    for i in range(5):
        print("singing...")
        time.sleep(1)


def dance():
    """dance for 5 seconds"""

    for i in range(5):
        print("dancing...")
        time.sleep(1)


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
