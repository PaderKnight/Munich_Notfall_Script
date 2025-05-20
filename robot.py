import pyautogui
import time
import pyautogui
import time
import keyboard
import threading
import pyautogui
import threading
import winsound
from pyautogui import ImageNotFoundException, FailSafeException
import os

import tkinter as tk
from PIL import ImageGrab



class ScreenCapture:
    def __init__(self, image_name):
        self.start_x = None
        self.start_y = None
        self.rect = None
        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-alpha", 0.3)
        self.canvas = tk.Canvas(self.root, cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<ButtonPress-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)
        self.image_name = image_name

    def on_mouse_down(self, event):
        self.start_x = self.root.winfo_pointerx()
        self.start_y = self.root.winfo_pointery()
        self.rect = self.canvas.create_rectangle(
            self.start_x, self.start_y, self.start_x, self.start_y,
            outline="red", width=2
        )

    def on_mouse_drag(self, event):
        cur_x = self.root.winfo_pointerx()
        cur_y = self.root.winfo_pointery()
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_mouse_up(self, event):
        end_x = self.root.winfo_pointerx()
        end_y = self.root.winfo_pointery()
        self.root.destroy()

        left = min(self.start_x, end_x)
        top = min(self.start_y, end_y)
        right = max(self.start_x, end_x)
        bottom = max(self.start_y, end_y)

        img = ImageGrab.grab(bbox=(left, top, right, bottom))
        img.save(self.image_name)
        print(f"Screenshot saved as '{self.image_name}'")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":

################## Screenshot function, in order to check against the presence or absence of termin. the second run can be done without it. ##################
    stop_flag = threading.Event()
    # pyautogui.moveTo(50, 300)
    # pyautogui.click()
    # pyautogui.press('f5')
    
    # 检查文件是否存在
    if not os.path.exists("robot.png"):
        cap = ScreenCapture("robot.png")
        cap.run()
    else:
        print("robot.png 已存在，跳过截图。")

##########################################################################################################################################################################
    

# 等待一会儿，确保文件保存
    time.sleep(1)

    # 在屏幕上查找截图
    location = pyautogui.locateOnScreen('robot.png', confidence=0.8)
    if location:
        center = pyautogui.center(location)
        pyautogui.click(center)
        print(f"已点击位置：{center}")
        time.sleep(3)
    else:
        print("未找到截图对应的位置。")

    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')

    if not os.path.exists("calendar.png"):
        print("请在屏幕上选择日历的区域...")
        cap1 = ScreenCapture("calendar.png")
        cap1.run()
    else:
        print("calendar.png 已存在，跳过截图。")
    
    for a in range(1000):
        try:
            image_found = pyautogui.locateOnScreen("calendar.png")
        except ImageNotFoundException:
            image_found = False

        if a != 0 and (stop_flag.is_set() or not image_found):
            winsound.Beep(1000, 500)  
            print("-------------got it, now!!!!!!!--------")
            break
        pyautogui.press('f5')
        time.sleep(3)
        location = pyautogui.locateOnScreen('robot.png', confidence=0.8)
        if location:
            center = pyautogui.center(location)
            pyautogui.click(center)
            print(f"已点击位置：{center}")
        else:
            print("未找到截图对应的位置。")

        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')

        time.sleep(3)
        print(a)
