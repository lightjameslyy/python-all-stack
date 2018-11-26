
# Python 提供了 with 语法用于简化资源操作的后续清除操作，是 try/finally 的替代方法，实现原理建立在上下文管理器之上。此外，Python 还提供了一个 contextmanager 装饰器，更进一步简化上下管理器的实现方式。

# 1. 任何实现了 __enter__() 和 __exit__() 方法的对象都可称之为上下文管理器。


class File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("entering")
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, *args):
        print("will exit")
        self.f.close()


with File('out1.txt', 'w') as f:
    print("writing")
    f.write('hello, python')

# 2. Python 还提供了一个 contextmanager 的装饰器，更进一步简化了上下文管理器的实现方式。通过 yield 将函数分割成两部分，yield 之前的语句在 __enter__ 方法中执行，yield 之后的语句在 __exit__ 方法中执行。紧跟在 yield 后面的值是函数的返回值。
from contextlib import contextmanager


@contextmanager
def my_open(path, mode):
    f = open(path, mode)
    yield f
    f.close()


with my_open('out2.txt', 'w') as f:
    f.write("hello , the simplest context manager")
