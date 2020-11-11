#!/usr/bin/env python3
import time

from lightutils import lights,setColor, colorList, COLOR_NAMES

for color in colorList:
    for light in lights:
        setColor(light, color)
    print(COLOR_NAMES[color])
    time.sleep(2)

