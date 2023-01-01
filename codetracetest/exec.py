from trace import start, stop, output


def func1():
    print("ok")


def func2():
    func1()


def func3():
    func2()


def func4():
    func3()


if __name__ == "__main__":
    start()
    func4()
    stop()
    output()
