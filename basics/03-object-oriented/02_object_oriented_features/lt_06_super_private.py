class A:

    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("private %d %d" % (self.num1, self.__num2))


    def test(self):
        print(self.__num2)
        self.__test()


class B(A):
    def demo(self):
        # print("super private: %d" % self.__num2)  # illegal

        # self.__test()  # illegal
        self.test()



b = B()
print(b)

# print(b.__num2)  # illegal
# print(b.__test())  # illegal
b.test()
