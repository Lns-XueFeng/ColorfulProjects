"""
作者：Lns-XueFeng(回到古代见李白)
时间：2022.11.9

爱心形方程：r=a (1-sinθ)
x = 2r(sinθ-1/2sin(2θ))
y = 2r(cosθ-1/2cos(2θ))

x = 16 * (sin(value) ** 3)
y = -(13 * cos(value) - 5 * cos(2 * value) - 2 * cos(3 * value) - cos(4 * value))
最终选择的爱心, 比上面那个更加好看
"""


import random
import math
from math import sin, cos
from tkinter import Tk, Canvas


WIDTH = 800
HEIGHT = 600
LET_X_CENTER = WIDTH / 2
LET_Y_CENTER = HEIGHT / 2


class LoveHeart:
    def __init__(self):
        self.all_point_list = set()   # 生成原始坐标集
        self.frame_point_list = set()   # 心形骨架坐标集
        self.decorate_point_list = set()   # 装饰心形的坐标集
        self.active_point_list = set()   # 随机跳动点坐标集

        self.get_outside()
        self.decorate_list = self.fill_shape()

    @staticmethod
    def count_point(value, enlarge=10.0):
        """
        根据此函数计算出爱心形的坐标
        """
        x = 16 * (sin(value) ** 3)
        y = -(13 * cos(value) - 5 * cos(2 * value) - 2 * cos(3 * value) - cos(4 * value))
        x = enlarge * x
        y = enlarge * y
        return int(x), int(y)

    def get_outside(self):
        """
        得到外型的原始边
        """
        for _ in range(4000):
            rand_value = random.uniform(0.0, 2 * math.pi)
            self.all_point_list.add(self.count_point(rand_value))

    def fill_shape(self):
        """
        得到外型轮廓
        """
        fill_shape_list = []
        for point in self.all_point_list:
            rand_x = random.uniform(-10.0, 10.0)
            rand_y = random.uniform(-10.0, 10.0)
            fill_shape_list.append((point[0] + rand_x, point[1] + rand_y))
        self.all_point_list = {*self.all_point_list, *fill_shape_list}

        decorate_point_list = set()
        for point in self.all_point_list:
            rand_x = random.uniform(-40.0, 40.0)
            rand_y = random.uniform(-40.0, 40.0)
            x_y = (point[0] + rand_x, point[1] + rand_y)
            decorate_point_list.add(x_y)

        return decorate_point_list

    def add_active_point(self):
        """
        创建一堆随机跳动的点
        """
        get_some_points = set()
        for _ in range(50):
            rand_value = random.uniform(0.0, 2 * math.pi)
            get_some_points.add(self.count_point(rand_value, enlarge=7))
        for _ in range(200):
            rand_value = random.uniform(0.0, 2 * math.pi)
            get_some_points.add(self.count_point(rand_value, enlarge=12))
        active_points = set()
        for point in get_some_points:
            rand_x = random.uniform(-20.0, 20.0)
            rand_y = random.uniform(-20.0, 20.0)
            x_y = (point[0] + rand_x, point[1] + rand_y)
            active_points.add(x_y)
        return active_points

    def animate(self, frame):
        """
        利用周期函数对爱心进行周期性放大缩小以达到模拟跳动的目的
        并且将爱心移动到canvas中间
        """
        # 主要轮廓的收缩
        for point in self.all_point_list:
            new_x = period(frame) * point[0] + LET_X_CENTER
            new_y = period(frame) * point[1] + LET_Y_CENTER
            self.frame_point_list.add((new_x, new_y))

        # 装饰的点的收缩
        for point in self.decorate_list:
            new_x = period(frame) * point[0] + LET_X_CENTER
            new_y = period(frame) * point[1] + LET_Y_CENTER
            self.decorate_point_list.add((new_x, new_y))

        # 跳动的点的收缩
        active_points = self.add_active_point()
        for point in active_points:
            new_x = period(frame) * point[0] + LET_X_CENTER
            new_y = period(frame) * point[1] + LET_Y_CENTER
            self.active_point_list.add((new_x, new_y))

    def render(self, canvas, frame):
        self.animate(frame)   # 得到当前这一帧的动态坐标
        # 画出心形骨架
        for point in self.frame_point_list:
            canvas.create_rectangle(
                point[0], point[1], point[0] + 3, point[1] + 3, fill="#ff2121")

        # 装饰心形图形
        for point in self.decorate_point_list:
            canvas.create_rectangle(
                point[0], point[1], point[0] + 2, point[1] + 2, fill="#FF5151")

        # 画出不断跳动的点
        for point in self.active_point_list:
            canvas.create_rectangle(
                point[0], point[1], point[0] + 2, point[1] + 2, fill="#FF5151")


def period(t):
    """周期性跳动"""
    larger = abs(1/2 * sin(t)) + 0.5
    if larger <= 0.8:
        larger = 0.8
    return larger


frame = 0


def draw(main, render_canvas, heart):
    global frame
    render_canvas.delete("all")
    heart.render(render_canvas, frame)
    frame += 1/8 * math.pi
    heart.frame_point_list = set()
    heart.decorate_point_list = set()
    heart.active_point_list = set()
    main.after(60, draw, main, render_canvas, heart)


if __name__ == "__main__":
    root = Tk()
    canvas = Canvas(root, width=WIDTH, height=HEIGHT, background="black")
    canvas.pack()
    heart = LoveHeart()
    draw(root, canvas, heart)
    root.mainloop()
