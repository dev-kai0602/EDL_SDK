# OS: Ubuntu25.10
import logging

from edlclient.Library.Connection import usblib

temp_port_config = [[0x2d95, 0x6013, -1]]
usb = usblib.USBClass(log_level=logging.DEBUG, port_config=temp_port_config, enabled_log=True, enabled_print=True)

print(f'[INFO] USB interface count: {usb.get_interface_count()}')
