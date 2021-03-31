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

with open("La tirade du nez, Cyrano de Bergerac.txt", 'r') as tirade:
    lines = tirade.readlines()
    for attribute in lines:
        num = attribute.split()
        for i in num:
            pg.write(i)
            pg.press("space")