"""
本篇文章地址：
https://mp.weixin.qq.com/s?__biz=Mzg5ODYxMTg0NA==&mid=2247483830&idx=1&sn=04db289664f9271dc75f07b59046623d&chksm=c05eae5df729274b566debff02c623b63b7546bd83a71336f486f69e17ee2b976a6e7566381f&token=627588858&lang=zh_CN#rd
"""

import turtle as t


def tree(n):
    if n > 5:
        t.forward(n)
        t.right(20)
        tree(n-15)   # 在所有此递归调用全部压入栈之后运行下面的代码
        t.left(40)
        tree(n-10)
        t.right(20)
        t.backward(n)


if __name__ == '__main__':
    t.penup()
    t.right(90)
    t.forward(150)
    t.pendown()
    t.left(170)
    tree(100)   # 递归画分支
    t.mainloop()
