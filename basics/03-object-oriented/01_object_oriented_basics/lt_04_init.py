class Cat:

    def __init__(self):
        # do something in init
        print("initialize...")

        # attribute for all objects of Cat
        self.name = "Tom"

    def eat(self):
        print("%s 爱吃鱼" % self.name)


tom = Cat()
tom.eat()

print(tom.name)
