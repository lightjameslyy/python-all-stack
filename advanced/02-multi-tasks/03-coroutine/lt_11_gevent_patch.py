import gevent
from gevent import monkey
import time

monkey.patch_all()

def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)
        # gevent.sleep(0.5)


def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)
        # gevent.sleep(0.5)


def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)
        # gevent.sleep(0.5)

"""
print("----1----")
g1 = gevent.spawn(f1, 5)
print("----2----")
g2 = gevent.spawn(f2, 5)
print("----3----")
g2 = gevent.spawn(f3, 5)
print("----4----")
g1.join()
g2.join()
g2.join()
"""

gevent.joinall([
    gevent.spawn(f1, 5),
    gevent.spawn(f2, 5),
    gevent.spawn(f2, 5)
])