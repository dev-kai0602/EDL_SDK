# OS: Ubuntu 25.10
# TODO: 该测试因没有串口设备而无法测试

import logging

from edlclient.Library.Connection import seriallib
# from edlclient.Config import usb_ids

temp_vid_pid = [[0x0000, 0x0000, -1], [None, None, -1]]

device = serial_lib.SerialDevice(log_level=logging.DEBUG, port_config=temp_vid_pid, enabled_log=True, enabled_print=True)
print('[INFO] --- The serial_lib.SerialDevice was init success. ---')

print(f'[INFO] --- Connect start: {device.connect()}')
print(f'[INFO] --- Devices: {device.detect_devices()} ---')
