class Cat:

    def __init__(self, new_name):
        # do something in init
        print("initialize...")

        # add a attr
        self.name = new_name

    def eat(self):
        print("%s 爱吃鱼" % self.name)


tom = Cat("Tom")

print(tom.name)

lazy_cat = Cat("大懒猫")
lazy_cat.eat()
