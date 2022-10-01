#!/usr/bin/python
# majority copied from SO https://stackoverflow.com/questions/5060710/format-of-dev-input-event
import struct
import time
import sys
import os

#infile_path = "/dev/input/event" + (sys.argv[1] if len(sys.argv) > 1 else "0")
infile_path="/dev/input/by-id/usb-Raspberry_Pi_Pico_E66038B71399682F-if03-event-kbd"

"""
FORMAT represents the format used by linux kernel input event struct
See https://github.com/torvalds/linux/blob/v5.5-rc5/include/uapi/linux/input.h#L28
Stands for: long int, long int, unsigned short, unsigned short, unsigned int
"""
FORMAT = 'llHHI'
EVENT_SIZE = struct.calcsize(FORMAT)

#open file in binary mode
in_file = open(infile_path, "rb")

event = in_file.read(EVENT_SIZE)

while event:
    (tv_sec, tv_usec, type, code, value) = struct.unpack(FORMAT, event)

    if type != 0 or code != 0 or value != 0:
        #print("Event type %u, code %u, value %u at %d.%d" % \
        #    (type, code, value, tv_sec, tv_usec))
        if code==115 and value==1:
            print("volume up")
            os.system("pactl set-sink-volume @DEFAULT_SINK@ +5%")
        elif code==114 and value==1:
            print("volume down")
            os.system("pactl set-sink-volume @DEFAULT_SINK@ -5%")
        elif code==164 and value==1:
            print("mpc toggle")
            os.system("mpc -h 192.168.1.6 toggle")
    #else:
        # Events with code, type and value == 0 are "separator" events
        #print("===========================================")

    event = in_file.read(EVENT_SIZE)

in_file.close()
