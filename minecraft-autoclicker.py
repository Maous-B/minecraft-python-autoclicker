import dearpygui.dearpygui as dpg
import time
import random
import string
import win32api, win32con, win32gui
import threading
import os
import sys

dpg.create_context()

letters = string.ascii_letters
string_title = "".join(random.sample(letters, 10))
toggling_clicker = False
toggling_jitterstrength = False

def Toggle():
    global toggling_clicker
    global checkbox_toggle_clicker
    if (dpg.get_value(checkbox_toggle_clicker) == 1):
        toggling_clicker = True
    elif (dpg.get_value(checkbox_toggle_clicker) == 0):
        toggling_clicker = False

def ToggleJitter():
    global toggling_jitterstrength
    global checkbox_toggle_jitter
    if (dpg.get_value(checkbox_toggle_jitter) == 1):
        toggling_jitterstrength = True
    elif (dpg.get_value(checkbox_toggle_jitter) == 0):
        toggling_jitterstrength = False

def AutoClicker():
    global toggling_clicker
    global slider_float1
    global slider_float2
    while True:
        title2 = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        title = win32gui.FindWindow(None, None)
        if "Minecraft" in title2 or "Lunar" in title2 or "Badlion" in title2 or "Client" in title2 or "AZ" in title2:
            title = win32gui.FindWindow(None, title2)
            if win32api.GetAsyncKeyState(0x01) < 0 and toggling_clicker:
                lParam = win32api.MAKELONG(0,0)
                win32api.SendMessage(title, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
                win32api.SendMessage(title, win32con.WM_LBUTTONUP,win32con.MK_LBUTTON, lParam)
                min_cps = (1/dpg.get_value(slider_float1))
                max_cps = (1/dpg.get_value(slider_float2))
                randomzer = random.uniform(min_cps, max_cps)
                time.sleep(randomzer)
            else:
                pass
        elif toggling_clicker != True:
            pass

def JitterStrength():
    global slider_jitter
    while True:
        x_random = random.randint(-1*(dpg.get_value(slider_jitter)), dpg.get_value(slider_jitter))
        y_random = random.randint(-1*(dpg.get_value(slider_jitter)), dpg.get_value(slider_jitter))
        x,y = win32api.GetCursorPos()
        final_position = (x+x_random, y+y_random)
        if win32api.GetAsyncKeyState(0x01)<0 and toggling_jitterstrength:
            win32api.SetCursorPos(final_position)
            time.sleep(0.02)
        elif toggling_jitterstrength != True:
            pass

def Exit():
    dpg.destroy_context()

with dpg.window(tag="Primary Window"):
    with dpg.tab_bar():
        with dpg.tab(label="clicker"):
            slider_float1 = dpg.add_slider_float(label="min cps", default_value=8, max_value=20, min_value=0)
            slider_float2 = dpg.add_slider_float(label="max cps", default_value=12, max_value=20, min_value=0)
            checkbox_toggle_clicker = dpg.add_checkbox(label = "toggle clicker", callback=Toggle)
        with dpg.tab(label="jitter"):
            slider_jitter = dpg.add_slider_int(label="jitter strength", default_value=1, max_value=5, min_value=1)
            checkbox_toggle_jitter = dpg.add_checkbox(label = "toggle jitter", callback=ToggleJitter)
        with dpg.tab(label="settings"):
            button_self_destruct = dpg.add_button(label = "exit", callback=Exit)
    t1 = threading.Thread(target=AutoClicker)
    t1.start()
    t2 = threading.Thread(target=JitterStrength)
    t2.start()


    
dpg.create_viewport(title=string_title, width=600, height=300)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()


