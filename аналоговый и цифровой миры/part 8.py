import RPi.GPIO as GPI0
import time

GPI0.setmode(GPI0.BCM)


leds = [16, 5, 25, 17, 27, 23, 22, 24]

for led in leds:
    GPI0.setup(led, GPI0.OUT)
for led in leds:
    GPI0.output(led, 0)



up = 9
down = 10
GPI0.setup(up, GPI0.IN)
GPI0.setup(down, GPI0.IN)

num = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2

while True:
    if GPI0.input(up):
        num = num + 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)

    if GPI0.input(down):
        num = num - 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    GPI0.output(leds, dec2bin(num))
    if num > 127:
        num = 0

