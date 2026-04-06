import RPi.GPIO as GPI0
import time

GPI0.setmode(GPI0.BCM)

led = 26
GPI0.setup(led, GPI0.OUT)
button = 13
GPI0.setup(button, GPI0.IN)
state = False
GPI0.output(led, state)

while True:
    if GPI0.input(button):
        state = not state
        GPI0.output(led, state)
        time.sleep(0.2)