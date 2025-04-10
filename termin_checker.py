import pyautogui
import time
import keyboard
import threading
import pyautogui
import threading
import winsound
from pyautogui import ImageNotFoundException, FailSafeException


import tkinter as tk
from PIL import ImageGrab
# from plyer import notification

stop_flag = threading.Event()

# load screenshot from cap
image_path = 'screenshot.png'


def enroll_class():
    # time.sleep(5)

    pyautogui.moveTo(50, 1040)
    pyautogui.click()
    for a in range(1000):
        try:
            image_found = pyautogui.locateOnScreen(image_path)
        except ImageNotFoundException:
            image_found = False

        if a != 0 and (stop_flag.is_set() or not image_found):
            winsound.Beep(1000, 500)  
            print("-------------got it, now!!!!!!!--------")
            break
        pyautogui.press('f5')
        time.sleep(3)
        for i in range(20):
            pyautogui.press('tab')
        pyautogui.press('enter')
        for i in range(3):
            pyautogui.press('tab')

        time.sleep(3)
        print(a)

def run_script():
    try:
        # run enroll_class
        enroll_thread = threading.Thread(target=enroll_class)
        enroll_thread.start()

        # wait press 1 to stop script
        print("Press 1 to stop the script.")
        keyboard.wait('1')
        stop_flag.set()  
        enroll_thread.join()  
        print("Script stopped.")
    except Exception as e:
        print(f"Script terminated due to: {e}")


class ScreenCapture:
    def __init__(self):
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
        img.save("screenshot.png")
        print("📸 Screenshot saved as 'screenshot.png'")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":

################## Screenshot function, in order to check against the presence or absence of termin. the second run can be done without it. ##################

    cap = ScreenCapture()
    cap.run()
    
##############################################################################################################################################################

    run_script()


