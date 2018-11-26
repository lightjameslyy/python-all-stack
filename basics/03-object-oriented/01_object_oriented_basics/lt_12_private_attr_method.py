class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18  # private attribute

    # private method
    def __secret(self):
        print("%s's age: %d" % (self.name, self.__age))


xiaofang = Women("小芳")

# print(xiaofang.__age)  # can't access private attribute

# xiaofang.__secret()  # can't call private method

print(xiaofang._Women__age)
xiaofang._Women__secret()  # crack private
