class Cat:

    def __init__(self, new_name):
        self.name = new_name
        print("%s is coming" % self.name)

    def __del__(self):
        print("%s is gone" % self.name)

    def __str__(self):
        return "i'm a cat[%s]" % self.name

tom = Cat("Tom")
print(tom)
