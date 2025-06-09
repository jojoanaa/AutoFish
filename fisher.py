import pyautogui
import time
import numpy as np
import cv2
from PIL import ImageGrab
import keyboard

# bot status
running = True
screen_center = (960, 540)  # standard: 1920x1080

def select_res():
    global screen_center
    print("Choose your resolution (press 1, 2 or 3):")
    print("1. 1920x1080")
    print("2. 2560x1440")
    print("3. 3840x2160")

    while True:
        if keyboard.is_pressed("1"):
            screen_center = (960, 540)
            print("1920x1080 was chosen.")
            break
        elif keyboard.is_pressed("2"):
            screen_center = (1280, 720)
            print("2560x1440 was chosen.")
            break
        elif keyboard.is_pressed("3"):
            screen_center = (1920, 1080)
            print("3840x2160 was chosen.")
            break
        time.sleep(0.1)

# function for right click
def right_click():
    pyautogui.mouseDown(button='right')
    time.sleep(0.1)
    pyautogui.mouseUp(button='right')

# function to check if red is within range of crosshair
def color_check():
    x, y = screen_center
    offset = 20
    bbox = (x - offset, y - offset, x + offset, y + offset)

    try:
        screen_rgb = np.array(ImageGrab.grab(bbox=bbox))
        if screen_rgb.size == 0:
            return False
        hsv_img = cv2.cvtColor(screen_rgb, cv2.COLOR_RGB2HSV)
    except Exception as e:
        print(f"Error during screen: {e}")
        return False

    # red part of the bobber
    red_hsv = (0, 200, 220)
    h_tolerance_red = 25
    sv_tolerance_red = 85

    # checks for red part
    h, s, v = red_hsv
    lower_red1 = np.array([0, max(s - sv_tolerance_red, 0), max(v - sv_tolerance_red, 0)])
    upper_red1 = np.array([h + h_tolerance_red, min(s + sv_tolerance_red, 255), min(v + sv_tolerance_red, 255)])
    mask_red1 = cv2.inRange(hsv_img, lower_red1, upper_red1)

    lower_red2 = np.array([179 - h_tolerance_red, max(s - sv_tolerance_red, 0), max(v - sv_tolerance_red, 0)])
    upper_red2 = np.array([179, min(s + sv_tolerance_red, 255), min(v + sv_tolerance_red, 255)])
    mask_red2 = cv2.inRange(hsv_img, lower_red2, upper_red2)

    if np.any(mask_red1) or np.any(mask_red2):
        return True 

    # no red = fish is on rod
    return False

def start_fishing():
    global running
    running = True
    select_res()

    while running:
        right_click()
        print("- Throwing out fishing line. -")
        time.sleep(2.5)

        while running:
            if not color_check():
                print("Fish on rod! :3")
                right_click()
                print("- Reeling in line. -")
                time.sleep(1)
                break
            time.sleep(0.1)

    print("Not auto fishing anymore.")

def stop_fishing():
    global running
    print("Stopping bot...")
    running = False