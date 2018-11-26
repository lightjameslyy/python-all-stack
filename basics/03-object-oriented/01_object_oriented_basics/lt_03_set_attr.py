class Cat:

    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 要喝水" % self.name)


# 创建对象
tom = Cat()

# 这种方法有隐患
tom.name = "Tom"

tom.eat()
tom.drink()

print(tom)

# 再创建一个Cat
lazy_cat = Cat()

lazy_cat.name = "大懒猫"

lazy_cat.eat()
lazy_cat.drink()

print(lazy_cat)

lazy_cat2 = lazy_cat

print(lazy_cat2)
