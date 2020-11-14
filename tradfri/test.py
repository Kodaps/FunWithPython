
#!/usr/bin/env python3
import time

from lightutils import lights, setColorIndex, setLightIntensity, setLightState, colorList

for i in range (len(colorList)):
  for light in lights:
    setColorIndex(light, i)
  time.sleep(2)