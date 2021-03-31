import pyautogui as pg
import time

pg.FAILSAFE = True

########
# MAIN #
########

latence = 3

for i in range(latence):
    print(latence-i)
    time.sleep(1)

cars = ["Ford", "Volvo", "BMW"]

for i in cars:
    pg.write(i)
    pg.press("space")