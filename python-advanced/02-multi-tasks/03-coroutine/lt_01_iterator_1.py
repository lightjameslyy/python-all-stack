from collections import Iterable


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象Iterable,必须实现__iter__方法"""
        return ClassIterator()


class ClassIterator(object):
    def __iter__(self):
        pass

    def __next__(self):
        pass


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
