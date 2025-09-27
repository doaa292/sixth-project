import pyautogui
import time

pyautogui.moveTo(1247, 17, duration=1)
pyautogui.click()
time.sleep(0.5)

pyautogui.moveTo(187, 32, duration=1)
pyautogui.click()
pyautogui.click()
time.sleep(0.5)

pyautogui.moveTo(1345, 62, duration=1)
pyautogui.click()
time.sleep(0.5)

pyautogui.moveTo(1202, 157, duration=1)
pyautogui.click()
time.sleep(0.5)
pyautogui.moveTo(705, 62, duration=1
                 )
pyautogui.click()
time.sleep(0.5)
pyautogui.typewrite("How to use pyautogui lib?", interval=0.05)
pyautogui.press('enter')