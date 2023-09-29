import turtle

WINDOW_WIDTH = 210
WINDOW_HEIGHT = 100


class Interface(object):
    turtle.window_width = WINDOW_WIDTH
    turtle.window_height = WINDOW_HEIGHT

    def __init__(self):
        turtle.tracer(False)
        turtle.showturtle()
        turtle.shape(name="turtle")
        turtle.setworldcoordinates(llx=0, lly=0, urx=210, ury=100)

        self.two_dimension_array = []
        with open("draw_data", 'r') as fp:
            data = fp.readlines()
        for line in data:
            self.two_dimension_array.append(list(line))
        self.two_dimension_positions = {}   # 方块坐标与二维数组的映射

    @staticmethod
    def draw_rectangle():
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)

    def draw_map(self):
        go_y = 0
        for line in reversed(self.two_dimension_array):
            for value in line:
                if value != '\n':
                    if value == "-":
                        turtle.penup()
                    self.draw_rectangle()
                    turtle.pendown()
            go_y += 10
            turtle.penup()
            turtle.goto(0, go_y)
            turtle.pendown()

    def get_func_dic(self):
        position_row = 10
        position_row_index = 0
        for line in self.two_dimension_array:
            position_col_index = 1
            for _ in line:
                if _ != "\n":
                    pos_x = position_col_index * 10 - 5
                    pos_y = position_row * 10 - 5
                    self.two_dimension_positions[(pos_x, pos_y)] = [position_row_index, position_col_index-1]
                    position_col_index += 1
            position_row -= 1
            position_row_index += 1


if __name__ == "__main__":
    interface = Interface()
    interface.get_func_dic()
    print(interface.two_dimension_array)
    print(interface.two_dimension_positions)
