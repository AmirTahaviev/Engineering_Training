import RPi.GPIO as GPI0
import time

GPI0.setmode(GPI0.BCM)

leds = [24, 22, 23, 27, 17, 25, 5, 16]

for led in leds:
    GPI0.setup(led, GPI0.OUT)
for led in leds:
    GPI0.output(led, 0)

light_time = 0.2

for led in leds:
    GPI0.output(led, 1)
    time.sleep(light_time)
    GPI0.output(led, 0)

while True:
    for led in leds:
        GPI0.output(led, 1)
        time.sleep(light_time)
        GPI0.output(led, 0)
