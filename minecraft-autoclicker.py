import dearpygui.dearpygui as dpg
import time
import random
import string
import win32api, win32con, win32gui
import threading

dpg.create_context()

letters = string.ascii_letters
string_title = "".join(random.sample(letters, 10))

toggling = False

def Toggle():
    global toggling
    global checkbox_
    if (dpg.get_value(checkbox_) == 1):
        toggling = True
    elif (dpg.get_value(checkbox_) == 0):
        toggling = False

def AutoClicker():
    global toggling
    global slider_float1
    global slider_float2
    while True:
        title2 = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        title = win32gui.FindWindow(None, None)
        if "Minecraft" in title2 or "Lunar" in title2 or "Badlion" in title2 or "Client" in title2 or "AZ" in title2:
            title = win32gui.FindWindow(None, title2)
            if win32api.GetAsyncKeyState(0x01) < 0 and toggling:
                lParam = win32api.MAKELONG(0,0)
                win32api.SendMessage(title, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
                win32api.SendMessage(title, win32con.WM_LBUTTONUP,win32con.MK_LBUTTON, lParam)
                min_cps = (1/dpg.get_value(slider_float1))
                max_cps = (1/dpg.get_value(slider_float2))
                randomzer = random.uniform(min_cps, max_cps)
                time.sleep(randomzer)
            else:
                pass
        elif toggling != True:
            pass


with dpg.window(tag="Primary Window"):
    checkbox_ = dpg.add_checkbox(label = "Toggle", callback=Toggle)
    slider_float1 = dpg.add_slider_float(label="min cps", default_value=8, max_value=100)
    slider_float2 = dpg.add_slider_float(label="max cps", default_value=12, max_value=100)
    t1 = threading.Thread(target=AutoClicker)
    t1.start()
dpg.create_viewport(title=string_title, width=50, height=50)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()

