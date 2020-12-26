import pyautogui
import time
import random

time.sleep(2)

file = open("swearings.txt",'r').read()
file = file.splitlines()

for i in range(50):
    pyautogui.typewrite(random.choice(file))
    pyautogui.press('enter')
    time.sleep(0.5)



