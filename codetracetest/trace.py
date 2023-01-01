"""
理解sys.setprofile()使用与原理
"""

import sys

__all__ = ['start', 'stop', 'output']

EXCLUSIONS = {'<'}
CALL_EVENT_LIST = []


def tracefunc(frame, event, arg):
    if event == "call":
        tracefunc.stack_level += 1

        unique_id = frame.f_code.co_filename + str(frame.f_lineno)
        if unique_id in tracefunc.memorized:
            return

        # Part of filename MUST be in white list.
        if 'self' in frame.f_locals:
            class_name = frame.f_locals['self'].__class__.__name__
            func_name = class_name + '.' + frame.f_code.co_name
        else:
            func_name = frame.f_code.co_name

        func_name = '{indent}{name}'.format(
            indent=tracefunc.stack_level * 2 * '-', name=func_name)

        frame_back = frame.f_back  # 获取调用函数时的信息
        txt = '{: <40} # {}, {}, {}, {}'.format(
            func_name, frame.f_code.co_filename, frame.f_lineno, frame_back.f_code.co_filename, frame_back.f_lineno)

        CALL_EVENT_LIST.append(txt)

        tracefunc.memorized.add(unique_id)

    elif event == "return":
        tracefunc.stack_level -= 1


def start():
    tracefunc.memorized = set()
    tracefunc.stack_level = 0
    CALL_EVENT_LIST.clear()
    sys.setprofile(tracefunc)


def output():
    for text in CALL_EVENT_LIST:
        print(text)

    CALL_EVENT_LIST.clear()


def stop():
    sys.setprofile(None)
