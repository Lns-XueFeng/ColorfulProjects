import datetime
import time
from collections import deque
from set_todo_task import TASK_TODO_LIST


class Record:
    def __init__(self):
        self._record_list = TASK_TODO_LIST

    @property
    def record_list(self):
        return self._record_list


class Task:
    def __init__(self, todo_task):
        self.todo_task = todo_task
        self.duration = 0
        self.finish = False

    def __repr__(self):
        return f"<Task todo_task={self.todo_task}, " \
               f"duration={self.duration}, finish={self.finish}>"


class Timer:
    def __init__(self):
        self.time = 0

    def __enter__(self):
        self.time = time.time()
        return self   # 要返回实例, 不然找不到相应的方法

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def get_time(self):
        return time.time() - self.time


class ToDo:
    record = Record()

    def __init__(self):
        self._todo_list = self.record.record_list
        self.task_list = deque(Task(to_do) for to_do in self._todo_list)
        self.update_txt_status(line_break=True, begin=True)

    @classmethod
    def display_statement_string(cls, char, string, line_break=False):
        if char == "*":
            print("<{:*^80}>".format(string))
        elif char == "-":
            print("<{:-^80}>".format(string))
        else:
            assert (False, "No support other char except for * and -.")

        if line_break:
            print("")

    def display_todo(self):
        self.display_statement_string("*", "今日需完成任务")
        for task in self.task_list:
            self.display_statement_string("-", str(task))
        self.display_statement_string("*", "赶紧开始任务吧", line_break=True)
        input()

    def update_txt_status(self, line_break=False, begin=False, end=False):
        task_of_lines = ""
        for task in self.task_list:
            task_of_lines += str(task) + "\n"

        with open("task_results.txt", "a", encoding="utf-8") as fp:
            date = datetime.datetime
            if line_break:
                fp.write("\n\n")
            if begin:
                fp.write(str(date.today().strftime("%Y-%m-%d %H:%M")) + "开始：" + "\n")
            if end:
                fp.write(str(date.today().strftime("%Y-%m-%d %H:%M")) + "结束：" + "\n")
            fp.write(task_of_lines)

    def display_process(self):
        self.display_statement_string("*", "任务正在进行时", line_break=True)
        for task in self.task_list:
            with Timer() as t:
                todo_task = f"<Task todo_task={task.todo_task}>"
                input("<{:-^80}>".format("启动下一个任务") + "\n")
                self.display_statement_string("-", todo_task)
                input("<{:-^80}>".format("完成任务请回车") + "\n")
                duration = round(t.get_time(), 0)
            task.duration = str(duration) + "s"
            task.finish = True
        self.update_txt_status(end=True)  # 更新状态
        print("")

        self.display_statement_string("*", "任务的完成情况", line_break=True)

    def display_result(self):
        """
        模仿Github的哪块板子来可视化显示本月完成情况或自定义时间内
        前期先用字符进行print输出显示, 后面可以用tkinter/turtle画一个图出来
        """
        for task in self.task_list:
            self.display_statement_string("-", str(task), line_break=True)

        for i in range(7):
            day_case = ""
            for j in range(52):
                day_case += "+"
            self.display_statement_string("-", day_case)

    def control_Progress(self):
        self.display_todo()   # 可视化展示需要完成的任务
        self.display_process()  # 可视化展示任务完成的过程
        self.display_result()   # 可视化展示任务最终完成情况


if __name__ == "__main__":
    todo = ToDo()
    todo.control_Progress()
