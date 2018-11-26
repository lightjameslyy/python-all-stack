from multiprocessing import Pool
import os, time, random


def worker(msg):
    t_start = time.time()
    print("worker[%s] starts, pid: %d" % (msg, os.getpid()))
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print("worker[%s] finished, time: %0.2f" % (msg, t_stop - t_start))


pool = Pool(2)
for i in range(0, 10):
    pool.apply_async(worker, (i,))

print("start...")
pool.close()
pool.join()
print("end...")
