# -*- coding: utf-8 -*-
import time
import pyautogui


# 设置固定间隔移动一次鼠标（单位: 秒）
iSECONDS = 3


def _move(_time):
    while True:
        pyautogui.move(100, 0, 0.5)
        pyautogui.move(-100, 0, 0.5)
        time.sleep(_time)


def main():
    try:
        _move(iSECONDS)
    except Exception as exc:
        main()
    else:
        pass


if __name__ == "__main__":
    main()
