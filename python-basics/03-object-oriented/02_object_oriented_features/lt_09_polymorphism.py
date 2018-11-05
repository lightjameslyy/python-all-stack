class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s is gaming..." % self.name)


class XiaoTianDog(Dog):

    def game(self):
        print("%s is gaming in the sky..." % self.name)


class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s game with %s" % (self.name, dog.name))
        dog.game()


# wangcai = Dog("旺财")
wangcai = XiaoTianDog("飞天旺财")

xiaoming = Person("xiaoming")

xiaoming.game_with_dog(wangcai)
