from config import DESCRIPTION, NAME


def ppprint():
    print("在命令中, 在当前包路径时, 输入python -m Projects_tips则会执行__main__.py")
    print(DESCRIPTION)
    print(NAME)


if __name__ == "__main__":
    ppprint()
