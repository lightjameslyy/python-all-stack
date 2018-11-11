from collections import Iterable
import time


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象Iterable,必须实现__iter__方法"""
        return ClassIterator(self)


class ClassIterator(object):

    def __init__(self, obj):
        self.obj = obj
        self.cur_index = 0

    def __iter__(self):
        pass

    def __next__(self):
        ret = self.obj.names[self.cur_index]
        self.cur_index += 1
        return ret


classmate = Classmate()

classmate.add("mary")
classmate.add("terry")
classmate.add("james")

# print("is classmate iterable?: ", isinstance(classmate, Iterable))
#
# classmate_iter = iter(classmate)
# print("is classmate_iter iterable?: ", isinstance(classmate_iter, Iterable))
#
# print(next(classmate_iter))

for name in classmate:
    print(name)
    time.sleep(1)
