class Person:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "my name is %s, weight %.2f" % (self.name, self.weight)

    def run(self):
        print("%s like running, running makes me healthier!" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s eat something, then go to run!" % self.name)
        self.weight += 1


xiaoming = Person("xiaoming", 75.0)
xiaoming.run()
xiaoming.eat()
print(xiaoming)

xiaomei = Person("xiaomei", 45.0)
xiaomei.run()
xiaomei.eat()
print(xiaomei)

print(xiaoming)
