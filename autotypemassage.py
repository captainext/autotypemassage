import pyautogui
import time

time.sleep(1)
count = 1
while count <= 30:
    pyautogui.typewrite(str(count) + '.' + 'Text Massage')
    pyautogui.press('enter')
    count = count + 1
