class A:
    def test(self):
        print("A test")

    def demo(self):
        print("A demo")


class B:
    def test(self):
        print("B test")

    def demo(self):
        print("B demo")


class C(A, B):
    pass


c = C()

# using A
c.test()
c.demo()

# MRO(Method Resolution Order)
print(C.mro())
