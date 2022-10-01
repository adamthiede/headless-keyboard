## install on a RPI Pico with circuitpython, add adafruit_hid library
## hook buttons up to GPIO 16, 18, 19 and RGB LED to 1, 2, 3
import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

print("RUN")

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value=True

rled = digitalio.DigitalInOut(board.GP1)
rled.direction = digitalio.Direction.OUTPUT
gled = digitalio.DigitalInOut(board.GP2)
gled.direction = digitalio.Direction.OUTPUT
bled = digitalio.DigitalInOut(board.GP3)
bled.direction = digitalio.Direction.OUTPUT

# print("red")
# rled.value=True
# time.sleep(1)
# rled.value=False
# print("green")
# gled.value=True
# time.sleep(1)
# gled.value=False
# print("blue")
# bled.value=True
# time.sleep(1)
# bled.value=False

keyboard=Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

b16_pin=board.GP16
b16=digitalio.DigitalInOut(b16_pin)
b16.direction=digitalio.Direction.INPUT
b16.pull=digitalio.Pull.UP

b18_pin=board.GP18
b18=digitalio.DigitalInOut(b18_pin)
b18.direction=digitalio.Direction.INPUT
b18.pull=digitalio.Pull.UP

b19_pin=board.GP19
b19=digitalio.DigitalInOut(b19_pin)
b19.direction=digitalio.Direction.INPUT
b19.pull=digitalio.Pull.UP

time.sleep(1)
led.value=False
rled.value=False
gled.value=False
bled.value=False

while True:
    #print(f"b16: {b16.value} b18: {b18.value}")
    if (b16.value==False):
        # vol up
        rled.value=True
        cc.press(ConsumerControlCode.VOLUME_INCREMENT)
        cc.release()
        time.sleep(0.4)
        rled.value=False
    elif (b18.value==False):
        # vol down
        bled.value=True
        cc.press(ConsumerControlCode.VOLUME_DECREMENT)
        cc.release()
        time.sleep(0.4)
        bled.value=False
    elif (b19.value==False):
        # play pause
        gled.value=True
        cc.press(ConsumerControlCode.PLAY_PAUSE)
        cc.release()
        time.sleep(0.4)
        gled.value=False
    time.sleep(0.1)

