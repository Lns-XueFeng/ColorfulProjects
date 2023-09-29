import threading
from tkinter import *
import os

import pygame
from mutagen.mp3 import MP3

from interface import Interface


SONG_OF_PATH = "D:\\周杰伦歌曲\\最伟大的作品"
PLAY_ALL = "全部播放"
PAUSE_ALL = "暂停播放"
PLAY = "播放"
PAUSE = "暂停"


def thread(engine):
    engine.play_music()


class Engine(threading.Thread):
    """音乐播放器的功能实现"""
    def __init__(self, root):
        super().__init__(daemon=True)
        self.gui = Interface(root, self.button_control)

        self.current_selected_list = []
        self.curselection = None
        self.song_of_path = SONG_OF_PATH
        self.song_of_name = os.listdir(self.song_of_path)
        self.list_box = self.gui.list_box
        for name in self.song_of_name:
            name = name.strip(".mp3")
            self.list_box.insert(END, name)
        self.list_box.bind("<<ListboxSelect>>", self.get_selected_item)
        self.button = self.gui.button
        self.button.bind()
        self.play = False   # button控制的bool

    def get_selected_item(self, event):
        """触发被选择时事件"""
        self.curselection = self.list_box.curselection()
        self.current_selected_list = []
        print(self.curselection)
        for index in self.curselection:
            self.current_selected_list.append(self.song_of_name[index])
        self.gui.btn_text.set(PLAY)
        print(self.current_selected_list)

    @staticmethod
    def music_ready(music_path_list):
        pygame.mixer.init()
        if len(music_path_list) == 1:
            print(music_path_list[0])
            music_obj = MP3(music_path_list[0])
            music_duration = music_obj.info.length
            print("音乐时常：" + str(round(music_duration, 0)))
            pygame.mixer.music.load(music_path_list[0])
            pygame.mixer.music.play()
            pygame.time.delay(int(music_duration) * 1000)  # 相当于设置了这些音乐不同的播放等待时间
        else:
            for path in music_path_list:
                print(path)
                music_obj = MP3(path)
                music_duration = music_obj.info.length
                print("音乐时常：" + str(round(music_duration, 0)))
                pygame.mixer.music.load(path)
                pygame.mixer.music.play()
                pygame.time.delay(int(music_duration) * 1000)  # 相当于设置了这些音乐不同的播放等待时间

    def play_music(self):
        if not self.current_selected_list:
            """按顺序自动全部播放"""
            music_path_list = [SONG_OF_PATH + "\\" + name for name in self.song_of_name]
            self.music_ready(music_path_list)
            self.gui.btn_text.set(PLAY_ALL)

        else:
            music_path_list = [SONG_OF_PATH + "\\" + name for name in self.current_selected_list]
            print(music_path_list)
            self.music_ready(music_path_list)
            self.gui.btn_text.set(PLAY)

    def button_control(self):
        btn_text = self.gui.btn_text.get()
        if btn_text == PLAY_ALL:
            t1 = threading.Thread(target=thread, args=(self,))
            t1.start()
            self.gui.btn_text.set(PAUSE_ALL)
        elif btn_text == PAUSE_ALL:
            pygame.mixer.music.pause()
            self.gui.btn_text.set(PLAY_ALL)
        elif btn_text == PLAY:
            t1 = threading.Thread(target=thread, args=(self,))
            t1.start()
            self.gui.btn_text.set(PAUSE)
        elif btn_text == PAUSE:
            pygame.mixer.music.pause()
            self.gui.btn_text.set(PLAY)

            self.current_selected_list = []  # 播放完成需要清空播放列表


if __name__ == "__main__":
    root = Tk()
    engine = Engine(root)
    engine.start()
    root.mainloop()
