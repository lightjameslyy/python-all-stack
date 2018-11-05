class A:
    def test(self):
        print("A test")


class B:
    def demo(self):
        print("B demo")


class C(A, B):
    pass


c = C()

c.test()
c.demo()
