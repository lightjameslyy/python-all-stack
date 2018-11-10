import multiprocessing


def download_from_web(q):
    """fake download from web"""

    data = [11, 22, 33, 44]

    # write to queue
    for tmp in data:
        q.put(tmp)

    print("downloading done.")


def analysis_data(q):
    """process data"""

    waitting_analysis_data = list()

    # get data from queue
    while True:
        data = q.get()
        waitting_analysis_data.append(data)
        # if q.empty():
        if len(waitting_analysis_data) == 4:
            break

    print(waitting_analysis_data)


def main():
    # 1. create a queue
    q = multiprocessing.Queue(4)

    # 2. commuciating through queue
    p1 = multiprocessing.Process(target=download_from_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))

    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
