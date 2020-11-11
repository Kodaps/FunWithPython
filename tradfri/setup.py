#!/usr/bin/env python3
"""
This sets up the conf file with the TradFri identity & key 
To run the script, do the following:
$ pip3 install pytradfri
$ python3 setup.py <IP>
Where <IP> is the address to your IKEA gateway. The first time
running you will be asked to input the 'Security Code' found on
the back of your IKEA gateway.
"""

# pylint: disable=import-error
from pytradfri import Gateway
from pytradfri.api.libcoap_api import APIFactory
from pytradfri.error import PytradfriError

import json
import uuid
import argparse
import threading
import time

CONFIG_FILE = "tradfri_conf.json"

try:
    with open(CONFIG_FILE) as json_file:
        conf = json.load(json_file)
except:
    conf = {}

parser = argparse.ArgumentParser()
parser.add_argument(
    "host", metavar="IP", type=str, help="IP Address of your Tradfri gateway"
)
parser.add_argument(
    "-K",
    "--key",
    dest="key",
    required=False,
    help="Security code found on your Tradfri gateway",
)

args = parser.parse_args()

if args.host not in conf and args.key is None:
    print(
        "Please provide the 'Security Code' on the back of your " "Tradfri gateway:",
        end=" ",
    )
    key = input().strip()
    if len(key) != 16:
        raise PytradfriError("Invalid 'Security Code' provided.")
    else:
        args.key = key

# Assign configuration variables.
# The configuration check takes care they are present.


try:
    identity = conf["identity"]
    psk = conf["key"]
    api_factory = APIFactory(host=args.host, psk_id=identity, psk=psk)
except KeyError:
    print("key error")
    identity = uuid.uuid4().hex
    api_factory = APIFactory(host=args.host, psk_id=identity)

    try:
        psk = api_factory.generate_psk(args.key)
        print("Generated PSK: ", psk)

        conf = {"identity": identity, "key": psk, "ip": args.host}
        with open(CONFIG_FILE, 'w') as outfile:
          json.dump(conf, outfile)

    except AttributeError:
        print("AttributeError error")

        raise PytradfriError(
            "Please provide the 'Security Code' on the "
            "back of your Tradfri gateway using the "
            "-K flag."
        )
