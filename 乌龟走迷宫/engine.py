import random
import sys
import time
import turtle
from interface import Interface


class Engine(object):
    def __init__(self, interface):
        turtle.tracer(True)
        turtle.speed(1)
        self.home = (135, 55)
        self.interface = interface
        self.two_dimension_positions = self.interface.two_dimension_positions   # 方块坐标与二维数组的映射
        self.two_dimension_array = self.interface.two_dimension_array

    def birth_to_home(self):
        turtle.penup()
        turtle.goto(self.home)
        turtle.pendown()

    def confirm_block(self, position):
        _position = (round(position[0]), round(position[1]))
        print(_position)
        two_dim_position = self.two_dimension_positions[_position]
        print(two_dim_position)
        value_of_datatxt = self.two_dimension_array[two_dim_position[0]][two_dim_position[1]]
        print(value_of_datatxt)
        if value_of_datatxt == "+":
            return True   # 为墙壁
        return False   # 前方为空

    def turtle_go(self):
        if turtle.position()[0] >= 195:
            time.sleep(10)
            sys.exit()

        turtle.forward(10)
        if self.confirm_block(turtle.position()):
            turtle.backward(10)
            toward_list = ["turtle.right(90)", "turtle.left(90)"]
            exec(random.choice(toward_list))
        self.turtle_go()


if __name__ == "__main__":
    interface = Interface()
    interface.draw_map()
    interface.get_func_dic()
    engine = Engine(interface)
    engine.birth_to_home()
    engine.turtle_go()
    turtle.mainloop()
