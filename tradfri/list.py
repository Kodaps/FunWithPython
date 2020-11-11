#!/usr/bin/env python3
import time

from lightutils import lights,setLightHSB

# Lights can be accessed by its index, so lights[1] is the second light
for light in lights:
    # What is the name of the light ?
    print("Name: {}".format(light.name))

    # What is the nb of lights on the light ?
    print("Number of lights: {}".format(len(light.light_control.lights)))

    # Checks state of the light (true=on)
    print("State: {}".format(light.light_control.lights[0].state))

    # Get dimmer level of the light
    print("Dimmer: {}".format(light.light_control.lights[0].dimmer))

