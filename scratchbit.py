# microbit scratch by Experience Workshop (Akos Vecsei)

# import microbit module
from microbit import *


# Create and send Scratch data packet
def convert(a, b):
    sensor = bytearray(2)
    upper = (b & 0x380) >> 7
    sensor[1] = b & 0x7f
    sensor[0] = (1 << 7) | a << 3 | upper
    uart.write(sensor)


# Welcome screen
display.scroll('Connect USB cable! In Scratch add PicoBoard extension !')
# Set USB speed
uart.init(38400)
request = bytearray(1)

while True:
# Listen to Scratch
    if uart.readinto(request) == 1 and request[0] == 0x01:
        display.show('C')
        convert(15, 0x04)
        b = 1000
# Get accelerometer's y value from MicroBit
        reading = accelerometer.get_y()
        if reading >= 0:
            reading = int(reading / 2) + 512
            convert(0, reading)
        else:
            reading = 512 - abs(int(reading / 2))
            convert(0, reading)
# Get accelerometer's x value from MicroBit
        reading = accelerometer.get_x()
        if reading >= 0:
            reading = int(reading / 2) + 512
            convert(1, reading)
        else:
            reading = 512 - abs(int(reading / 2))
            convert(1, reading)
# Read button B state from MicroBit
        if button_b.is_pressed():
            convert(2, 1023)
        else:
            convert(2, 0)
        convert(3, b)
# Read button A state from MicroBit
        if button_a.is_pressed():
            convert(4, 1023)
        else:
            convert(4, 0)
# Read P0 analog value from MicroBit
            convert(5, 1023 - pin0.read_analog())
# Read P1 analog value from MicroBit
            convert(6, pin1.read_analog())
# Read P2 analog value from MicroBit
            convert(7, pin2.read_analog())
