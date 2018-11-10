import time


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
    sing()
    dance()


if __name__ == '__main__':
    main()
