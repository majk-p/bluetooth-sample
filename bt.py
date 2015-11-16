#!/usr/bin/python
from PyOBEX.client import BrowserClient as bc
import bluetooth

DEVICE_NAME = 'mp'

devices = bluetooth.discover_devices()
device = None
port = 20
for dev in devices:
    dev_name = bluetooth.lookup_name(dev)
    print "Discovered device: [{0}][{1}]".format(dev, dev_name)
    if dev_name == DEVICE_NAME:
        device = dev
        # services = bluetooth.find_service(address = device)
        svc = bluetooth.find_service(address = device, uuid = bluetooth.OBEX_FILETRANS_CLASS)
        port = svc[0]['port']
        # print services
        # for sv in services:
        #     if sv != None and sv['name'] != None and sv['name'].find('OBEX') != -1:
        #         port = sv['port']
        #         print sv
        #         print "Discovered OBEX service at port: {0}".format(port)
        break

if device != None:
    client = bc(device, port)
    client.connect()
    client.setpath('PHONE_MEMORY')
    client.put('success.txt', 'spam and stuff')
    client.disconnect()

