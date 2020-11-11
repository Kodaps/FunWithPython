#!/usr/bin/env python3
"""
This is an example of how the pytradfri-library can be used.
To run the script, do the following:
$ pip3 install pytradfri
$ python3 setupconf.py <IP>
Where <IP> is the address to your IKEA gateway. The first time
running you will be asked to input the 'Security Code' found on
the back of your IKEA gateway.
$ python3 list.py
"""

from lightutils import lights,api

state = False

for light in lights:

    # What is the name of the light ?
    print("Name: {}".format(light.name))
    state_command = light.light_control.set_state(True)
    api(state_command)
