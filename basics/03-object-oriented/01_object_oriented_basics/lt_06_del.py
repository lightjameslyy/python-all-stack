class Cat:

    def __init__(self, new_name):
        self.name = new_name
        print("%s is coming" % self.name)

    def __del__(self):
        print("%s is gone" % self.name)


tom = Cat("Tom")
print(tom.name)

# del时会调用__del__内建方法
# del tom

print("-" * 50)
