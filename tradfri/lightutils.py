#!/usr/bin/env python3
"""
Utilities for Ikea lights
"""

import json

# pylint: disable=import-error
from pytradfri import Gateway
from pytradfri.api.libcoap_api import APIFactory


CONFIG_FILE = "tradfri_conf.json"

with open(CONFIG_FILE) as json_file:
  conf = json.load(json_file)

# get setting from json
identity = conf["identity"]
psk = conf["key"]
host=conf["ip"]


api_factory = APIFactory(host=host, psk_id=identity, psk=psk)

# expose api endpoint
api = api_factory.request

gateway = Gateway()

# get the command to get all the devices 
devices_command = gateway.get_devices()
# get the list of devices 
devices_commands = api(devices_command)
# get the devices corresponding to the list
devices = api(devices_commands)

# get the lights in the list
lights = [dev for dev in devices if dev.has_light_control]

COLOR_NAMES = {
    "4a418a": "Blue",
    "6c83ba": "Light Blue",
    "8f2686": "Saturated Purple",
    "a9d62b": "Lime",
    "c984bb": "Light Purple",
    "d6e44b": "Yellow",
    "d9337c": "Saturated Pink",
    "da5d41": "Dark Peach",
    "dc4b31": "Saturated Red",
    "dcf0f8": "Cold sky",
    "e491af": "Pink",
    "e57345": "Peach",
    "e78834": "Warm Amber",
    "e8bedd": "Light Pink",
    "eaf6fb": "Cool daylight",
    "ebb63e": "Candlelight",
    "efd275": "Warm glow",
    "f1e0b5": "Warm white",
    "f2eccf": "Sunrise",
    "f5faf6": "Cool white",
}

colorList = []

for color in COLOR_NAMES:
  colorList.append(color)


def setLightHSB(light, h,s,b):
    command = light.light_control.set_hsb(h, s, b, transition_time=2) # #217272 #c61c8e
    api(command)

def setLightState(light, state):
    command = light.light_control.set_state(True)
    api(command)

def setLightIntensity(light, level):
    command = light.light_control.set_dimmer(level, transition_time=2)
    api(command)

def setColor(light, color):
    command = light.light_control.set_hex_color(color, transition_time=2)
    api(command)

def setColorIndex(light, color_id):
    setColor(light, colorList[color_id])