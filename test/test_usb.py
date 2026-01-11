# OS: Ubuntu 25.10

import logging

from edlclient.Library.Connection import serial_lib
from edlclient.Config import usb_ids

device = serial_lib.SerialDevice(log_level=logging.DEBUG, port_config=usb_ids.default_ids, enabled_log=True, enabled_print=True)
print('[INFO] --- The serial_lib.SerialDevice was init success. ---')

print(f'--- Devices: {device.detect_devices()} ---')
