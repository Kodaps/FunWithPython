#!/usr/bin/env python3
import time

from lightutils import lights,setLightIntensity

for light in lights:
    setLightIntensity(light, 100)
