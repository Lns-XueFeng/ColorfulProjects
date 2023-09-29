class A:
    oop = ""

    def __init__(self):
        print(self.oop == self.__class__.oop)
        print(self.oop is self.__class__.oop)


class B:
    oop = "oop"

    def __init__(self):
        self.oop = "oop"
        print(self.oop == self.__class__.oop)
        print(self.oop is self.__class__.oop)


class C:
    oop = "oop"

    def __init__(self):
        self.oop = "iip"
        print(self.oop == self.__class__.oop)
        print(self.oop is self.__class__.oop)


class D:
    oop = "oop"

    def __init__(self):
        print(self.oop)
        print(self.__class__.oop)
        self.oop = "iip"
        print(self.oop)
        print(self.__class__.oop)


a = A()
b = B()
c = C()
d = D()
