# -*- coding: UTF-8 -*-
import time
import pyautogui


def toRun():
    # 设置间隔几秒移动一次鼠标
    iSeconds = 3

    while True:
        pyautogui.move(100, 0, 0.5)
        pyautogui.move(-100, 0, 0.5)
        time.sleep(iSeconds)


if __name__ == "__main__":
    toRun()
