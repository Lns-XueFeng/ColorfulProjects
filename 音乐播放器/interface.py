from tkinter import *


WINDOW_TITLE = "音乐播放器"
WINDOW_SIZE = "350x480-0+30"


class Interface:
    """音乐播放器的交互界面"""
    def __init__(self, root, func):
        self.root = root
        self.root.title(WINDOW_TITLE)
        self.root.geometry(WINDOW_SIZE)
        self.root.resizable(False, False)
        self.root.configure(bg="gray")
        self.var = StringVar()
        self.list_box = Listbox(self.root, bg="white", width=50, height=10, fg="black",
                                font=("楷体", 26, "italic"), bd=1, selectmode=MULTIPLE, listvariable=self.var)
        self.list_box.pack()

        self.btn_text = StringVar()
        self.btn_text.set("全部播放")
        self.button = Button(self.root, textvariable=self.btn_text, width=50, height=2, bg="#005AB5",
                             font=("Times", 30, "bold"), bd=1, command=func)
        self.button.pack()
