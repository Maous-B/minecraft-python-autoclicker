from tkinter import *
import win32api, win32gui, win32con
import time
import random
import threading

toggling = False
def Initialize_Window():
    global scale_min_value
    global scale_max_value
    global x
    window = Tk()
    x = IntVar()
    window.title("Autoclicker v1.3")
    #window.geometry("420x420")
    window.config(background="#ffffff")
    check_box = Checkbutton(window, text="Toggle Clicker", variable=x, onvalue=1, offvalue=0, command=Toggle)
    label = Label(window,text="Autoclicker v1.3 by Maous-B", font=('Arial',20,'bold'))
    label2 = Label(window,text="ONLY WORK IF MINECRAFT WINDOW IS OPENED !!!", font=('Arial',10,'bold'))
    scale_min_value = Scale(window, from_=1, to=20, orient=HORIZONTAL, tickinterval=1, length = 400)
    scale_max_value = Scale(window, from_=1, to=20, orient=HORIZONTAL, tickinterval=1, length = 400)
    scale_min_value.pack()
    scale_max_value.pack()
    check_box.pack()
    label.pack()
    label2.pack()
    scale_min_value.set(8)
    scale_max_value.set(12)
    window.mainloop()

def Toggle():
    global toggling
    if (x.get() == 1):
        toggling = True
    elif (x.get() == 0):
        toggling = False

def AutoClicker():
    global toggling
    while True:
        title2 = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        title = win32gui.FindWindow(None, None)
        if "Minecraft" in title2 or "Lunar" in title2 or "Badlion" in title2 or "Client" in title2 or "AZ" in title2 or "Arckade" in title2:
            title = win32gui.FindWindow(None, title2)
            if win32api.GetAsyncKeyState(0x01) < 0 and toggling:
                lParam = win32api.MAKELONG(0,0)
                win32api.SendMessage(title, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
                win32api.SendMessage(title, win32con.WM_LBUTTONUP,win32con.MK_LBUTTON, lParam)
                min_cps = (1/scale_min_value.get())
                max_cps = (1/scale_max_value.get())
                randomzer = random.uniform(min_cps, max_cps)
                time.sleep(randomzer)
            else:
                pass
        elif toggling != True:
            pass



if __name__ == "__main__":
    t1 = threading.Thread(target=Initialize_Window)
    t1.start()
    t2 = threading.Thread(target=AutoClicker)
    t2.start()










