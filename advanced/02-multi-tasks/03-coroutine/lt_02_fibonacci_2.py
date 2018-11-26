class Fibonacci(object):
    def __init__(self, size):
        self.size = size
        self.cur_index = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        """如果想要一个对象Iterable,必须实现__iter__方法"""
        return self

    def __next__(self):
        """迭代器Iterator必须实现__iter__方法和__next__方法"""
        if self.cur_index >= self.size:
            self.cur_index = 0
            self.a = 0
            self.b = 1
            raise StopIteration
        ret = self.a
        self.a, self.b = self.b, self.a + self.b
        self.cur_index += 1
        return ret


fib = Fibonacci(10)

for num in fib:
    print(num)

for num in fib:
    print(num)
