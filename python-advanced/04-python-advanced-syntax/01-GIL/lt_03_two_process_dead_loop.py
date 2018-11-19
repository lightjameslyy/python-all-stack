import multiprocessing


# 子进程死循环
def deadLoop():
    while True:
        pass


t1 = multiprocessing.Process(target=deadLoop)
t1.start()

# 主进程死循环
while True:
    pass
