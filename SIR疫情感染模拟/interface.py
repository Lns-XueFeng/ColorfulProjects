import tkinter
import multiprocessing

from .engine import Engine
from .plot import Plot


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800
PERSON_NUMBERS = 500   # 生成人数


class Interface:
    def __init__(self):
        self.root = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack()
        self.engine = Engine(CANVAS_WIDTH, PERSON_NUMBERS)
        self.data_queue = multiprocessing.Queue()
        self.plot = Plot(self.data_queue)
        self.engine.create_people()
        self.infectious_num_li = []

    def draw_people(self):
        color = {
            "susceptible": "green",
            "infectious": "red",
            "recovered": "yellow"
        }
        for person in self.engine.person_li:
            self.canvas.create_rectangle(person.x, person.y, person.x + 5, person.y + 5
                                         , fill=color[person.status], outline=color[person.status])

    def next_frame(self):
        self.engine.next_frame()
        self.canvas.delete("all")
        self.draw_people()
        self.infectious_num_li.append(self.engine.infectious_people_num)
        self.data_queue.put(self.infectious_num_li)
        self.root.after(30, self.next_frame)

    def start(self):
        self.engine.infect()
        self.root.after(30, self.next_frame)
        self.plot.start()
        self.root.mainloop()
