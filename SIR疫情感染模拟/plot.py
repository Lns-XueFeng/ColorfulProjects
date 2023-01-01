import multiprocessing


class Plot(multiprocessing.Process):
    def __init__(self, infectious_num_li):
        super().__init__(daemon=True)
        self.data_queue = infectious_num_li

    def update(self, frame):
        self.data = []
        # self.draw_data.append(frame ** 2)
        for ele in self.data_queue.get():
            self.data.append(ele)
        y = self.data
        x = [i for i in range(len(self.data))]
        self.ax.relim()
        self.ax.autoscale_view()
        self.line.set_data(x, y)
        return self.line,

    def animate_init(self):
        self.line.set_data([], [])
        return self.line,

    def run(self):
        from matplotlib import pyplot as plt
        from matplotlib import animation
        self.figure = plt.figure()
        self.ax = plt.axes()
        self.line, = self.ax.plot([1, 2, 3], [2, 3, 5])
        """上述代码放入run函数，并且在外部使用start()运行时才会真正另外开启一个进程进行渲染"""
        animation.FuncAnimation(self.figure, self.update, init_func=self.animate_init,
                                          frames=100, interval=100, blit=False)
        plt.show()
