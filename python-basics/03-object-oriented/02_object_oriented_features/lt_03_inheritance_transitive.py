class Animal:

    def eat(self):
        print("eat...")

    def drink(self):
        print("drink...")

    def run(self):
        print("run...")

    def sleep(self):
        print("sleep...")


class Dog(Animal):

    def bark(self):
        print("wang wang wang...")


class XiaoTianQuan(Dog):

    def fly(self):
        print("i can fly...")


class Cat(Animal):

    def catch(self):
        print("catch mouse")


wangcai = XiaoTianQuan()

wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()
wangcai.fly()

cat = Cat()
cat.eat()
cat.catch()
