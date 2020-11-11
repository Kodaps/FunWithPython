#!/usr/bin/env python3
import time

from lightutils import lights,setLightHSB

for i in range(33):
    for light in lights:
        print(print("Name: {} @ {}".format(light.name, i*6000)))
        setLightHSB(light, i*1000, 65279, 254)

    time.sleep(3)

